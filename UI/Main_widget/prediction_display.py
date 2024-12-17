from Main_widget.data_visualization import Visualization
from Main_widget.Predict_engine.infer_life_expectancy import Predict
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os
import pandas as pd
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predictylLrRh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1011, 612)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(111, 66, 193, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(169, 122, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(140, 94, 224, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(55, 33, 96, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(74, 44, 129, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(183, 160, 224, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
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
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        Form.setPalette(palette)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.left_frame = QFrame(Form)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy)
        self.left_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border:1px solid black;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.year_combobox = QComboBox(self.frame_3)
        self.year_combobox.setObjectName(u"year_combobox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.year_combobox.sizePolicy().hasHeightForWidth())
        self.year_combobox.setSizePolicy(sizePolicy2)
        self.year_combobox.setCursor(QCursor(Qt.ArrowCursor))
        self.year_combobox.setContextMenuPolicy(Qt.PreventContextMenu)
        self.year_combobox.setStyleSheet(u"QComboBox {\n"
"		background-color:rgb(255, 255, 255);\n"
"        border: 1px solid gray; \n"
"        border-radius: 3px;   \n"
"        padding: 3px;  \n"
"    }\n"
"QComboBox::drop-down {\n"
"        border-left: 1px solid gray;\n"
"		image: url(:/icons/images/icons/cil-arrow-bottom-2.png);\n"
"		width: 25px; \n"
"    }")
        self.year_combobox.setFrame(True)

        self.gridLayout_2.addWidget(self.year_combobox, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(100, 16777215))
        self.label_13.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border:0\n"
"}")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border:0\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.worldmap_display = QFrame(self.left_frame)
        self.worldmap_display.setObjectName(u"worldmap_display")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(6)
        sizePolicy3.setHeightForWidth(self.worldmap_display.sizePolicy().hasHeightForWidth())
        self.worldmap_display.setSizePolicy(sizePolicy3)
        self.worldmap_display.setFrameShape(QFrame.StyledPanel)
        self.worldmap_display.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.worldmap_display)


        self.horizontalLayout.addWidget(self.left_frame)

        self.right_frame = QFrame(Form)
        self.right_frame.setObjectName(u"right_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.right_frame.sizePolicy().hasHeightForWidth())
        self.right_frame.setSizePolicy(sizePolicy4)
        self.right_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.right_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, -1, 7)
        self.frame = QFrame(self.right_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.age_predict_button = QPushButton(self.frame)
        self.age_predict_button.setObjectName(u"age_predict_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.age_predict_button.sizePolicy().hasHeightForWidth())
        self.age_predict_button.setSizePolicy(sizePolicy5)
        self.age_predict_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.age_predict_button.setAutoFillBackground(False)
        self.age_predict_button.setStyleSheet(u"QPushButton:checked\n"
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
"	border-bottom-left-radius: 10px; \n"
"	border-top-left-radius: 10px; \n"
"	border:0\n"
"}")
        self.age_predict_button.setCheckable(True)
        self.age_predict_button.setChecked(True)
        self.age_predict_button.setAutoExclusive(True)
        self.age_predict_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.age_predict_button)

        self.population_growth_button = QPushButton(self.frame)
        self.population_growth_button.setObjectName(u"population_growth_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.population_growth_button.sizePolicy().hasHeightForWidth())
        self.population_growth_button.setSizePolicy(sizePolicy6)
        self.population_growth_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.population_growth_button.setAutoFillBackground(False)
        self.population_growth_button.setStyleSheet(u"QPushButton:checked\n"
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
"	border-bottom-right-radius: 10px; \n"
"	border-top-right-radius: 10px;\n"
"	border:0\n"
"}")
        self.population_growth_button.setCheckable(True)
        self.population_growth_button.setChecked(False)
        self.population_growth_button.setAutoExclusive(True)
        self.population_growth_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.population_growth_button)


        self.verticalLayout.addWidget(self.frame)

        self.input_frame = QFrame(self.right_frame)
        self.input_frame.setObjectName(u"input_frame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(10)
        sizePolicy7.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())
        self.input_frame.setSizePolicy(sizePolicy7)
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.input_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.retirement_line = QLineEdit(self.input_frame)
        self.retirement_line.setObjectName(u"retirement_line")
        self.retirement_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.retirement_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.retirement_line, 7, 1, 1, 1)

        self.label_11 = QLabel(self.input_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.label_5 = QLabel(self.input_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.gdp_line = QLineEdit(self.input_frame)
        self.gdp_line.setObjectName(u"gdp_line")
        self.gdp_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.gdp_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gdp_line, 3, 1, 1, 1)

        self.mortality_line = QLineEdit(self.input_frame)
        self.mortality_line.setObjectName(u"mortality_line")
        self.mortality_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.mortality_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mortality_line, 10, 1, 1, 1)

        self.label_9 = QLabel(self.input_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.young_ratio_line = QLineEdit(self.input_frame)
        self.young_ratio_line.setObjectName(u"young_ratio_line")
        self.young_ratio_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.young_ratio_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.young_ratio_line, 8, 1, 1, 1)

        self.label_7 = QLabel(self.input_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_8 = QLabel(self.input_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_6 = QLabel(self.input_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.life_expectancy_line = QLineEdit(self.input_frame)
        self.life_expectancy_line.setObjectName(u"life_expectancy_line")
        self.life_expectancy_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.life_expectancy_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.life_expectancy_line, 11, 1, 1, 1)

        self.male_ratio_line = QLineEdit(self.input_frame)
        self.male_ratio_line.setObjectName(u"male_ratio_line")
        self.male_ratio_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.male_ratio_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.male_ratio_line, 9, 1, 1, 1)

        self.label_10 = QLabel(self.input_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.bmi_line = QLineEdit(self.input_frame)
        self.bmi_line.setObjectName(u"bmi_line")
        self.bmi_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.bmi_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.bmi_line, 2, 1, 1, 1)

        self.label_12 = QLabel(self.input_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)

        self.label_3 = QLabel(self.input_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.urban_line = QLineEdit(self.input_frame)
        self.urban_line.setObjectName(u"urban_line")
        self.urban_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.urban_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.urban_line, 5, 1, 1, 1)

        self.population_line = QLineEdit(self.input_frame)
        self.population_line.setObjectName(u"population_line")
        self.population_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.population_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.population_line, 6, 1, 1, 1)

        self.label_4 = QLabel(self.input_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.area_line = QLineEdit(self.input_frame)
        self.area_line.setObjectName(u"area_line")
        self.area_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.area_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.area_line, 4, 1, 1, 1)

        self.label_14 = QLabel(self.input_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_2 = QLabel(self.input_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.country_select_combobox = QComboBox(self.input_frame)
        self.country_select_combobox.setObjectName(u"country_select_combobox")
        sizePolicy2.setHeightForWidth(self.country_select_combobox.sizePolicy().hasHeightForWidth())
        self.country_select_combobox.setSizePolicy(sizePolicy2)
        self.country_select_combobox.setCursor(QCursor(Qt.ArrowCursor))
        self.country_select_combobox.setContextMenuPolicy(Qt.PreventContextMenu)
        self.country_select_combobox.setStyleSheet(u"QComboBox {\n"
"		background-color:rgb(255, 255, 255);\n"
"        border: 1px solid gray; \n"
"        border-radius: 3px;   \n"
"        padding: 3px;  \n"
"    }\n"
"QComboBox::drop-down {\n"
"        border-left: 1px solid gray;\n"
"		image: url(:/icons/images/icons/cil-arrow-bottom-2.png);\n"
"		width: 25px; \n"
"    }")
        self.country_select_combobox.setFrame(True)

        self.gridLayout.addWidget(self.country_select_combobox, 0, 1, 1, 1)

        self.year_line = QLineEdit(self.input_frame)
        self.year_line.setObjectName(u"year_line")
        self.year_line.setStyleSheet(u"QLineEdit{\n"
"		background-color:rgb(255, 255, 255);\n"
"		border: 1px solid gray;  /* Border color */\n"
"        border-radius: 3px; \n"
"}")
        self.year_line.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.year_line, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.input_frame)

        self.predict_button_frame = QFrame(self.right_frame)
        self.predict_button_frame.setObjectName(u"predict_button_frame")
        sizePolicy1.setHeightForWidth(self.predict_button_frame.sizePolicy().hasHeightForWidth())
        self.predict_button_frame.setSizePolicy(sizePolicy1)
        self.predict_button_frame.setFrameShape(QFrame.StyledPanel)
        self.predict_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.predict_button_frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.predict_button = QPushButton(self.predict_button_frame)
        self.predict_button.setObjectName(u"predict_button")
        sizePolicy5.setHeightForWidth(self.predict_button.sizePolicy().hasHeightForWidth())
        self.predict_button.setSizePolicy(sizePolicy5)
        self.predict_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.predict_button.setAutoFillBackground(False)
        self.predict_button.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(218, 218, 218)\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(0, 0, 0);\n"
"	font-size:12px;\n"
"	color:white;\n"
"	font-weight: bold;\n"
"	border-radius: 5px; \n"
"	border:0\n"
"}")
        self.predict_button.setCheckable(False)
        self.predict_button.setChecked(False)
        self.predict_button.setAutoExclusive(False)
        self.predict_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.predict_button)

        self.auto_fill_button = QPushButton(self.predict_button_frame)
        self.auto_fill_button.setObjectName(u"auto_fill_button")
        sizePolicy5.setHeightForWidth(self.auto_fill_button.sizePolicy().hasHeightForWidth())
        self.auto_fill_button.setSizePolicy(sizePolicy5)
        self.auto_fill_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.auto_fill_button.setAutoFillBackground(False)
        self.auto_fill_button.setStyleSheet(u"QPushButton:checked\n"
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
"	color:white;\n"
"	font-weight: bold;\n"
"	border-radius: 5px; \n"
"	border:0\n"
"}")
        self.auto_fill_button.setCheckable(False)
        self.auto_fill_button.setChecked(False)
        self.auto_fill_button.setAutoExclusive(False)
        self.auto_fill_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.auto_fill_button)


        self.verticalLayout.addWidget(self.predict_button_frame)

        self.display_output_frame = QFrame(self.right_frame)
        self.display_output_frame.setObjectName(u"display_output_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(4)
        sizePolicy8.setHeightForWidth(self.display_output_frame.sizePolicy().hasHeightForWidth())
        self.display_output_frame.setSizePolicy(sizePolicy8)
        palette1 = QPalette()
        brush10 = QBrush(QColor(0, 0, 127, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.display_output_frame.setPalette(palette1)
        self.display_output_frame.setStyleSheet(u"QFrame {\n"
"        border: 1px solid gray; \n"
"        border-radius: 5px;\n"
"		background-color:rgb(0, 0, 127)\n"
"    }")
        self.display_output_frame.setFrameShape(QFrame.StyledPanel)
        self.display_output_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.display_output_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_label = QLabel(self.display_output_frame)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setStyleSheet(u"QFrame {\n"
"        border: 1px solid gray; \n"
"        border-radius: 5px;\n"
"		background-color:rgb(218, 218, 218);\n"
"	font-size:12px;\n"
"	color:black;\n"
"	font-weight: bold;\n"
"    }")
        self.output_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.output_label)


        self.verticalLayout.addWidget(self.display_output_frame)


        self.horizontalLayout.addWidget(self.right_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Year</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sample predict</span></p></body></html>", None))
        self.age_predict_button.setText(QCoreApplication.translate("Form", u"Age Prediction", None))
        self.population_growth_button.setText(QCoreApplication.translate("Form", u"Population growth ", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Mortality/1000 live births</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Total area</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Young age ratio</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Population</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Retirement age ratio</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Urban population ratio</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Male population ratio</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Life expectancy</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">BMI</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">GDP</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Year</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Your country</span></p></body></html>", None))
        self.predict_button.setText(QCoreApplication.translate("Form", u"Predict", None))
        self.auto_fill_button.setText(QCoreApplication.translate("Form", u"Auto Fill", None))
        self.output_label.setText("")
    # retranslateUi




class Predict_widget(QWidget):
    def __init__(self, parent=None):
        super(Predict_widget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Load all country
        self.data = self.load_graph()
        predict = Predict(life_predict = False)
        predict.create_new_json()
        self.graph_list = self.data.get_graph()
        self.columns = self.data.get_columns()
        self.countries = self.data.get_rows("Country")
        self.ui.country_select_combobox.addItem("None")
        for country in self.countries:
            self.ui.country_select_combobox.addItem(country)
        self.ui.country_select_combobox.setFixedWidth(130)
        #Set up input line
        self.ui.label_12.setVisible(False)
        self.ui.life_expectancy_line.setVisible(False)
        #self.ui.country_select_combobox.setVisible(False)
        #self.ui.label_2.setVisible(False)
        self.ui.year_line.setValidator(QIntValidator())
        self.ui.bmi_line.setValidator(QDoubleValidator())
        self.ui.gdp_line.setValidator(QDoubleValidator())
        self.ui.area_line.setValidator(QDoubleValidator())
        self.ui.urban_line.setValidator(QDoubleValidator())
        self.ui.population_line.setValidator(QIntValidator())
        self.ui.retirement_line.setValidator(QDoubleValidator())
        self.ui.young_ratio_line.setValidator(QDoubleValidator())
        self.ui.male_ratio_line.setValidator(QDoubleValidator())
        self.ui.mortality_line.setValidator(QDoubleValidator())
        self.ui.life_expectancy_line.setValidator(QDoubleValidator())
        # Connect button signals
        self.ui.predict_button.clicked.connect(self.predict)
        self.ui.age_predict_button.clicked.connect(lambda: self.predict_life())
        self.ui.population_growth_button.clicked.connect(lambda: self.predict_growth())
        self.ui.auto_fill_button.clicked.connect(lambda : self.auto_fill())
        # Set up world map
        self.ui.year_combobox.addItems(self.change_world_map(2016))
        self.ui.year_combobox.currentIndexChanged.connect(lambda : self.change_world_map(int(self.ui.year_combobox.currentText())))
    def load_graph(self):
        
        return Visualization()
    def remove_all_widgets(self, layout):
        for i in range(layout.count()):
                
                item = layout.itemAt(i)
                widget = item.widget()
                widget.hide()
    def predict(self):
        lines_valid_range = {self.ui.bmi_line : [0, 1000], self.ui.gdp_line : [0, 10000000], self.ui.area_line : [1, 10000000000], self.ui.urban_line : [0, 100], self.ui.population_line : [1, 100000000000], self.ui.retirement_line : [0, 100], self.ui.young_ratio_line : [0, 100], self.ui.male_ratio_line : [0, 100], self.ui.mortality_line : [0, 1000], self.ui.life_expectancy_line : [1, 10000]}
        for line, range in lines_valid_range.items():
            if line.text() == "":
                line.setStyleSheet("""
                                QLineEdit{
                                background-color:rgb(255, 255, 255);
                                border: 1px solid red;  /* Border color */
                                border-radius: 3px; 
                                }""")
            elif float(line.text()) > range[1] or float(line.text()) < range[0]:
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
                try:
                    symbol = ""
                    input_dict = {"BMI" : float(self.ui.bmi_line.text()), "GDP_per_Capita" : float(self.ui.gdp_line.text()), "Total Area (sq km)" : float(self.ui.area_line.text()), "Urban Population Ratio" : float(self.ui.urban_line.text()), "Population" : float(self.ui.population_line.text()), "Retirement Age Dependency Ratio" : float(self.ui.retirement_line.text()), "Young Age Dependency Ratio" : float(self.ui.young_ratio_line.text()), "Male Population Ratio" : float(self.ui.male_ratio_line.text()), "Infant mortality per 1000 live births" : float(self.ui.mortality_line.text()), "Year": int(self.ui.year_line.text())}
                    region_dict = {
                                'Australia and New Zealand': ['Australia', 'New Zealand'],
                                'Central and Southern Asia': ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Kazakhstan', 
                                                                'Kyrgyzstan', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka', 'Tajikistan', 
                                                                'Uzbekistan', 'Turkmenistan'],
                                'Eastern and South-Eastern Asia': ['Brunei', 'Cambodia', 'China', 'East Timor', 'Indonesia', 'Japan', 
                                                                        'Laos', 'Malaysia', 'Mongolia', 'Myanmar', 'Philippines', 'Singapore', 
                                                                        'South Korea', 'Thailand', 'Vietnam'],
                                'Europe and Northern America': ['Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 
                                                                'Bulgaria', 'Canada', 'Croatia', 'Czechia', 'Denmark', 'Estonia', 
                                                                'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 
                                                                'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 
                                                                'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 
                                                                'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 
                                                                'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'United States'],
                                'Latin America and the Caribbean': ['Antigua and Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belize', 
                                                                        'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 
                                                                        'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Grenada', 
                                                                        'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 
                                                                        'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Saint Kitts and Nevis', 
                                                                        'Saint Lucia', 'Saint Vincent and the Grenadines', 'Suriname', 
                                                                        'Trinidad and Tobago', 'Uruguay', 'Venezuela'],
                                'Northern Africa and Western Asia': ['Algeria', 'Armenia', 'Azerbaijan', 'Bahrain', 'Cyprus', 'Egypt', 
                                                                        'Georgia', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 
                                                                        'Morocco', 'Oman', 'Qatar', 'Saudi Arabia', 'Sudan', 'Syria', 
                                                                        'Tunisia', 'Turkey', 'United Arab Emirates', 'Yemen'],
                                'Oceania': ['Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia (country)', 'Nauru', 'Palau', 
                                                'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'],
                                'Sub-Saharan Africa': ['Angola', 'Benin', 'Botswana', 'Burundi', 'Cameroon', 'Cape Verde', 
                                                        'Central African Republic', 'Chad', 'Comoros', 'Congo', "Cote d'Ivoire", 
                                                        'Democratic Republic of the Congo', 'Burkina Faso', 'Djibouti', 
                                                        'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 
                                                        'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 
                                                        'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 
                                                        'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 
                                                        'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'Tanzania', 'Togo', 
                                                        'Uganda', 'Zambia', 'Zimbabwe']
                                }
                    for region, countries_list in region_dict.items():
                        if self.ui.country_select_combobox.currentText() in countries_list:
                            input_dict["SDG Region"] = region
                    if "SDG Region" not in  input_dict.keys():
                        input_dict["SDG Region"] = None
                    if self.ui.population_growth_button.isChecked():
                        input_dict["Life Expectancy"] = float(self.ui.life_expectancy_line.text())
                        predict = Predict(life_predict = False)
                        #predict.create_new_json()
                        add_text = "Population growth:\n"
                        symbol = "%"
                    else:
                        predict = Predict(life_predict = True)
                        add_text = "Life expectancy:\n"
                    ans = predict.predict(input_dict)
                    
                    self.ui.output_label.setText(add_text + str(round(ans.item(), 2)) + symbol)
                    self.ui.output_label.setStyleSheet("""
                                QLabel{
                                        border: 1px solid gray; 
                                        border-radius: 5px;
		                        background-color:rgb(218, 218, 218);
	                                font-size:20px;
	                                color:black;
	                                font-weight: bold;
                                }""")
                except Exception as e:
                    print(e)
    def predict_life(self):
        self.ui.label_12.setVisible(False)
        self.ui.life_expectancy_line.setVisible(False)
    def predict_growth(self):
        self.ui.label_12.show()
        self.ui.life_expectancy_line.show()
    def change_world_map(self, year):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folders = os.listdir(script_dir + "\World_map")
        for save_folder in folders:
            if int(save_folder) == year:
                files = os.listdir(script_dir + "\World_map\\" + save_folder)
                for file in files:
                    pixmap = QPixmap(script_dir + "\World_map\\" + save_folder + "\\"+ file)
                    label = QLabel()
                    label.setPixmap(pixmap)  # Set the pixmap to the label
                    label.setAlignment(Qt.AlignCenter)  # Center the image in the frame
                    #label.setGeometry(0, 0, pixmap.width(), pixmap.height())
                    if self.ui.worldmap_display.layout() is None:
            
                        layout = QVBoxLayout(self.ui.worldmap_display)
                        
                    else:
                        layout = self.ui.worldmap_display.layout()
                    self.remove_all_widgets(layout)
                    layout.addWidget(label)
        return folders
    def auto_fill(self):
        
        if self.ui.country_select_combobox.currentText() != None:
            self.ui.country_select_combobox.setStyleSheet("""QComboBox {
                        background-color:rgb(255, 255, 255);
                        border: 1px solid gray; 
                        border-radius: 3px;   
                        padding: 3px;  
                }
                QComboBox::drop-down {
                        border-left: 1px solid gray;
                                image: url(:/icons/images/icons/cil-arrow-bottom-2.png);
                                width: 25px; 
                }""")
             #Find Data
            file_path =  os.path.dirname(os.path.abspath(__file__)) + "\MongoDB\Data\cleaned_data.csv"  # Replace with your CSV file path
            df = pd.read_csv(file_path)
            try:
                
                filtered_rows = df[(df['Year'] == int(self.ui.year_line.text())) & (df['Country'] == self.ui.country_select_combobox.currentText())]
                result_row = filtered_rows.to_dict(orient='records')[0]
                if not filtered_rows.empty:
                    line_dict = {"BMI" : self.ui.bmi_line, "GDP_per_Capita" : self.ui.gdp_line, "Total Area (sq km)" : self.ui.area_line, "Urban Population Ratio" : self.ui.urban_line, "Population" : self.ui.population_line, "Retirement Age Dependency Ratio" : self.ui.retirement_line, "Young Age Dependency Ratio" : self.ui.young_ratio_line, "Male Population Ratio" : self.ui.male_ratio_line, "Infant mortality per 1000 live births" : self.ui.mortality_line, "Life Expectancy" : self.ui.life_expectancy_line}
                    for key, line in line_dict.items():
                        line.setText(str(result_row[key]))
            except Exception as e:
                print(e)
                self.ui.year_line.setStyleSheet("""QLineEdit {
                        background-color:rgb(255, 255, 255);
                        border: 1px solid red; 
                        border-radius: 3px;   
                        padding: 3px;  
                }
                QComboBox::drop-down {
                        border-left: 1px solid gray;
                                image: url(:/icons/images/icons/cil-arrow-bottom-2.png);
                                width: 25px; 
                }""")
        else:
            self.ui.country_select_combobox.setStyleSheet("""QComboBox {
                        background-color:rgb(255, 255, 255);
                        border: 1px solid red; 
                        border-radius: 3px;   
                        padding: 3px;  
                }
                QComboBox::drop-down {
                        border-left: 1px solid gray;
                                image: url(:/icons/images/icons/cil-arrow-bottom-2.png);
                                width: 25px; 
                }""")
