# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configure_audio_devices.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_configure_audio_devices(object):
    def setupUi(self, configure_audio_devices):
        if not configure_audio_devices.objectName():
            configure_audio_devices.setObjectName(u"configure_audio_devices")
        configure_audio_devices.resize(250, 280)
        configure_audio_devices.setMinimumSize(QSize(250, 280))
        configure_audio_devices.setMaximumSize(QSize(250, 300))
        self.centralwidget = QWidget(configure_audio_devices)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_device_list = QComboBox(self.centralwidget)
        self.input_device_list.setObjectName(u"input_device_list")
        self.input_device_list.setGeometry(QRect(10, 40, 231, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 230, 20))
        self.refresh_button = QPushButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(10, 200, 230, 30))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 230, 20))
        self.label_2.setOpenExternalLinks(True)
        self.output_device_list = QComboBox(self.centralwidget)
        self.output_device_list.setObjectName(u"output_device_list")
        self.output_device_list.setGeometry(QRect(10, 120, 231, 22))
        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(10, 240, 230, 30))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 160, 230, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        configure_audio_devices.setCentralWidget(self.centralwidget)

        self.retranslateUi(configure_audio_devices)

        QMetaObject.connectSlotsByName(configure_audio_devices)
    # setupUi

    def retranslateUi(self, configure_audio_devices):
        configure_audio_devices.setWindowTitle(QCoreApplication.translate("configure_audio_devices", u"Audio Devices", None))
        self.label.setText(QCoreApplication.translate("configure_audio_devices", u"Select Microphone:", None))
        self.refresh_button.setText(QCoreApplication.translate("configure_audio_devices", u"Refresh", None))
        self.label_2.setText(QCoreApplication.translate("configure_audio_devices", u"<html><head/><body><p>Select Virtual Audio Cable: (<a href=\"https://vb-audio.com/Cable/\"><span style=\" text-decoration: underline; color:#0000ff;\">What's this?</span></a>)</p></body></html>", None))
        self.submit_button.setText(QCoreApplication.translate("configure_audio_devices", u"Submit", None))
    # retranslateUi

