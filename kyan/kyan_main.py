import audioop
import json
import os
import pyaudio  
import sounddevice
import threading
import wave
from pydub import AudioSegment
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFileDialog, QLabel, QMainWindow, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QMetaObject


# Adapted from https://gist.github.com/cpbotha/1b42a20c8f3eb9bb7cb8 (licensed under MIT)
class UiLoader(QUiLoader):
    def __init__(self, base_instance):
        QUiLoader.__init__(self, base_instance)
        self.base_instance = base_instance

    def createWidget(self, class_name, parent=None, name=''):
        if parent is None and self.base_instance:
            return self.base_instance
        else:
            widget = QUiLoader.createWidget(self, class_name, parent, name)
            if self.base_instance:
                setattr(self.base_instance, name, widget)
            return widget

def load_ui(ui_file, base_instance=None):
    loader = UiLoader(base_instance)

    widget = loader.load(ui_file)
    QMetaObject.connectSlotsByName(widget)
    return widget


class AudioHandler:
    def __init__(self, parent):
        self.parent = parent
        self.pyaudio = pyaudio.PyAudio()
        self.CHUNK_SIZE = 1024
        self.RATE = 44100
        self.sound_volume = 1
        self.mic_volume = 1
        self.can_play_audio = True
        self.sound_count = 0

        # These will use the default devices
        selected_devices = self.parent.config_manager.get_config()["selected_devices"]
        self.input_device_index = selected_devices["input"]
        self.output_device_index = selected_devices["output"]

        mic_to_vac_pipe_thread = threading.Thread(target=self.mic_to_vac_pipe, daemon=True)
        mic_to_vac_pipe_thread.start()

    def get_audio_devices(self):
        output = {"input": [], "output": []}
        info = self.pyaudio.get_host_api_info_by_index(0)
        for index in range(0, info.get("deviceCount")):
            q = self.pyaudio.get_device_info_by_host_api_device_index(0, index)
            if q.get("maxInputChannels") != 0:
                output["input"].append({"index": index, "name": q["name"]})
            if q.get("maxOutputChannels") != 0:
                output["output"].append({"index": index, "name": q["name"]})
        return output

    def play_audio(self, file):
        try:
            # Initalize streams
            wave_file = wave.open(file, "rb")
            stream1 = self.pyaudio.open(
                format=self.pyaudio.get_format_from_width(wave_file.getsampwidth()),
                channels=wave_file.getnchannels(),
                rate=wave_file.getframerate(),
                output_device_index=self.output_device_index,
                output=True
            )
            if self.output_device_index != self.parent.default_devices[1]:
                stream2 = self.pyaudio.open(
                    format=self.pyaudio.get_format_from_width(wave_file.getsampwidth()),
                    channels=wave_file.getnchannels(),
                    rate=wave_file.getframerate(),
                    output_device_index=self.parent.default_devices[1],
                    output=True
                )

            # Write inital data
            self.sound_count += 1
            data = wave_file.readframes(self.CHUNK_SIZE)
            stream1.write(self.change_volume(data, self.sound_volume), self.CHUNK_SIZE)
            if self.output_device_index != self.parent.default_devices[1]:
                stream2.write(self.change_volume(data, self.sound_volume), self.CHUNK_SIZE)

            # Finish writing the data
            while data != b"":
                if self.can_play_audio == False:
                    self.sound_count -= 1
                    if self.sound_count == 0:
                        self.can_play_audio = True
                    return
                stream1.write(self.change_volume(data, self.sound_volume))
                if self.output_device_index != self.parent.default_devices[1]:
                    stream2.write(self.change_volume(data, self.sound_volume))
                data = wave_file.readframes(self.CHUNK_SIZE)

            stream1.stop_stream()
            stream1.close()
            if self.output_device_index != self.parent.default_devices[1]:
                stream2.stop_stream()
                stream2.close()

            self.sound_count -= 1
        except FileNotFoundError:
            self.parent.delete_sound()
            pass # Sound was deleted improperly

    def initialize_streams(self):
        self.microphone_input_stream = self.pyaudio.open(
            format=self.pyaudio.get_format_from_width(2),
            channels=1,
            rate=self.RATE,
            input=True,
            output=True,
            input_device_index=self.input_device_index,
            frames_per_buffer=self.CHUNK_SIZE
        )

        self.cable_output_stream = self.pyaudio.open(
            format=self.pyaudio.get_format_from_width(2),
            channels=1,
            rate=self.RATE,
            output=True,
            output_device_index=self.output_device_index,
            frames_per_buffer=self.CHUNK_SIZE
        )

        self.speaker_output_stream = self.pyaudio.open(
            format=self.pyaudio.get_format_from_width(2),
            channels=1,
            rate=self.RATE,
            output=True,
            output_device_index=self.parent.default_devices[1],
            frames_per_buffer=self.CHUNK_SIZE
        )

    def update_device_indices(self, input=None, output=None):
        if input:
            self.input_device_index = input
        if output:
            self.output_device_index = output
        self.initialize_streams()

    def mic_to_vac_pipe(self):
        self.initialize_streams()

        # This will last for 217483647 seconds, or 68.09 years
        for i in range(0, int(self.RATE / self.CHUNK_SIZE * 2147483647)):
            try:
                data = self.microphone_input_stream.read(self.CHUNK_SIZE)
                self.cable_output_stream.write(self.change_volume(data, self.mic_volume), self.CHUNK_SIZE)
                if self.parent.hear_mic_input.isChecked():
                    self.speaker_output_stream.write(self.change_volume(data, self.mic_volume), self.CHUNK_SIZE)
            except OSError as error:
                if error == "[Errno -9988] Stream closed":
                    pass # User closed window

        self.close_streams()

    def close_streams(self):
        self.microphone_input_stream.stop_stream()
        self.microphone_input_stream.close()
        self.cable_output_stream.stop_stream()
        self.cable_output_stream.close()

    def change_volume(self, data, volume):
        return audioop.mul(data, 2, volume)


class ConfigureAudioDevices(QMainWindow):
    def __init__(self, parent):
        self.parent = parent

        super(ConfigureAudioDevices, self).__init__()
        load_ui(os.path.join(os.path.dirname(os.path.abspath(__file__)), "configure_audio_devices.ui"), self)

        self.refresh_button.clicked.connect(self.populate_device_boxes)
        self.submit_button.clicked.connect(self.save_config)

    def populate_device_boxes(self):
        self.input_device_list.clear()
        self.output_device_list.clear()

        self.devices = self.parent.audio_handler.get_audio_devices()
        for item in self.devices["input"]:
            self.input_device_list.addItem(item["name"], item["index"])
        for item in self.devices["output"]:
            self.output_device_list.addItem(item["name"], item["index"])

        # Set active device if it exists
        config_contents = self.parent.config_manager.get_config()
        if config_contents["selected_devices"]["input"] is not None:
            selected_input_device_index = self.input_device_list.findData(config_contents["selected_devices"]["input"])
            self.input_device_list.setCurrentIndex(selected_input_device_index)
        if config_contents["selected_devices"]["output"] is not None:
            selected_output_device_index = self.output_device_list.findData(config_contents["selected_devices"]["output"])
            self.output_device_list.setCurrentIndex(selected_output_device_index)

    def save_config(self):
        selected_input_device_index = self.input_device_list.itemData(self.input_device_list.currentIndex())
        selected_output_device_index = self.output_device_list.itemData(self.output_device_list.currentIndex())
        self.parent.audio_handler.update_device_indices(selected_input_device_index, selected_output_device_index)

        self.parent.config_manager.edit_config(selected_devices={"input": selected_input_device_index, "output": selected_output_device_index})

        self.close()
        

class ConfigManager:
    def __init__(self, parent):
        self.parent = parent
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

    def edit_config(self, selected_devices=None, sound=None, remove_sound=False):
        if not os.path.isfile(self.config_path):
            self.create_config()

        with open(self.config_path, "r") as infile:
            config_contents = json.load(infile)

        if selected_devices is not None:
            config_contents["selected_devices"] = selected_devices
        if sound is not None:
            if remove_sound == False:
                config_contents["sounds"].append(sound)
            else:
                config_contents["sounds"].remove(sound)

        with open(self.config_path, "w") as outfile:
            json.dump(config_contents, outfile, indent=4)

    def get_config(self):
        if not os.path.isfile(self.config_path):
            self.create_config()

        with open(self.config_path, "r") as infile:
            return json.load(infile)

    def create_config(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        config_contents = {"selected_devices": {"input": self.parent.default_devices[0], "output": self.parent.default_devices[1]}, "sounds": []}
        with open(config_path, "w") as outfile:
            json.dump(config_contents, outfile, indent=4)


class NameInUseErrorBox(QDialog):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle("Error")

        self.button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(f"'{name}' is already in use. Overwrite?"))
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class ImportAudioFileUI(QMainWindow):
    def __init__(self, parent):
        self.parent = parent

        super(ImportAudioFileUI, self).__init__()
        load_ui(os.path.join(os.path.dirname(os.path.abspath(__file__)), "import_audio_file.ui"), self)

        self.select_file_button.clicked.connect(self.select_file)
        self.import_button.clicked.connect(self.attempt_audio_import)

    def clear_prompts(self):
        self.file_path_display.setText("")
        self.audio_name_box.setText("")

    def select_file(self):
        selected_audio_file = QFileDialog.getOpenFileName(filter="Audio Files (*.mp3 *.wav *.ogg)")[:-1][0]
        self.file_path_display.setText(selected_audio_file)
        self.audio_name_box.setText(os.path.splitext(os.path.basename(selected_audio_file))[0])

    def attempt_audio_import(self):
        if self.audio_name_box.text() not in self.parent.config_manager.get_config()["sounds"]:
            self.import_audio()
        else:
            error = NameInUseErrorBox(self.audio_name_box.text())
            if error.exec_():
                self.import_audio(add_new_config_entry=False)

    def import_audio(self, add_new_config_entry=True):
        audio_file = AudioSegment.from_file(self.file_path_display.text())
        audio_file.export(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_files", self.audio_name_box.text() + ".wav"), format="wav")
        if add_new_config_entry == True:
            self.parent.config_manager.edit_config(sound=self.audio_name_box.text())
            self.parent.sounds_list.addItem(self.audio_name_box.text())
        self.close()


class KyanUI(QMainWindow):
    def __init__(self):
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_files")):
            os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_files"))

        self.default_devices = sounddevice.default.device # input is index 0, output is index 1

        self.config_manager = ConfigManager(self)
        self.audio_handler = AudioHandler(self)
        self.configure_menu = ConfigureAudioDevices(self)
        self.import_audio_menu = ImportAudioFileUI(self)

        super(KyanUI, self).__init__()
        load_ui(os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.ui"), self)

        self.configure_audio_devices.clicked.connect(self.open_cad_ui)
        self.import_audio_file.clicked.connect(self.open_iaf_ui)
        self.delete_selected_sound.clicked.connect(self.delete_sound)
        self.play_selected_sound.clicked.connect(self.play_sound)
        self.sounds_list.doubleClicked.connect(self.play_sound)
        self.stop_all_sounds.clicked.connect(self.stop_sounds)
        self.mic_volume_slider.valueChanged.connect(self.mic_volume_slider_changed)
        self.sound_volume_slider.valueChanged.connect(self.sound_volume_slider_changed)
        self.mic_volume_display.valueChanged.connect(self.mic_volume_display_changed)
        self.sound_volume_display.valueChanged.connect(self.sound_volume_display_changed)
        self.sounds_list.addItems(self.config_manager.get_config()["sounds"])

        self.show()

    def delete_sound(self):
        try:
            self.config_manager.edit_config(sound=self.sounds_list.currentItem().text(), remove_sound=True)
        except AttributeError:
            pass # Sound is not selected
        try:
            os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_files", f"{self.sounds_list.selectedItems()[0].text()}.wav"))
        except FileNotFoundError:
            pass # Sound file was deleted improperly
        self.sounds_list.takeItem(self.sounds_list.row(self.sounds_list.currentItem()))

    def play_sound(self):
        try:
            audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_files", f"{self.sounds_list.selectedItems()[0].text()}.wav")
            sound_thread = threading.Thread(target=self.audio_handler.play_audio, args=[audio_path], daemon=True)
            sound_thread.start()
        except IndexError:
            pass # Sound is not selected

    def stop_sounds(self):
        self.audio_handler.can_play_audio = False

    def mic_volume_slider_changed(self):
        normalized_value = round(self.mic_volume_slider.value() / 100 + 1, 2)
        self.audio_handler.mic_volume = normalized_value
        self.mic_volume_display.blockSignals(True)
        self.mic_volume_display.setValue(normalized_value)
        self.mic_volume_display.blockSignals(False)

    def sound_volume_slider_changed(self):
        normalized_value = round(self.sound_volume_slider.value() / 100 + 1, 2)
        self.audio_handler.sound_volume = normalized_value
        self.sound_volume_display.blockSignals(True)
        self.sound_volume_display.setValue(normalized_value)
        self.sound_volume_display.blockSignals(False)

    def mic_volume_display_changed(self):
        self.audio_handler.mic_volume = self.mic_volume_display.value()
        self.mic_volume_slider.blockSignals(True)
        self.mic_volume_slider.setValue(self.mic_volume_display.value() * 100 - 100)
        self.mic_volume_slider.blockSignals(False)

    def sound_volume_display_changed(self):
        self.audio_handler.sound_volume = self.sound_volume_display.value()
        self.sound_volume_slider.blockSignals(True)
        self.sound_volume_slider.setValue(self.sound_volume_display.value() * 100 - 100)
        self.sound_volume_slider.blockSignals(False)

    def open_cad_ui(self):
        self.configure_menu.populate_device_boxes()
        self.configure_menu.show()

    def open_iaf_ui(self):
        self.import_audio_menu.clear_prompts()
        self.import_audio_menu.show()
