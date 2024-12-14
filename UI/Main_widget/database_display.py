import json
import os
import csv
import runpy
from ping3 import ping
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QVBoxLayout, QListWidget, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from Main_widget.MongoDB.connect import DB
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databaseualVMn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_database_widget(object):
    def setupUi(self, database_widget):
        if not database_widget.objectName():
            database_widget.setObjectName(u"database_widget")
        database_widget.resize(1163, 725)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(125, 125, 125, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(187, 187, 187, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(156, 156, 156, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(62, 62, 62, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(83, 83, 83, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        database_widget.setPalette(palette)
        self.horizontalLayout = QHBoxLayout(database_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 11, -1, -1)
        self.right_main_widget = QFrame(database_widget)
        self.right_main_widget.setObjectName(u"right_main_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_main_widget.sizePolicy().hasHeightForWidth())
        self.right_main_widget.setSizePolicy(sizePolicy)
        self.right_main_widget.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.right_main_widget.setFrameShape(QFrame.StyledPanel)
        self.right_main_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.right_main_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.right_main_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.data_table = QTableWidget(self.right_main_widget)
        self.data_table.setObjectName(u"data_table")

        self.verticalLayout_5.addWidget(self.data_table)


        self.horizontalLayout.addWidget(self.right_main_widget)

        self.left_main_widget = QFrame(database_widget)
        self.left_main_widget.setObjectName(u"left_main_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_main_widget.sizePolicy().hasHeightForWidth())
        self.left_main_widget.setSizePolicy(sizePolicy1)
        self.left_main_widget.setStyleSheet(u"")
        self.left_main_widget.setFrameShape(QFrame.StyledPanel)
        self.left_main_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_main_widget)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(self.left_main_widget)
        self.login_frame.setObjectName(u"login_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.login_frame.sizePolicy().hasHeightForWidth())
        self.login_frame.setSizePolicy(sizePolicy2)
        self.login_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.login_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.login_frame)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy2.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy2)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.top_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.login_message = QLabel(self.top_frame)
        self.login_message.setObjectName(u"login_message")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.login_message.sizePolicy().hasHeightForWidth())
        self.login_message.setSizePolicy(sizePolicy3)
        self.login_message.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.login_message)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.login_frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.bottom_frame.sizePolicy().hasHeightForWidth())
        self.bottom_frame.setSizePolicy(sizePolicy4)
        self.bottom_frame.setLayoutDirection(Qt.LeftToRight)
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 5)
        self.frame = QFrame(self.bottom_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 11, 5, 11)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.username_text = QLineEdit(self.frame)
        self.username_text.setObjectName(u"username_text")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.username_text.sizePolicy().hasHeightForWidth())
        self.username_text.setSizePolicy(sizePolicy5)
        self.username_text.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_2.addWidget(self.username_text, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.password_text = QLineEdit(self.frame)
        self.password_text.setObjectName(u"password_text")
        sizePolicy5.setHeightForWidth(self.password_text.sizePolicy().hasHeightForWidth())
        self.password_text.setSizePolicy(sizePolicy5)
        self.password_text.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_2.addWidget(self.password_text, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        self.holder_6 = QFrame(self.bottom_frame)
        self.holder_6.setObjectName(u"holder_6")
        sizePolicy2.setHeightForWidth(self.holder_6.sizePolicy().hasHeightForWidth())
        self.holder_6.setSizePolicy(sizePolicy2)
        self.holder_6.setFrameShape(QFrame.StyledPanel)
        self.holder_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.holder_6)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.login_button = QPushButton(self.holder_6)
        self.login_button.setObjectName(u"login_button")
        sizePolicy2.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy2)
        self.login_button.setMinimumSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        brush9 = QBrush(QColor(243, 243, 243, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush9)
        brush10 = QBrush(QColor(116, 116, 116, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush10)
        brush11 = QBrush(QColor(155, 155, 155, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush13 = QBrush(QColor(232, 232, 232, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.login_button.setPalette(palette1)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(255, 255, 255);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:1px solid gray;\n"
"	border-radius: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.login_button)

        self.guest_login_button = QPushButton(self.holder_6)
        self.guest_login_button.setObjectName(u"guest_login_button")
        sizePolicy3.setHeightForWidth(self.guest_login_button.sizePolicy().hasHeightForWidth())
        self.guest_login_button.setSizePolicy(sizePolicy3)
        self.guest_login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.guest_login_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(255, 255, 255);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:1px solid gray;\n"
"	border-radius: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.guest_login_button)


        self.verticalLayout_4.addWidget(self.holder_6)


        self.verticalLayout_2.addWidget(self.bottom_frame)


        self.verticalLayout.addWidget(self.login_frame)

        self.upload_frame = QFrame(self.left_main_widget)
        self.upload_frame.setObjectName(u"upload_frame")
        sizePolicy4.setHeightForWidth(self.upload_frame.sizePolicy().hasHeightForWidth())
        self.upload_frame.setSizePolicy(sizePolicy4)
        self.upload_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.upload_frame.setFrameShape(QFrame.StyledPanel)
        self.upload_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.upload_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.upload_frame_2 = QFrame(self.upload_frame)
        self.upload_frame_2.setObjectName(u"upload_frame_2")
        self.upload_frame_2.setStyleSheet(u"QFrame {\n"
"        border: 1px solid gray; \n"
"        \n"
"    }\n"
"")
        self.upload_frame_2.setFrameShape(QFrame.StyledPanel)
        self.upload_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.upload_frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(40, 21, 40, -1)
        self.upload_message = QLabel(self.upload_frame_2)
        self.upload_message.setObjectName(u"upload_message")
        self.upload_message.setStyleSheet(u"QLabel{\n"
"	border:0\n"
"}")

        self.verticalLayout_7.addWidget(self.upload_message)

        self.upload_button = QPushButton(self.upload_frame_2)
        self.upload_button.setObjectName(u"upload_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.upload_button.sizePolicy().hasHeightForWidth())
        self.upload_button.setSizePolicy(sizePolicy6)
        self.upload_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_button.setAutoFillBackground(False)
        self.upload_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(0, 170, 0);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.upload_button.setCheckable(False)
        self.upload_button.setChecked(False)
        self.upload_button.setAutoExclusive(False)
        self.upload_button.setFlat(False)

        self.verticalLayout_7.addWidget(self.upload_button)

        self.status_label = QLabel(self.upload_frame_2)
        self.status_label.setObjectName(u"status_label")
        sizePolicy2.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy2)
        self.status_label.setStyleSheet(u"QLabel{\n"
"	border:0;\n"
"}")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.status_label)

        self.permission_label = QLabel(self.upload_frame_2)
        self.permission_label.setObjectName(u"permission_label")
        sizePolicy2.setHeightForWidth(self.permission_label.sizePolicy().hasHeightForWidth())
        self.permission_label.setSizePolicy(sizePolicy2)
        self.permission_label.setStyleSheet(u"QLabel{\n"
"	border:0;\n"
"}")
        self.permission_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.permission_label)


        self.verticalLayout_6.addWidget(self.upload_frame_2)

        self.download_frame = QFrame(self.upload_frame)
        self.download_frame.setObjectName(u"download_frame")
        self.download_frame.setStyleSheet(u"QFrame {\n"
"        border: 1px solid gray; \n"
"        \n"
"    }\n"
"")
        self.download_frame.setFrameShape(QFrame.StyledPanel)
        self.download_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.download_frame)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(40, 30, 40, 32)
        self.download_message = QLabel(self.download_frame)
        self.download_message.setObjectName(u"download_message")
        self.download_message.setStyleSheet(u"QLabel{\n"
"	border:0\n"
"}")

        self.verticalLayout_8.addWidget(self.download_message)

        self.download_button = QPushButton(self.download_frame)
        self.download_button.setObjectName(u"download_button")
        sizePolicy6.setHeightForWidth(self.download_button.sizePolicy().hasHeightForWidth())
        self.download_button.setSizePolicy(sizePolicy6)
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_button.setAutoFillBackground(False)
        self.download_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(0, 170, 0);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.download_button.setCheckable(False)
        self.download_button.setChecked(False)
        self.download_button.setAutoExclusive(False)
        self.download_button.setFlat(False)

        self.verticalLayout_8.addWidget(self.download_button)

        self.status_label_2 = QLabel(self.download_frame)
        self.status_label_2.setObjectName(u"status_label_2")
        sizePolicy2.setHeightForWidth(self.status_label_2.sizePolicy().hasHeightForWidth())
        self.status_label_2.setSizePolicy(sizePolicy2)
        self.status_label_2.setStyleSheet(u"QLabel{\n"
"	border:0;\n"
"}")
        self.status_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.status_label_2)


        self.verticalLayout_6.addWidget(self.download_frame)

        self.crawl_frame = QFrame(self.upload_frame)
        self.crawl_frame.setObjectName(u"crawl_frame")
        self.crawl_frame.setStyleSheet(u"QFrame {\n"
"        border: 1px solid gray; \n"
"        \n"
"    }\n"
"")
        self.crawl_frame.setFrameShape(QFrame.StyledPanel)
        self.crawl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.crawl_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(40, 21, 40, 11)
        self.crawl_message = QLabel(self.crawl_frame)
        self.crawl_message.setObjectName(u"crawl_message")
        self.crawl_message.setStyleSheet(u"QLabel{\n"
"	border:0\n"
"}")

        self.verticalLayout_9.addWidget(self.crawl_message)

        self.crawl_button = QPushButton(self.crawl_frame)
        self.crawl_button.setObjectName(u"crawl_button")
        sizePolicy6.setHeightForWidth(self.crawl_button.sizePolicy().hasHeightForWidth())
        self.crawl_button.setSizePolicy(sizePolicy6)
        self.crawl_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.crawl_button.setAutoFillBackground(False)
        self.crawl_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(0, 170, 0);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.crawl_button.setCheckable(False)
        self.crawl_button.setChecked(False)
        self.crawl_button.setAutoExclusive(False)
        self.crawl_button.setFlat(False)

        self.verticalLayout_9.addWidget(self.crawl_button)

        self.internet_status_label = QLabel(self.crawl_frame)
        self.internet_status_label.setObjectName(u"internet_status_label")
        sizePolicy2.setHeightForWidth(self.internet_status_label.sizePolicy().hasHeightForWidth())
        self.internet_status_label.setSizePolicy(sizePolicy2)
        self.internet_status_label.setStyleSheet(u"QLabel{\n"
"	border:0;\n"
"}")
        self.internet_status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.internet_status_label)

        self.permission_label_2 = QLabel(self.crawl_frame)
        self.permission_label_2.setObjectName(u"permission_label_2")
        self.permission_label_2.setStyleSheet(u"QLabel{\n"
"	border:0;\n"
"}")

        self.verticalLayout_9.addWidget(self.permission_label_2)


        self.verticalLayout_6.addWidget(self.crawl_frame)


        self.verticalLayout.addWidget(self.upload_frame)


        self.horizontalLayout.addWidget(self.left_main_widget)


        self.retranslateUi(database_widget)

        QMetaObject.connectSlotsByName(database_widget)
    # setupUi

    def retranslateUi(self, database_widget):
        database_widget.setWindowTitle(QCoreApplication.translate("database_widget", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Data</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Hello, Guest</span></p></body></html>", None))
        self.login_message.setText("")
        self.label_3.setText(QCoreApplication.translate("database_widget", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("database_widget", u"Username", None))
        self.login_button.setText(QCoreApplication.translate("database_widget", u"Log in", None))
        self.guest_login_button.setText(QCoreApplication.translate("database_widget", u"Use as guest", None))
        self.upload_message.setText("")
        self.upload_button.setText(QCoreApplication.translate("database_widget", u"Upload", None))
        self.status_label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p><span style=\" font-weight:600;\">Status: </span><span style=\" color:#00ff00;\">Connected</span></p></body></html>", None))
        self.permission_label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p><span style=\" font-weight:600;\">Permisson</span>: <span style=\" color:#00ff00;\">Admin</span></p></body></html>", None))
        self.download_message.setText("")
        self.download_button.setText(QCoreApplication.translate("database_widget", u"Download", None))
        self.status_label_2.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p><span style=\" font-weight:600;\">Status: </span><span style=\" color:#00ff00;\">Connected</span></p></body></html>", None))
        self.crawl_message.setText("")
        self.crawl_button.setText(QCoreApplication.translate("database_widget", u"Crawl", None))
        self.internet_status_label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p><span style=\" font-weight:600;\">Internet: </span><span style=\" color:#00ff00;\">Connected</span></p></body></html>", None))
        self.permission_label_2.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p><span style=\" font-weight:600;\">Permisson</span>: <span style=\" color:#00ff00;\">Admin</span></p></body></html>", None))
    # retranslateUi







class Database_widget(QWidget):
    def __init__(self, parent=None):
        super(Database_widget, self).__init__(parent)
        self.ui = Ui_database_widget()
        self.ui.setupUi(self)
        self.already_login = False
        
        self.ui.login_button.clicked.connect(self.login)
        self.ui.guest_login_button.clicked.connect(self.login_as_guest)
        # Load table
        filename = "\MongoDB\Data\cleaned_data.csv"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.load_csv(script_dir + filename)
        # Handle upload, download and crawl buttons
        self.isConnected = False
        
        self.isAdmin = False
        self.internet = self.is_connected()
        self.change_buttons_status()
        self.ui.download_button.clicked.connect(self.download_button_function)
        self.ui.upload_button.clicked.connect(self.upload_button_function)
        self.ui.crawl_button.clicked.connect(self.crawl_button_function)
        # Hide password
        self.ui.password_text.setEchoMode(QLineEdit.Password)

    def login(self):
        data = {
                "username": str(self.ui.username_text.text()),
                "password": str(self.ui.password_text.text()),
        }

        # Specify the file name
        filename = "\login_data.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Writing the JSON data to a file
        try:
                with open(script_dir + filename, "w") as file:
                        json.dump(data, file, indent=4)  # `indent=4` makes the JSON pretty-printed
                        
        except Exception as e:
                print(f"Error: {e}")
        # Connect to DB
        try:
             db = DB(data["username"], data["password"])
             role = db.get_role()
      
             if role[0]["role"] == "atlasAdmin":
                self.isAdmin = True
             self.db = db
             status = db.try_to_connect()
             print(status)
             if status == "Connected":
                self.ui.login_message.setText("")
                self.isConnected = True
                name = self.create_name_icon(data["username"])
                self.hide_all_widget(self.ui.bottom_frame.layout())
                self.ui.bottom_frame.layout().addWidget(name)
                self.ui.label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Hello, Admin</span></p></body></html>", None))
             else:
                self.isConnected = False
                
                self.ui.login_message.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Invalid username or password</span></p></body></html>", None))
        except:

             self.ui.login_message.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Invalid username or password</span></p></body></html>", None))
        
        
        self.change_buttons_status()
    def login_as_guest(self):
        data = {
                "username": "read_only_user",
                "password": "no_password",
        }

        # Specify the file name
        filename = "\login_data.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Writing the JSON data to a file
        try:
                with open(script_dir + filename, "w") as file:
                        json.dump(data, file, indent=4)  # `indent=4` makes the JSON pretty-printed
                        
        except Exception as e:
                print(f"Error: {e}")
        # Connect to DB
        db = DB(data["username"], data["password"])
        role = db.get_role()
      
        if role[0]["role"] == "atlasAdmin":
             self.isAdmin = True
        self.db = db
        status = db.try_to_connect()
        print(status)
        if status == "Connected":
             self.ui.login_message.setText("")
             self.isConnected = True
             name = self.create_name_icon("Guest")
             self.hide_all_widget(self.ui.bottom_frame.layout())
             self.ui.bottom_frame.layout().addWidget(name)
             self.ui.label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Hello, Guest</span></p></body></html>", None))
        else:
             self.isConnected = False
             self.ui.login_message.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Invalid username or password</span></p></body></html>", None))
        self.change_buttons_status()
    def hide_all_widget(self, layout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()  # Get the widget from the layout item
            widget.hide()
    def show_all_widget(self, layout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()  # Get the widget from the layout item
            widget.show()
    def create_name_icon(self, name):
            frame = QFrame()
            self.isClicked = True 
            self.frame = frame
            label = QPushButton(name, frame)
            label.setGeometry(55, 20, 90, 40)
            icon = QIcon(":/icons/images/icons/cil-arrow-bottom.png")
            label.setIcon(icon)
            label.setLayoutDirection(Qt.RightToLeft)
            label.setStyleSheet("""
                                        QPushButton {
                                        background-color: rgb(255, 255, 255);
                                        font-size: 12px;
                                        color: black;
                                        font-weight: bold;
                                        border: 1px solid gray;
                                        border-radius: 20px;
                                        
                                        
                                        }
                                        
                                        QPushButton:pressed
                                        {
                                                background-color:rgb(218, 218, 218)
                                        }

                                        """)
            label.clicked.connect(self.drop_list_of_options)
            #frame_layout.addWidget(label)
            #frame.setLayout(frame_layout)
            return frame
    def drop_list_of_options(self):
        
        def on_item_selected():
                
                selected_item = self.list_widget.currentItem().text()
                
                if selected_item == "Log out":
                    self.isConnected = False
                    item = self.ui.bottom_frame.layout().itemAt(0)
                    widget = item.widget()  # Get the widget from the layout item
                    widget.close()

                    self.show_all_widget(self.ui.bottom_frame.layout())
                    self.db.disconnect()
                    self.ui.label.setText(QCoreApplication.translate("database_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Hello, Guest</span></p></body></html>", None))
                    
                    filename = "\login_data.json"
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    # Writing the JSON data to a file
                    data = {}

                    try:
                        with open(script_dir + filename, "w") as file:
                                json.dump(data, file, indent=4)  # `indent=4` makes the JSON pretty-printed
                                
                    except Exception as e:
                        print(f"Error: {e}")
                    self.change_buttons_status()
        if self.isClicked:
             self.list_widget = QListWidget(self.frame)
             self.list_widget.setGeometry(65, 60, 60, 20)
             self.list_widget.setStyleSheet("""
                                        QListView {
                                        background-color: rgb(255, 255, 255);
                                        font-size: 12px;
                                        color: black;
                                        border: 1px solid gray;
                                        border-radius: 0px;
                                        
                                        
                                        }
                                        
                                        

                                        """)
             self.list_widget.addItems(["Log out"])
             self.list_widget.clicked.connect(on_item_selected)
             self.list_widget.show()
        else:
             
             self.list_widget.hide()
        
        self.isClicked = not self.isClicked
    def load_csv(self, file_path):
        
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)

            # Set table dimensions
            self.ui.data_table.setWordWrap(True)
            self.ui.data_table.resizeColumnsToContents()
            self.ui.data_table.resizeRowsToContents()
            self.ui.data_table.setRowCount(len(data))
            self.ui.data_table.setColumnCount(len(data[0]))

            # Populate table with data
            for row_idx, row in enumerate(data):
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(value)
                    self.ui.data_table.setItem(row_idx, col_idx, item)

            self.ui.data_table.setHorizontalHeaderLabels(data[0])  # Set first row as headers
            self.ui.data_table.removeRow(0)  # Remove header row from the table body
        except Exception as e:
            print(f"Error loading CSV: {e}")
    def set_valid(self, widget, valid: bool):
        widget.setEnabled(valid)
        if valid:
                widget.setStyleSheet("""
                                                QPushButton:checked
                                                {
                                                        background-color:rgb(50, 50, 50);
                                                        color:white;
                                                }
                                                QPushButton:pressed
                                                {
                                                        background-color:rgb(218, 218, 218);
                                                }
                                                QPushButton{
                                                        background-color:rgb(0, 170, 0);
                                                        font-size:12px;
                                                        color:black;
                                                        font-weight: bold;
                                                        
                                                        border:1px solid gray;
                                                        border-radius: 5px;
                                                }
                                                """)
        else:
                widget.setStyleSheet("""
                                                QPushButton:checked
                                                {
                                                        background-color:rgb(50, 50, 50);
                                                        color:white;
                                                }
                                                QPushButton:pressed
                                                {
                                                        background-color:rgb(218, 218, 218);
                                                }
                                                QPushButton{
                                                        background-color:rgb(218, 218, 218);
                                                        font-size:12px;
                                                        color:black;
                                                        font-weight: bold;
                                                        
                                                        border:1px solid gray;
                                                        border-radius: 5px;
                                                }
                                                """)
    def change_buttons_status(self):
        if self.internet:
            self.ui.internet_status_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Internet: </span><span style=\" color:#00ff00;\">Connected</span></p></body></html>", None))
            if self.isConnected:
                self.ui.status_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span><span style=\" color:#00ff00;\">Connected</span></p></body></html>", None))
                self.ui.status_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span><span style=\" color:#00ff00;\">Connected</span></p></body></html>", None))
                if self.isAdmin:
                     self.ui.permission_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#00ff00;\">Admin</span></p></body></html>", None))
                     self.ui.permission_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#00ff00;\">Admin</span></p></body></html>", None))
                     
                     self.set_valid(self.ui.upload_button, True)
                     self.set_valid(self.ui.download_button, True)
                     self.set_valid(self.ui.crawl_button, True)
                else:
                     self.ui.permission_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#ff0000;\">Not Admin</span></p></body></html>", None))
                     self.ui.permission_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#ff0000;\">Not Admin</span></p></body></html>", None))
                     self.set_valid(self.ui.upload_button, False)
                     self.set_valid(self.ui.download_button, True)
                     self.set_valid(self.ui.crawl_button, False)
            else:
                self.ui.status_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span><span style=\" color:#ff0000;\">Disconnected</span></p></body></html>", None))
                self.ui.status_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span><span style=\" color:#ff0000;\">Disconnected</span></p></body></html>", None))
                self.ui.permission_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#ff0000;\">Not Admin</span></p></body></html>", None))
                self.ui.permission_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#ff0000;\">Not Admin</span></p></body></html>", None))
                self.set_valid(self.ui.upload_button, False)
                self.set_valid(self.ui.download_button, False)
                self.set_valid(self.ui.crawl_button, False)
        else:
            self.ui.internet_status_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Internet: </span><span style=\" color:#ff0000;\">Disconnected</span></p></body></html>", None))
            self.ui.status_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span><span style=\" color:#ff0000;\">Disconnected</span></p></body></html>", None))
            self.ui.status_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span><span style=\" color:#ff0000;\">Disconnected</span></p></body></html>", None))
            self.ui.permission_label.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#ff0000;\">Not Admin</span></p></body></html>", None))
            self.ui.permission_label_2.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Permisson: </span><span style=\" color:#ff0000;\">Not Admin</span></p></body></html>", None))
            self.set_valid(self.ui.upload_button, False)
            self.set_valid(self.ui.download_button, False)
            self.set_valid(self.ui.crawl_button, False)
        
    def download_button_function(self):
        try:
             self.db.download_collection()
             self.ui.download_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#00ff00;\">Download successful</span></p></body></html>", None))
        except Exception as e:
             print(e)
             self.ui.download_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Something wrong</span></p></body></html>", None))
        self.change_buttons_status()
    def upload_button_function(self):
        try:
             self.db.upload_collection()
             self.ui.upload_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#00ff00;\">Upload successful</span></p></body></html>", None))
        except Exception as e:
             print(e)
             self.ui.upload_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Something wrong</span></p></body></html>", None))
        self.change_buttons_status()
    def crawl_button_function(self):
        try:
             
             self.ui.crawl_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ffff00;\">Please wait</span></p></body></html>", None))
             
             
             runpy.run_path(os.path.dirname(os.path.abspath(__file__)) + "\Crawl_data\data_scraping.py")
             self.ui.crawl_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#00ff00;\">Done</span></p></body></html>", None))
        except Exception as e:
             print(e)
             self.ui.crawl_message.setText(QCoreApplication.translate("database_widget", f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Something wrong</span></p></body></html>", None))
    def is_connected(self):
        try:
                # Ping Google's DNS (8.8.8.8)
                response_time = ping("8.8.8.8", timeout=5)
                return response_time is not None
        except Exception:
                return False

   