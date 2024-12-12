from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy, QStyledItemDelegate
from PySide6.QtGui import QIntValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from Main_widget.data_visualization import Visualization
import textwrap
import os
import re
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'displaybeCfOz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_main_board(object):
    def setupUi(self, main_board):
        if not main_board.objectName():
            main_board.setObjectName(u"main_board")
        main_board.resize(1036, 688)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_board.sizePolicy().hasHeightForWidth())
        main_board.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(0, 201, 255, 255))
        gradient.setColorAt(1, QColor(146, 254, 157, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(255, 242, 217, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(127, 114, 90, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(170, 153, 120, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(0, 201, 255, 255))
        gradient1.setColorAt(1, QColor(146, 254, 157, 255))
        brush6 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        gradient2 = QLinearGradient(0, 0, 1, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(0, 201, 255, 255))
        gradient2.setColorAt(1, QColor(146, 254, 157, 255))
        brush7 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(0, 201, 255, 255))
        gradient3.setColorAt(1, QColor(146, 254, 157, 255))
        brush10 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(0, 201, 255, 255))
        gradient4.setColorAt(1, QColor(146, 254, 157, 255))
        brush11 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        gradient5 = QLinearGradient(0, 0, 1, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(0, 201, 255, 255))
        gradient5.setColorAt(1, QColor(146, 254, 157, 255))
        brush12 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        gradient6 = QLinearGradient(0, 0, 1, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(0, 201, 255, 255))
        gradient6.setColorAt(1, QColor(146, 254, 157, 255))
        brush13 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        gradient7 = QLinearGradient(0, 0, 1, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(0, 201, 255, 255))
        gradient7.setColorAt(1, QColor(146, 254, 157, 255))
        brush14 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        gradient8 = QLinearGradient(0, 0, 1, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(0, 201, 255, 255))
        gradient8.setColorAt(1, QColor(146, 254, 157, 255))
        brush15 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush16 = QBrush(QColor(255, 229, 180, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        main_board.setPalette(palette)
        main_board.setAutoFillBackground(False)
        main_board.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #00c9ff, stop:1 #92fe9d);")
        self.horizontalLayout = QHBoxLayout(main_board)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.main_display = QFrame(main_board)
        self.main_display.setObjectName(u"main_display")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_display.sizePolicy().hasHeightForWidth())
        self.main_display.setSizePolicy(sizePolicy1)
        self.main_display.setMinimumSize(QSize(0, 0))
        self.main_display.setAutoFillBackground(False)
        self.main_display.setStyleSheet(u"")
        self.main_display.setFrameShape(QFrame.StyledPanel)
        self.main_display.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_display)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.custom_graph_choose = QFrame(self.main_display)
        self.custom_graph_choose.setObjectName(u"custom_graph_choose")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.custom_graph_choose.sizePolicy().hasHeightForWidth())
        self.custom_graph_choose.setSizePolicy(sizePolicy2)
        self.custom_graph_choose.setMaximumSize(QSize(16777215, 16777215))
        self.custom_graph_choose.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.custom_graph_choose.setFrameShape(QFrame.StyledPanel)
        self.custom_graph_choose.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.custom_graph_choose)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.choose_type_of_graph = QFrame(self.custom_graph_choose)
        self.choose_type_of_graph.setObjectName(u"choose_type_of_graph")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.choose_type_of_graph.sizePolicy().hasHeightForWidth())
        self.choose_type_of_graph.setSizePolicy(sizePolicy3)
        self.choose_type_of_graph.setFrameShape(QFrame.StyledPanel)
        self.choose_type_of_graph.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.choose_type_of_graph)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.label = QLabel(self.choose_type_of_graph)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.graph_box = QComboBox(self.choose_type_of_graph)
        self.graph_box.setObjectName(u"graph_box")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.graph_box.setPalette(palette1)
        self.graph_box.setAutoFillBackground(False)
        self.graph_box.setStyleSheet(u"QComboBox {\n"
"        border: 2px solid black;\n"
"        border-radius: 3px;\n"
"        padding: 3px;\n"
"    }\n"
" QComboBox::drop-down {\n"
"        border-left: 1px solid gray;\n"
"		image: url(:/icons/images/icons/cil-arrow-bottom-2.png);\n"
"		width: 25px; \n"
"    }\n"
"")
        self.graph_box.setFrame(True)

        self.verticalLayout_7.addWidget(self.graph_box)

        self.holder_4 = QFrame(self.choose_type_of_graph)
        self.holder_4.setObjectName(u"holder_4")
        self.holder_4.setFrameShape(QFrame.StyledPanel)
        self.holder_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.holder_4)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 0)
        self.frame_2 = QFrame(self.holder_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.draw_graph_button = QPushButton(self.frame_2)
        self.draw_graph_button.setObjectName(u"draw_graph_button")
        self.draw_graph_button.setGeometry(QRect(0, 0, 51, 31))
        self.draw_graph_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.draw_graph_button.setAutoFillBackground(False)
        self.draw_graph_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px;         /* Rounded corners */\n"
"        padding: 3px;   \n"
"		background-color:rgb(218, 218, 218)\n"
"    }\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(232, 232, 232)\n"
"}")
        self.draw_graph_button.setFlat(False)

        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.holder_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.save_graph_button = QPushButton(self.frame_4)
        self.save_graph_button.setObjectName(u"save_graph_button")
        self.save_graph_button.setGeometry(QRect(0, 0, 51, 31))
        self.save_graph_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_graph_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px;         /* Rounded corners */\n"
"        padding: 3px;   \n"
"		background-color:rgb(218, 218, 218)\n"
"    }\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(232, 232, 232)\n"
"}")

        self.horizontalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_7.addWidget(self.holder_4)


        self.horizontalLayout_3.addWidget(self.choose_type_of_graph)

        self.information_of_graph = QFrame(self.custom_graph_choose)
        self.information_of_graph.setObjectName(u"information_of_graph")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.information_of_graph.sizePolicy().hasHeightForWidth())
        self.information_of_graph.setSizePolicy(sizePolicy4)
        self.information_of_graph.setAutoFillBackground(False)
        self.information_of_graph.setStyleSheet(u"QFrame {\n"
"        border: 1px solid gray; \n"
"        border-radius: 2px;\n"
"    }\n"
"")
        self.information_of_graph.setFrameShape(QFrame.StyledPanel)
        self.information_of_graph.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.information_of_graph)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.information_of_graph)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.holder_2 = QFrame(self.information_of_graph)
        self.holder_2.setObjectName(u"holder_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(4)
        sizePolicy5.setHeightForWidth(self.holder_2.sizePolicy().hasHeightForWidth())
        self.holder_2.setSizePolicy(sizePolicy5)
        self.holder_2.setStyleSheet(u"border: none;")
        self.holder_2.setFrameShape(QFrame.StyledPanel)
        self.holder_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.holder_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.holder_1 = QFrame(self.holder_2)
        self.holder_1.setObjectName(u"holder_1")
        sizePolicy4.setHeightForWidth(self.holder_1.sizePolicy().hasHeightForWidth())
        self.holder_1.setSizePolicy(sizePolicy4)
        self.holder_1.setFrameShape(QFrame.StyledPanel)
        self.holder_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.holder_1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.holder_3 = QFrame(self.holder_1)
        self.holder_3.setObjectName(u"holder_3")
        sizePolicy2.setHeightForWidth(self.holder_3.sizePolicy().hasHeightForWidth())
        self.holder_3.setSizePolicy(sizePolicy2)
        self.holder_3.setFrameShape(QFrame.StyledPanel)
        self.holder_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.holder_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.holder_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.reduce_factor_value = QLineEdit(self.holder_3)
        self.reduce_factor_value.setObjectName(u"reduce_factor_value")
        self.reduce_factor_value.setStyleSheet(u"border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; ")
        self.reduce_factor_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.reduce_factor_value)

        self.label_5 = QLabel(self.holder_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lower_value = QLineEdit(self.holder_3)
        self.lower_value.setObjectName(u"lower_value")
        self.lower_value.setStyleSheet(u"border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; ")
        self.lower_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lower_value)

        self.label_6 = QLabel(self.holder_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.upper_value = QLineEdit(self.holder_3)
        self.upper_value.setObjectName(u"upper_value")
        self.upper_value.setStyleSheet(u"border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; ")
        self.upper_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.upper_value)


        self.verticalLayout_10.addWidget(self.holder_3)

        self.frame_3 = QFrame(self.holder_1)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.country_choose = QComboBox(self.frame_3)
        self.country_choose.setObjectName(u"country_choose")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.country_choose.sizePolicy().hasHeightForWidth())
        self.country_choose.setSizePolicy(sizePolicy6)
        self.country_choose.setStyleSheet(u"QComboBox {\n"
"        border: 1px solid gray; \n"
"        border-radius: 3px;   \n"
"        padding: 3px;  \n"
"    }\n"
"QComboBox::drop-down {\n"
"        border-left: 1px solid gray;\n"
"		image: url(:/icons/images/icons/cil-arrow-bottom-2.png);\n"
"		width: 25px; \n"
"    }")
        self.country_choose.setFrame(True)

        self.horizontalLayout_6.addWidget(self.country_choose)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy7)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.clolumn_box_1 = QComboBox(self.frame_3)
        self.clolumn_box_1.setObjectName(u"clolumn_box_1")
        sizePolicy6.setHeightForWidth(self.clolumn_box_1.sizePolicy().hasHeightForWidth())
        self.clolumn_box_1.setSizePolicy(sizePolicy6)
        self.clolumn_box_1.setCursor(QCursor(Qt.ArrowCursor))
        self.clolumn_box_1.setContextMenuPolicy(Qt.PreventContextMenu)
        self.clolumn_box_1.setStyleSheet(u"QComboBox {\n"
"        border: 1px solid gray; \n"
"        border-radius: 3px;   \n"
"        padding: 3px;  \n"
"    }\n"
"QComboBox::drop-down {\n"
"        border-left: 1px solid gray;\n"
"		image: url(:/icons/images/icons/cil-arrow-bottom-2.png);\n"
"		width: 25px; \n"
"    }")
        self.clolumn_box_1.setFrame(True)

        self.horizontalLayout_6.addWidget(self.clolumn_box_1)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy7.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy7)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.clolumn_box_2 = QComboBox(self.frame_3)
        self.clolumn_box_2.setObjectName(u"clolumn_box_2")
        sizePolicy6.setHeightForWidth(self.clolumn_box_2.sizePolicy().hasHeightForWidth())
        self.clolumn_box_2.setSizePolicy(sizePolicy6)
        self.clolumn_box_2.setCursor(QCursor(Qt.ArrowCursor))
        self.clolumn_box_2.setContextMenuPolicy(Qt.PreventContextMenu)
        self.clolumn_box_2.setStyleSheet(u"QComboBox {\n"
"        border: 1px solid gray; \n"
"        border-radius: 3px;   \n"
"        padding: 3px;  \n"
"    }\n"
"QComboBox::drop-down {\n"
"        border-left: 1px solid gray;\n"
"		image: url(:/icons/images/icons/cil-arrow-bottom-2.png);\n"
"		width: 25px; \n"
"    }")
        self.clolumn_box_2.setFrame(True)

        self.horizontalLayout_6.addWidget(self.clolumn_box_2)

        self.regression_box = QCheckBox(self.frame_3)
        self.regression_box.setObjectName(u"regression_box")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.regression_box.sizePolicy().hasHeightForWidth())
        self.regression_box.setSizePolicy(sizePolicy8)
        self.regression_box.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_6.addWidget(self.regression_box)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.holder_1)


        self.verticalLayout_8.addWidget(self.holder_2)


        self.horizontalLayout_3.addWidget(self.information_of_graph)


        self.verticalLayout.addWidget(self.custom_graph_choose)

        self.graph_display = QFrame(self.main_display)
        self.graph_display.setObjectName(u"graph_display")
        sizePolicy5.setHeightForWidth(self.graph_display.sizePolicy().hasHeightForWidth())
        self.graph_display.setSizePolicy(sizePolicy5)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.graph_display.setPalette(palette2)
        self.graph_display.setAutoFillBackground(False)
        self.graph_display.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.graph_display.setFrameShape(QFrame.StyledPanel)
        self.graph_display.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.graph_display)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.graph_display)


        self.horizontalLayout.addWidget(self.main_display)

        self.right_bar = QFrame(main_board)
        self.right_bar.setObjectName(u"right_bar")
        sizePolicy3.setHeightForWidth(self.right_bar.sizePolicy().hasHeightForWidth())
        self.right_bar.setSizePolicy(sizePolicy3)
        self.right_bar.setMinimumSize(QSize(0, 0))
        self.right_bar.setMaximumSize(QSize(16777215, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        gradient9 = QLinearGradient(0, 0, 1, 1)
        gradient9.setSpread(QGradient.PadSpread)
        gradient9.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(0, 201, 255, 255))
        gradient9.setColorAt(1, QColor(146, 254, 157, 255))
        brush17 = QBrush(gradient9)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush17)
        brush18 = QBrush(QColor(70, 118, 118, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush18)
        brush19 = QBrush(QColor(58, 98, 98, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        brush20 = QBrush(QColor(23, 39, 39, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush20)
        brush21 = QBrush(QColor(31, 53, 53, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        gradient10 = QLinearGradient(0, 0, 1, 1)
        gradient10.setSpread(QGradient.PadSpread)
        gradient10.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(0, 201, 255, 255))
        gradient10.setColorAt(1, QColor(146, 254, 157, 255))
        brush22 = QBrush(gradient10)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush22)
        gradient11 = QLinearGradient(0, 0, 1, 1)
        gradient11.setSpread(QGradient.PadSpread)
        gradient11.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(0, 201, 255, 255))
        gradient11.setColorAt(1, QColor(146, 254, 157, 255))
        brush23 = QBrush(gradient11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush20)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush24 = QBrush(QColor(255, 255, 255, 128))
        brush24.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        gradient12 = QLinearGradient(0, 0, 1, 1)
        gradient12.setSpread(QGradient.PadSpread)
        gradient12.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(0, 201, 255, 255))
        gradient12.setColorAt(1, QColor(146, 254, 157, 255))
        brush25 = QBrush(gradient12)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush25)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        gradient13 = QLinearGradient(0, 0, 1, 1)
        gradient13.setSpread(QGradient.PadSpread)
        gradient13.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(0, 201, 255, 255))
        gradient13.setColorAt(1, QColor(146, 254, 157, 255))
        brush26 = QBrush(gradient13)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush26)
        gradient14 = QLinearGradient(0, 0, 1, 1)
        gradient14.setSpread(QGradient.PadSpread)
        gradient14.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(0, 201, 255, 255))
        gradient14.setColorAt(1, QColor(146, 254, 157, 255))
        brush27 = QBrush(gradient14)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush20)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        gradient15 = QLinearGradient(0, 0, 1, 1)
        gradient15.setSpread(QGradient.PadSpread)
        gradient15.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient15.setColorAt(0, QColor(0, 201, 255, 255))
        gradient15.setColorAt(1, QColor(146, 254, 157, 255))
        brush28 = QBrush(gradient15)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush28)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        gradient16 = QLinearGradient(0, 0, 1, 1)
        gradient16.setSpread(QGradient.PadSpread)
        gradient16.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient16.setColorAt(0, QColor(0, 201, 255, 255))
        gradient16.setColorAt(1, QColor(146, 254, 157, 255))
        brush29 = QBrush(gradient16)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush29)
        gradient17 = QLinearGradient(0, 0, 1, 1)
        gradient17.setSpread(QGradient.PadSpread)
        gradient17.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient17.setColorAt(0, QColor(0, 201, 255, 255))
        gradient17.setColorAt(1, QColor(146, 254, 157, 255))
        brush30 = QBrush(gradient17)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush30)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush31 = QBrush(QColor(47, 79, 79, 255))
        brush31.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush31)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.right_bar.setPalette(palette3)
        self.right_bar.setAutoFillBackground(False)
        self.right_bar.setStyleSheet(u"")
        self.right_bar.setFrameShape(QFrame.StyledPanel)
        self.right_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.file_choose = QFrame(self.right_bar)
        self.file_choose.setObjectName(u"file_choose")
        self.file_choose.setAutoFillBackground(False)
        self.file_choose.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.file_choose.setFrameShape(QFrame.StyledPanel)
        self.file_choose.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.file_choose)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(7, 7, 7, 7)
        self.label_8 = QLabel(self.file_choose)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 50))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.data_file_choose = QFrame(self.file_choose)
        self.data_file_choose.setObjectName(u"data_file_choose")
        sizePolicy2.setHeightForWidth(self.data_file_choose.sizePolicy().hasHeightForWidth())
        self.data_file_choose.setSizePolicy(sizePolicy2)
        self.data_file_choose.setCursor(QCursor(Qt.UpArrowCursor))
        self.data_file_choose.setFrameShape(QFrame.StyledPanel)
        self.data_file_choose.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.data_file_choose)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.all_frame = QFrame(self.data_file_choose)
        self.all_frame.setObjectName(u"all_frame")
        self.all_frame.setFrameShape(QFrame.StyledPanel)
        self.all_frame.setFrameShadow(QFrame.Raised)
        self.all_button = QPushButton(self.all_frame)
        self.all_button.setObjectName(u"all_button")
        self.all_button.setGeometry(QRect(10, 0, 93, 28))
        self.all_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.all_button.setAutoFillBackground(False)
        self.all_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.all_button.setCheckable(True)
        self.all_button.setChecked(True)
        self.all_button.setAutoExclusive(False)
        self.all_button.setFlat(False)

        self.gridLayout.addWidget(self.all_frame, 0, 0, 1, 1)

        self.male_ratio_frame = QFrame(self.data_file_choose)
        self.male_ratio_frame.setObjectName(u"male_ratio_frame")
        self.male_ratio_frame.setFrameShape(QFrame.StyledPanel)
        self.male_ratio_frame.setFrameShadow(QFrame.Raised)
        self.male_ratio_button = QPushButton(self.male_ratio_frame)
        self.male_ratio_button.setObjectName(u"male_ratio_button")
        self.male_ratio_button.setGeometry(QRect(10, 0, 93, 28))
        self.male_ratio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.male_ratio_button.setAutoFillBackground(False)
        self.male_ratio_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.male_ratio_button.setCheckable(True)
        self.male_ratio_button.setChecked(False)
        self.male_ratio_button.setAutoExclusive(False)
        self.male_ratio_button.setFlat(True)

        self.gridLayout.addWidget(self.male_ratio_frame, 0, 1, 1, 1)

        self.GDP_per_capita_frame = QFrame(self.data_file_choose)
        self.GDP_per_capita_frame.setObjectName(u"GDP_per_capita_frame")
        self.GDP_per_capita_frame.setFrameShape(QFrame.StyledPanel)
        self.GDP_per_capita_frame.setFrameShadow(QFrame.Raised)
        self.GDP_per_capita_button = QPushButton(self.GDP_per_capita_frame)
        self.GDP_per_capita_button.setObjectName(u"GDP_per_capita_button")
        self.GDP_per_capita_button.setGeometry(QRect(0, 0, 111, 28))
        self.GDP_per_capita_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.GDP_per_capita_button.setAutoFillBackground(False)
        self.GDP_per_capita_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.GDP_per_capita_button.setCheckable(True)
        self.GDP_per_capita_button.setChecked(False)
        self.GDP_per_capita_button.setAutoExclusive(False)
        self.GDP_per_capita_button.setFlat(True)

        self.gridLayout.addWidget(self.GDP_per_capita_frame, 1, 0, 1, 1)

        self.frame = QFrame(self.data_file_choose)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.population_button = QPushButton(self.frame)
        self.population_button.setObjectName(u"population_button")
        self.population_button.setGeometry(QRect(10, 0, 91, 28))
        self.population_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.population_button.setAutoFillBackground(False)
        self.population_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.population_button.setCheckable(True)
        self.population_button.setChecked(False)
        self.population_button.setAutoExclusive(True)
        self.population_button.setFlat(True)

        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.life_expectancy_frame = QFrame(self.data_file_choose)
        self.life_expectancy_frame.setObjectName(u"life_expectancy_frame")
        sizePolicy.setHeightForWidth(self.life_expectancy_frame.sizePolicy().hasHeightForWidth())
        self.life_expectancy_frame.setSizePolicy(sizePolicy)
        self.life_expectancy_frame.setFrameShape(QFrame.StyledPanel)
        self.life_expectancy_frame.setFrameShadow(QFrame.Raised)
        self.life_expectancy_button = QPushButton(self.life_expectancy_frame)
        self.life_expectancy_button.setObjectName(u"life_expectancy_button")
        self.life_expectancy_button.setGeometry(QRect(0, 0, 111, 28))
        self.life_expectancy_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.life_expectancy_button.setAutoFillBackground(False)
        self.life_expectancy_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.life_expectancy_button.setCheckable(True)
        self.life_expectancy_button.setChecked(False)
        self.life_expectancy_button.setAutoExclusive(False)
        self.life_expectancy_button.setFlat(True)

        self.gridLayout.addWidget(self.life_expectancy_frame, 2, 0, 1, 1)

        self.BMI_frame = QFrame(self.data_file_choose)
        self.BMI_frame.setObjectName(u"BMI_frame")
        sizePolicy.setHeightForWidth(self.BMI_frame.sizePolicy().hasHeightForWidth())
        self.BMI_frame.setSizePolicy(sizePolicy)
        self.BMI_frame.setFrameShape(QFrame.StyledPanel)
        self.BMI_frame.setFrameShadow(QFrame.Raised)
        self.BMI_button = QPushButton(self.BMI_frame)
        self.BMI_button.setObjectName(u"BMI_button")
        self.BMI_button.setGeometry(QRect(30, 0, 51, 28))
        self.BMI_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.BMI_button.setAutoFillBackground(False)
        self.BMI_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.BMI_button.setCheckable(True)
        self.BMI_button.setChecked(False)
        self.BMI_button.setAutoExclusive(False)
        self.BMI_button.setFlat(True)

        self.gridLayout.addWidget(self.BMI_frame, 2, 1, 1, 1)

        self.retirement_ratio_frame = QFrame(self.data_file_choose)
        self.retirement_ratio_frame.setObjectName(u"retirement_ratio_frame")
        self.retirement_ratio_frame.setFrameShape(QFrame.StyledPanel)
        self.retirement_ratio_frame.setFrameShadow(QFrame.Raised)
        self.retirement_ratio_button = QPushButton(self.retirement_ratio_frame)
        self.retirement_ratio_button.setObjectName(u"retirement_ratio_button")
        self.retirement_ratio_button.setGeometry(QRect(10, 0, 211, 28))
        self.retirement_ratio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.retirement_ratio_button.setAutoFillBackground(False)
        self.retirement_ratio_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.retirement_ratio_button.setCheckable(True)
        self.retirement_ratio_button.setChecked(False)
        self.retirement_ratio_button.setAutoExclusive(False)
        self.retirement_ratio_button.setFlat(True)

        self.gridLayout.addWidget(self.retirement_ratio_frame, 3, 0, 1, 2)

        self.young_ratio_frame = QFrame(self.data_file_choose)
        self.young_ratio_frame.setObjectName(u"young_ratio_frame")
        self.young_ratio_frame.setFrameShape(QFrame.StyledPanel)
        self.young_ratio_frame.setFrameShadow(QFrame.Raised)
        self.young_ratio_button = QPushButton(self.young_ratio_frame)
        self.young_ratio_button.setObjectName(u"young_ratio_button")
        self.young_ratio_button.setGeometry(QRect(10, 0, 211, 28))
        self.young_ratio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.young_ratio_button.setAutoFillBackground(False)
        self.young_ratio_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(188, 188, 188);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        self.young_ratio_button.setCheckable(True)
        self.young_ratio_button.setChecked(False)
        self.young_ratio_button.setAutoExclusive(False)
        self.young_ratio_button.setFlat(True)

        self.gridLayout.addWidget(self.young_ratio_frame, 4, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.data_file_choose)

        self.data_choose = QFrame(self.file_choose)
        self.data_choose.setObjectName(u"data_choose")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(2)
        sizePolicy9.setHeightForWidth(self.data_choose.sizePolicy().hasHeightForWidth())
        self.data_choose.setSizePolicy(sizePolicy9)
        self.data_choose.setFrameShape(QFrame.StyledPanel)
        self.data_choose.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.data_choose)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search_bar_frame = QFrame(self.data_choose)
        self.search_bar_frame.setObjectName(u"search_bar_frame")
        sizePolicy2.setHeightForWidth(self.search_bar_frame.sizePolicy().hasHeightForWidth())
        self.search_bar_frame.setSizePolicy(sizePolicy2)
        self.search_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.search_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.search_bar_frame)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.search_button = QPushButton(self.search_bar_frame)
        self.search_button.setObjectName(u"search_button")
        sizePolicy3.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy3)
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_button.setStyleSheet(u"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(232, 232, 232)\n"
"}\n"
"QPushButton{\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"	\n"
"	border:0\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.search_button)

        self.search_text = QLineEdit(self.search_bar_frame)
        self.search_text.setObjectName(u"search_text")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(5)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.search_text.sizePolicy().hasHeightForWidth())
        self.search_text.setSizePolicy(sizePolicy10)
        self.search_text.setStyleSheet(u"QLineEdit {\n"
"        border: none;\n"
"        border-bottom: 1px solid rgb(50, 50, 50);\n"
"		border-radius: 0px;\n"
"    }")

        self.horizontalLayout_2.addWidget(self.search_text)


        self.verticalLayout_5.addWidget(self.search_bar_frame)

        self.graph_choose = QFrame(self.data_choose)
        self.graph_choose.setObjectName(u"graph_choose")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(7)
        sizePolicy11.setHeightForWidth(self.graph_choose.sizePolicy().hasHeightForWidth())
        self.graph_choose.setSizePolicy(sizePolicy11)
        self.graph_choose.setFrameShape(QFrame.StyledPanel)
        self.graph_choose.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.graph_choose)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.graph_choose)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 226, 340))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.graph_choose)


        self.verticalLayout_4.addWidget(self.data_choose)


        self.verticalLayout_2.addWidget(self.file_choose)


        self.horizontalLayout.addWidget(self.right_bar)


        self.retranslateUi(main_board)

        self.draw_graph_button.setDefault(False)


        QMetaObject.connectSlotsByName(main_board)
    # setupUi

    def retranslateUi(self, main_board):
        main_board.setWindowTitle(QCoreApplication.translate("main_board", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_board", u"<html><head/><body><p><span style=\" font-weight:600;\">Type of graph</span></p></body></html>", None))
        self.draw_graph_button.setText(QCoreApplication.translate("main_board", u"Draw", None))
        self.save_graph_button.setText(QCoreApplication.translate("main_board", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("main_board", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Information of the custom graph</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("main_board", u"Reduce factor", None))
        self.label_5.setText(QCoreApplication.translate("main_board", u"Lower percentile", None))
        self.label_6.setText(QCoreApplication.translate("main_board", u"Upper percentile", None))
        self.label_7.setText(QCoreApplication.translate("main_board", u"Country", None))
        self.label_3.setText(QCoreApplication.translate("main_board", u"Column 1", None))
        self.label_9.setText(QCoreApplication.translate("main_board", u"Column 2", None))
        self.regression_box.setText(QCoreApplication.translate("main_board", u" Regression", None))
        self.label_8.setText(QCoreApplication.translate("main_board", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Saved graphs</span></p></body></html>", None))
        self.all_button.setText(QCoreApplication.translate("main_board", u"All", None))
        self.male_ratio_button.setText(QCoreApplication.translate("main_board", u"Male ratio", None))
        self.GDP_per_capita_button.setText(QCoreApplication.translate("main_board", u"GDP per capita", None))
        self.population_button.setText(QCoreApplication.translate("main_board", u"Population", None))
        self.life_expectancy_button.setText(QCoreApplication.translate("main_board", u"Life expectancy", None))
        self.BMI_button.setText(QCoreApplication.translate("main_board", u"BMI", None))
        self.retirement_ratio_button.setText(QCoreApplication.translate("main_board", u"Retirement age dependency ratio", None))
        self.young_ratio_button.setText(QCoreApplication.translate("main_board", u"Young age dependency ratio", None))
        self.search_button.setText("")
    # retranslateUi







#IMPORTANT
class Graph_widget(QWidget):
    def __init__(self, parent=None):
        super(Graph_widget, self).__init__(parent)
        #Load all graph
        self.data = self.load_graph()
        self.graph_list = self.data.get_graph()
        self.columns = self.data.get_columns()
        self.countries = self.data.get_rows("Country")
        # Create an instance of the generated UI class
        self.ui = Ui_main_board()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Set up the UI by calling setupUi and passing this widget (QWidget)
        self.ui.setupUi(self)
        self.button_group = QButtonGroup()
         # Make them auto-exclusive
        self.button_group.addButton(self.ui.all_button)
        self.button_group.addButton(self.ui.male_ratio_button)
        self.button_group.addButton(self.ui.GDP_per_capita_button)
        self.button_group.addButton(self.ui.population_button)
        self.button_group.addButton(self.ui.life_expectancy_button)
        self.button_group.addButton(self.ui.BMI_button)
        self.button_group.addButton(self.ui.retirement_ratio_button)
        self.button_group.addButton(self.ui.young_ratio_button)
        self.button_group.setExclusive(True) 
        
        # Set up layout for graph display
        if self.ui.graph_display.layout() is None:
            
            layout = QVBoxLayout(self.ui.graph_display)
            self.ui.graph_display.setLayout(layout)
        else:
            layout = self.ui.graph_display.layout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.layout = layout
        # Add signals
        
        self.buttons_list = {save_location: [] for save_location in self.graph_list.keys()}
        for save_location, name_list in self.graph_list.items():
            for name in name_list:
                real_name = name.split("_")[0] + "\n" + name.split("_")[3] + " - " +name.split("_")[4]
                
                wrapped_title = textwrap.fill(real_name, width=30)
                button = QPushButton(wrapped_title, self)
                def handle_button_click(sl=save_location, n=name):
                        self.click_button(sl, n, layout)
                
                # Connect the inner function to the button's clicked signal
                button.clicked.connect(handle_button_click)
                button.setCursor(Qt.PointingHandCursor)
                self.buttons_list[save_location].append(button)
        
        # Add the initialcanvas to the layout
        
        layout.addWidget(self.image_label)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        self.content_layout = content_layout
        # Add different options as buttons or labels
        self.button_group_1 = QButtonGroup()
        for save, buttons in self.buttons_list.items():
            for button in buttons:
                button.setStyleSheet("""
                                        QPushButton {
                                        
                                        background-color: rgb(188, 188, 188);
                                        font-size: 12px;
                                        color: black;
                                        font-weight: bold;
                                        border: 0;
                                        padding: 2px;  /* Ensures padding within button */
                                        }

                                        QPushButton:checked {
                                        background-color: rgb(50, 50, 50);
                                        color: white;
                                        }

                                        QPushButton:pressed {
                                        background-color: rgb(218, 218, 218);
                                        color: black;
                                        }
                                        """)
                button.setCheckable(True)
                self.button_group_1.addButton(button)
                button.setMinimumHeight(50)
                content_layout.addWidget(button)
        self.button_group_1.setExclusive(True)
        # Connect signals
        self.ui.all_button.clicked.connect(lambda: self.reload_button(content_layout, ["Population", "BMI", "GDP_per_Capita", "Life Expectancy", "Retirement Age Dependency Ratio", "Male Ratio", "Young ratio", "Infant mortality per 1000 live births", "Urban Population Ratio", "Population Growth (%)"]))
        self.ui.GDP_per_capita_button.clicked.connect(lambda: self.reload_button(content_layout, ["GDP_per_Capita"]))
        self.ui.BMI_button.clicked.connect(lambda: self.reload_button(content_layout, ["BMI"]))
        self.ui.population_button.clicked.connect(lambda: self.reload_button(content_layout, ["Population"]))
        self.ui.retirement_ratio_button.clicked.connect(lambda: self.reload_button(content_layout, ["Retirement Age Dependency Ratio"]))
        self.ui.male_ratio_button.clicked.connect(lambda: self.reload_button(content_layout, ["Male Ratio"]))
        self.ui.life_expectancy_button.clicked.connect(lambda: self.reload_button(content_layout, ["Life Expectancy"]))
        self.ui.young_ratio_button.clicked.connect(lambda: self.reload_button(content_layout, ["Young ratio"]))

        # Set the content widget to scroll area
        content_widget.setLayout(content_layout)
        self.ui.scrollArea.setWidget(content_widget)
        # Set up top bar
        self.types_of_graph = ["Scatter"]
        for type in self.types_of_graph:
            
                self.ui.graph_box.addItem(type)

        for column in self.columns:
            if column not in ['Country','SDG Region', 'Urban Population Ratio', 'Urban Population Ratio']:
                self.ui.clolumn_box_1.addItem(column)
        self.ui.clolumn_box_1.setFixedWidth(130)

        drop_down_width = 250

        self.ui.clolumn_box_1.view().setFixedWidth(drop_down_width)

        for column in ["Life Expectancy", "Population Growth (%)"]:
            if column not in ['Country','SDG Region']:
                self.ui.clolumn_box_2.addItem(column)
        self.ui.clolumn_box_2.setFixedWidth(130)
        
        self.ui.clolumn_box_2.view().setFixedWidth(drop_down_width)
        self.ui.country_choose.addItem("None")
        for country in self.countries:
            
                self.ui.country_choose.addItem(country)
        self.ui.country_choose.setFixedWidth(100)
        self.ui.country_choose.view().setFixedWidth(drop_down_width)

        self.ui.reduce_factor_value.setValidator(QIntValidator())
        self.ui.lower_value.setValidator(QIntValidator())
        self.ui.upper_value.setValidator(QIntValidator())
        # Draw and save button
        self.ui.draw_graph_button.clicked.connect(self.check_and_draw_graph)
        self.ui.save_graph_button.clicked.connect(self.save_graph)
        # Search
        self.ui.search_button.clicked.connect(lambda: self.search(self.ui.search_text.text(), content_layout))



    def load_graph(self):
        
        return Visualization()
    def click_button(self, save_location, name, layout):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        file_path = script_dir + f"\Graph\{save_location}\{name}"
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
    def reload_button(self, layout, locations):
        self.remove_all_widgets(layout)
        for loc in locations:
            for button in self.buttons_list[loc]:

                layout.addWidget(button)
                button.show()
        layout.update()
    def remove_all_widgets(self, layout):
        for i in range(layout.count()):
                
                item = layout.itemAt(i)
                widget = item.widget()
                widget.hide()
    def check_and_draw_graph(self):
        
        valid_value_range = [[0, 100],[0, 100],[0, 100]]
        error = []
        save_location= "Population"
        if int(self.ui.reduce_factor_value.text()) > valid_value_range[0][1] or int(self.ui.reduce_factor_value.text()) < valid_value_range[0][0]:
             error.append(self.ui.reduce_factor_value)
        if int(self.ui.lower_value.text()) > valid_value_range[1][1] or int(self.ui.lower_value.text()) < valid_value_range[1][0]:
             error.append(self.ui.lower_value)
        if int(self.ui.upper_value.text()) > valid_value_range[2][1] or int(self.ui.upper_value.text()) < valid_value_range[2][0]:
             error.append(self.ui.upper_value)
        if int(self.ui.lower_value.text()) >= int(self.ui.upper_value.text()):
             error.append(self.ui.upper_value)
             error.append(self.ui.lower_value)
        if tuple(error) == ():
             for line in [self.ui.reduce_factor_value, self.ui.lower_value, self.ui.upper_value]:
                line.setStyleSheet("""
                                QLineEdit{
                                background-color:rgb(255, 255, 255);
                                border: 1px solid gray;  /* Border color */
                                border-radius: 3px; 
                                }""")
             country = self.ui.country_choose.currentText()
             if country == "None":
                country = None
             name, buf= self.data.plot_scatter(self.ui.clolumn_box_1.currentText(), col_y = self.ui.clolumn_box_2.currentText(), country = country,reduce_factor = int(self.ui.reduce_factor_value.text()), lower_percentile=int(self.ui.lower_value.text())/100,upper_percentile=int(self.ui.upper_value.text())/100,regression=self.ui.regression_box.isChecked(),save_location= save_location, plot_only = True)
             pixmap = QPixmap()
             pixmap.loadFromData(buf.getvalue())
             scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
             self.image_label.setPixmap(scaled_pixmap)
        else:
             for line in [self.ui.reduce_factor_value, self.ui.lower_value, self.ui.upper_value]:
                if line in error:
                        line.setStyleSheet("""
                                QLineEdit{
                                background-color:rgb(255, 255, 255);
                                border: 1px solid red;  /* Border color */
                                border-radius: 3px; 
                                }""")
                else:
                        line.setStyleSheet("""
                                QLineEdit{
                                background-color:rgb(255, 255, 255);
                                border: 1px solid gray;  /* Border color */
                                border-radius: 3px; 
                                }""")

    def save_graph(self):
        valid_value_range = [[0, 100],[0, 100],[0, 100]]
        error = []
        save_location= self.ui.clolumn_box_1.currentText()
        if int(self.ui.reduce_factor_value.text()) > valid_value_range[0][1] or int(self.ui.reduce_factor_value.text()) < valid_value_range[0][0]:
             error.append(self.ui.reduce_factor_value)
        if int(self.ui.lower_value.text()) > valid_value_range[1][1] or int(self.ui.lower_value.text()) < valid_value_range[1][0]:
             error.append(self.ui.lower_value)
        if int(self.ui.upper_value.text()) > valid_value_range[2][1] or int(self.ui.upper_value.text()) < valid_value_range[2][0]:
             error.append(self.ui.upper_value)
        if int(self.ui.lower_value.text()) >= int(self.ui.upper_value.text()):
             error.append(self.ui.upper_value)
             error.append(self.ui.lower_value)
        if error == []:
             country = self.ui.country_choose.currentText()
             if country == "None":
                country = None
             name = self.data.plot_scatter(self.ui.clolumn_box_1.currentText(), col_y = self.ui.clolumn_box_2.currentText(),country = country,reduce_factor = int(self.ui.reduce_factor_value.text()), lower_percentile=int(self.ui.lower_value.text())/100,upper_percentile=int(self.ui.upper_value.text())/100,regression=self.ui.regression_box.isChecked(),save_location= save_location)
             # Update button
             real_name = name.split("_")[0] + "\n" + name.split("_")[3] + " - " +name.split("_")[4]
                
             wrapped_title = textwrap.fill(real_name, width=30)
             button = QPushButton(wrapped_title, self)
             def handle_button_click(sl=save_location, n=name):
                        self.click_button(sl, n, self.layout)
                
             button.clicked.connect(handle_button_click)
             button.setStyleSheet("""
                                        QPushButton {
                                        background-color: rgb(188, 188, 188);
                                        font-size: 12px;
                                        color: black;
                                        font-weight: bold;
                                        border: 0;
                                        padding: 2px;  /* Ensures padding within button */
                                        }

                                        QPushButton:checked {
                                        background-color: rgb(50, 50, 50);
                                        color: white;
                                        }

                                        QPushButton:pressed {
                                        background-color: rgb(218, 218, 218);
                                        color: black;
                                        }
                                        """)
             button.setCheckable(True)
             self.button_group_1.addButton(button)
             button.setMinimumHeight(50)
             self.content_layout.addWidget(button)
             self.button_group_1.setExclusive(True)
             self.buttons_list[save_location].append(button)
        else:
             for line in error:
                line.setStyleSheet("""
                                QLineEdit{
                                background-color:rgb(255, 255, 255);
                                border: 1px solid red;  /* Border color */
                                border-radius: 3px; 
                                }""")
    def search(self, keyword, layout):

        self.remove_all_widgets(layout)

        keys = re.split(r'[ \n]', keyword)
        
        pool = []
        for l in list(self.buttons_list.values()):
             for i in l:
                pool.append(i)
        real_pool = {}
        
        for button in pool:
             real_pool[button.text()] = button
        for name in real_pool.keys():
             add = True
             character = name.split(" ")
             for key in keys:
                  if key not in character:
                       add = False
             if add:
                  b = real_pool[name]
                  layout.addWidget(b)
                  b.show()
        layout.update()

                       
        




        
