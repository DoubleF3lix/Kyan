# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 600)
        main_window.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)

        self.sounds_list = QListWidget(self.centralwidget)
        self.sounds_list.setObjectName(u"sounds_list")
        self.sounds_list.setMinimumSize(QSize(0, 400))
        self.sounds_list.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.sounds_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.play_selected_sound = QPushButton(self.centralwidget)
        self.play_selected_sound.setObjectName(u"play_selected_sound")
        self.play_selected_sound.setMinimumSize(QSize(200, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.play_selected_sound.setFont(font1)

        self.horizontalLayout_2.addWidget(self.play_selected_sound)

        self.stop_all_sounds = QPushButton(self.centralwidget)
        self.stop_all_sounds.setObjectName(u"stop_all_sounds")
        self.stop_all_sounds.setMinimumSize(QSize(200, 60))
        self.stop_all_sounds.setFont(font1)

        self.horizontalLayout_2.addWidget(self.stop_all_sounds)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mic_volume_slider = QSlider(self.centralwidget)
        self.mic_volume_slider.setObjectName(u"mic_volume_slider")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mic_volume_slider.sizePolicy().hasHeightForWidth())
        self.mic_volume_slider.setSizePolicy(sizePolicy)
        self.mic_volume_slider.setMinimum(-100)
        self.mic_volume_slider.setMaximum(100)
        self.mic_volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.mic_volume_slider)

        self.mic_volume_display = QDoubleSpinBox(self.centralwidget)
        self.mic_volume_display.setObjectName(u"mic_volume_display")
        self.mic_volume_display.setMaximumSize(QSize(45, 16777215))
        self.mic_volume_display.setMaximum(2.000000000000000)
        self.mic_volume_display.setSingleStep(0.010000000000000)
        self.mic_volume_display.setValue(1.000000000000000)

        self.horizontalLayout_5.addWidget(self.mic_volume_display)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sound_volume_slider = QSlider(self.centralwidget)
        self.sound_volume_slider.setObjectName(u"sound_volume_slider")
        sizePolicy.setHeightForWidth(self.sound_volume_slider.sizePolicy().hasHeightForWidth())
        self.sound_volume_slider.setSizePolicy(sizePolicy)
        self.sound_volume_slider.setMinimum(-100)
        self.sound_volume_slider.setMaximum(100)
        self.sound_volume_slider.setValue(0)
        self.sound_volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.sound_volume_slider)

        self.sound_volume_display = QDoubleSpinBox(self.centralwidget)
        self.sound_volume_display.setObjectName(u"sound_volume_display")
        self.sound_volume_display.setMaximumSize(QSize(45, 16777215))
        self.sound_volume_display.setMaximum(2.000000000000000)
        self.sound_volume_display.setSingleStep(0.010000000000000)
        self.sound_volume_display.setValue(1.000000000000000)

        self.horizontalLayout_6.addWidget(self.sound_volume_display)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.hear_mic_input = QCheckBox(self.centralwidget)
        self.hear_mic_input.setObjectName(u"hear_mic_input")

        self.verticalLayout.addWidget(self.hear_mic_input)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.configure_audio_devices = QPushButton(self.centralwidget)
        self.configure_audio_devices.setObjectName(u"configure_audio_devices")
        self.configure_audio_devices.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.configure_audio_devices)

        self.import_audio_file = QPushButton(self.centralwidget)
        self.import_audio_file.setObjectName(u"import_audio_file")
        self.import_audio_file.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.import_audio_file)

        self.delete_selected_sound = QPushButton(self.centralwidget)
        self.delete_selected_sound.setObjectName(u"delete_selected_sound")
        self.delete_selected_sound.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.delete_selected_sound)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Kyan", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"Sounds:", None))
        self.play_selected_sound.setText(QCoreApplication.translate("main_window", u"Play Selected Sound", None))
        self.stop_all_sounds.setText(QCoreApplication.translate("main_window", u"Stop All Sounds", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Microphone Volume:", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Sound Volume:", None))
        self.hear_mic_input.setText(QCoreApplication.translate("main_window", u"Hear Microphone Input", None))
        self.configure_audio_devices.setText(QCoreApplication.translate("main_window", u"Configure Audio Devices", None))
        self.import_audio_file.setText(QCoreApplication.translate("main_window", u"Import Audio File", None))
        self.delete_selected_sound.setText(QCoreApplication.translate("main_window", u"Delete Selected Sound", None))
    # retranslateUi

