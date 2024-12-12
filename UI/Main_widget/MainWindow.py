# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledlkmXZY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 746)
        self.Main_layout = QWidget(MainWindow)
        self.Main_layout.setObjectName(u"Main_layout")
        self.verticalLayout_2 = QVBoxLayout(self.Main_layout)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_layout = QFrame(self.Main_layout)
        self.top_layout.setObjectName(u"top_layout")
        self.horizontalLayout = QHBoxLayout(self.top_layout)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.top_layout)
        self.side_bar.setObjectName(u"side_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_bar.sizePolicy().hasHeightForWidth())
        self.side_bar.setSizePolicy(sizePolicy)
        self.side_bar.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 50, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(75, 75, 75, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(62, 62, 62, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(25, 25, 25, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(33, 33, 33, 255))
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
        self.side_bar.setPalette(palette)
        self.side_bar.setAutoFillBackground(True)
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.side_bar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.side_bar)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(40, 40))
        self.logo.setMaximumSize(QSize(55, 55))
        self.logo.setStyleSheet(u"image:url(:/images/images/images/PyDracula.png)")

        self.verticalLayout_5.addWidget(self.logo)

        self.content_buttons_group = QFrame(self.side_bar)
        self.content_buttons_group.setObjectName(u"content_buttons_group")
        self.content_buttons_group.setFrameShape(QFrame.StyledPanel)
        self.content_buttons_group.setFrameShadow(QFrame.Raised)
        self.home_button = QPushButton(self.content_buttons_group)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(0, 0, 281, 61))
        self.home_button.setAutoFillBackground(False)
        self.home_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(149, 149, 149)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(255, 137, 253)\n"
"}\n"
"QPushButton{\n"
"	font-size:16px;\n"
"	color: white;\n"
"	text-align:left;\n"
"	padding-left:20px;\n"
"	border:0\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(50, 50))
        self.home_button.setCheckable(False)
        self.home_button.setChecked(False)
        self.home_button.setAutoExclusive(False)
        self.home_button.setFlat(True)
        self.database_button = QPushButton(self.content_buttons_group)
        self.database_button.setObjectName(u"database_button")
        self.database_button.setGeometry(QRect(0, 60, 281, 61))
        self.database_button.setAutoFillBackground(False)
        self.database_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(149, 149, 149)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(255, 137, 253)\n"
"}\n"
"QPushButton{\n"
"	font-size:16px;\n"
"	color: white;\n"
"	text-align:left;\n"
"	padding-left:22px;\n"
"	border:0\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-arrow-circle-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.database_button.setIcon(icon1)
        self.database_button.setIconSize(QSize(50, 50))
        self.database_button.setCheckable(True)
        self.database_button.setChecked(False)
        self.database_button.setAutoExclusive(True)
        self.database_button.setFlat(True)
        self.graph_button = QPushButton(self.content_buttons_group)
        self.graph_button.setObjectName(u"graph_button")
        self.graph_button.setGeometry(QRect(0, 120, 281, 61))
        self.graph_button.setAutoFillBackground(False)
        self.graph_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(149, 149, 149)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(255, 137, 253)\n"
"}\n"
"QPushButton{\n"
"	font-size:16px;\n"
"	color: white;\n"
"	text-align:left;\n"
"	padding-left:22px;\n"
"	border:0\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.graph_button.setIcon(icon2)
        self.graph_button.setCheckable(True)
        self.graph_button.setAutoExclusive(True)
        self.graph_button.setFlat(True)
        self.predict_button = QPushButton(self.content_buttons_group)
        self.predict_button.setObjectName(u"predict_button")
        self.predict_button.setGeometry(QRect(0, 180, 281, 61))
        self.predict_button.setAutoFillBackground(False)
        self.predict_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(149, 149, 149)\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(255, 137, 253)\n"
"}\n"
"QPushButton{\n"
"	font-size:16px;\n"
"	color: white;\n"
"	text-align:left;\n"
"	padding-left:22px;\n"
"	border:0\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.predict_button.setIcon(icon3)
        self.predict_button.setCheckable(True)
        self.predict_button.setAutoExclusive(True)
        self.predict_button.setFlat(True)

        self.verticalLayout_5.addWidget(self.content_buttons_group)


        self.horizontalLayout.addWidget(self.side_bar)

        self.main_content = QFrame(self.top_layout)
        self.main_content.setObjectName(u"main_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(12)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy2)
        self.main_content.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.main_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.main_content)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 0))
        self.top_bar.setMaximumSize(QSize(16777215, 55))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.top_bar.setPalette(palette1)
        self.top_bar.setAutoFillBackground(True)
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.fill_frame = QFrame(self.top_bar)
        self.fill_frame.setObjectName(u"fill_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fill_frame.sizePolicy().hasHeightForWidth())
        self.fill_frame.setSizePolicy(sizePolicy3)
        self.fill_frame.setFrameShape(QFrame.StyledPanel)
        self.fill_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fill_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout_4.addWidget(self.fill_frame)

        self.horizontalFrame_2 = QFrame(self.top_bar)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy4)
        self.horizontalFrame_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.horizontalFrame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalFrame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setAutoFillBackground(True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalFrame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        palette2 = QPalette()
        self.pushButton_4.setPalette(palette2)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_4.setAutoFillBackground(True)
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout_4.addWidget(self.horizontalFrame_2)


        self.verticalLayout_3.addWidget(self.top_bar)

        self.content_display = QFrame(self.main_content)
        self.content_display.setObjectName(u"content_display")
        self.content_display.setMinimumSize(QSize(0, 0))
        self.content_display.setAutoFillBackground(False)
        self.content_display.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #00c9ff, stop:1 #92fe9d);")

        self.verticalLayout_3.addWidget(self.content_display)


        self.horizontalLayout.addWidget(self.main_content)


        self.verticalLayout_2.addWidget(self.top_layout)

        MainWindow.setCentralWidget(self.Main_layout)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.showMaximized)
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)

        self.database_button.setDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"            Hide/Show", None))
        self.database_button.setText(QCoreApplication.translate("MainWindow", u"            Database", None))
        self.graph_button.setText(QCoreApplication.translate("MainWindow", u"            Graph", None))
        self.predict_button.setText(QCoreApplication.translate("MainWindow", u"            Predict", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

