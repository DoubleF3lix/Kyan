# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_audio_file.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_import_audio_file(object):
    def setupUi(self, import_audio_file):
        if not import_audio_file.objectName():
            import_audio_file.setObjectName(u"import_audio_file")
        import_audio_file.resize(250, 180)
        import_audio_file.setMinimumSize(QSize(250, 180))
        import_audio_file.setMaximumSize(QSize(250, 180))
        self.action_configure_audio_devices = QAction(import_audio_file)
        self.action_configure_audio_devices.setObjectName(u"action_configure_audio_devices")
        self.centralwidget = QWidget(import_audio_file)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 230, 20))
        self.import_button = QPushButton(self.centralwidget)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setGeometry(QRect(10, 140, 230, 30))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 120, 230, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 230, 20))
        self.select_file_button = QPushButton(self.centralwidget)
        self.select_file_button.setObjectName(u"select_file_button")
        self.select_file_button.setGeometry(QRect(220, 29, 21, 24))
        self.audio_name_box = QLineEdit(self.centralwidget)
        self.audio_name_box.setObjectName(u"audio_name_box")
        self.audio_name_box.setGeometry(QRect(10, 90, 231, 22))
        self.audio_name_box.setMaxLength(35)
        self.audio_name_box.setReadOnly(False)
        self.file_path_display = QLineEdit(self.centralwidget)
        self.file_path_display.setObjectName(u"file_path_display")
        self.file_path_display.setGeometry(QRect(10, 30, 205, 22))
        self.file_path_display.setReadOnly(True)
        import_audio_file.setCentralWidget(self.centralwidget)

        self.retranslateUi(import_audio_file)

        QMetaObject.connectSlotsByName(import_audio_file)
    # setupUi

    def retranslateUi(self, import_audio_file):
        import_audio_file.setWindowTitle(QCoreApplication.translate("import_audio_file", u"Import Audio", None))
        self.action_configure_audio_devices.setText(QCoreApplication.translate("import_audio_file", u"Configure Audio Devices", None))
        self.label.setText(QCoreApplication.translate("import_audio_file", u"Select File:", None))
        self.import_button.setText(QCoreApplication.translate("import_audio_file", u"Import", None))
        self.label_2.setText(QCoreApplication.translate("import_audio_file", u"Audio Name:", None))
        self.select_file_button.setText(QCoreApplication.translate("import_audio_file", u"...", None))
    # retranslateUi

