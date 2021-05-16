import sys
from kyan.kyan_main import KyanUI
from PySide6.QtWidgets import QApplication


app = QApplication(sys.argv)
KyanUI = KyanUI()
KyanUI.show()
app.exec_()
KyanUI.audio_handler.pyaudio.terminate()
