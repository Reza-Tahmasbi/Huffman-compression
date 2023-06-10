# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget_Main(object):
    def setupUi(self, Widget_Main):
        if not Widget_Main.objectName():
            Widget_Main.setObjectName(u"Widget_Main")
        Widget_Main.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget_Main.sizePolicy().hasHeightForWidth())
        Widget_Main.setSizePolicy(sizePolicy)
        Widget_Main.setMinimumSize(QSize(1366, 768))
        Widget_Main.setMaximumSize(QSize(1366, 768))
        self.menuBox = QFrame(Widget_Main)
        self.menuBox.setObjectName(u"menuBox")
        self.menuBox.setGeometry(QRect(0, 0, 150, 768))
        self.menuBox.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"\n"
"}")
        self.menuBox.setFrameShape(QFrame.StyledPanel)
        self.menuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.menuBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 140, 154, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.encoderPage_button = QPushButton(self.verticalLayoutWidget)
        self.encoderPage_button.setObjectName(u"encoderPage_button")
        self.encoderPage_button.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(18)
        self.encoderPage_button.setFont(font)
        self.encoderPage_button.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(252, 163, 17);\n"
"color: rgb(20, 33, 61);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		color: rgb(229, 229, 229);\n"
"	\n"
"}")
        self.encoderPage_button.setCheckable(False)
        self.encoderPage_button.setAutoRepeat(False)
        self.encoderPage_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.encoderPage_button)

        self.decoderPage_button = QPushButton(self.verticalLayoutWidget)
        self.decoderPage_button.setObjectName(u"decoderPage_button")
        self.decoderPage_button.setMinimumSize(QSize(0, 60))
        self.decoderPage_button.setFont(font)
        self.decoderPage_button.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(252, 163, 17);\n"
"	color: rgb(20, 33, 61);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		color: rgb(229, 229, 229);\n"
"	\n"
"}")
        self.decoderPage_button.setCheckable(False)
        self.decoderPage_button.setAutoRepeat(False)
        self.decoderPage_button.setAutoExclusive(False)
        self.decoderPage_button.setFlat(False)

        self.verticalLayout.addWidget(self.decoderPage_button)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 60))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(252, 163, 17);\n"
"color: rgb(20, 33, 61);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(20, 33, 61);\n"
"		color: rgb(229, 229, 229);\n"
"	\n"
"}")
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setAutoRepeat(False)
        self.pushButton_11.setAutoExclusive(False)
        self.pushButton_11.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 60))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(252, 163, 17);\n"
"color: rgb(20, 33, 61);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(20, 33, 61);\n"
"		color: rgb(229, 229, 229);\n"
"	\n"
"}")
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setAutoRepeat(False)
        self.pushButton_12.setAutoExclusive(False)
        self.pushButton_12.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 60))
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(252, 163, 17);\n"
"color: rgb(20, 33, 61);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(20, 33, 61);\n"
"		color: rgb(229, 229, 229);\n"
"	\n"
"}")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setAutoRepeat(False)
        self.pushButton_13.setAutoExclusive(False)
        self.pushButton_13.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_13)

        self.mainBox = QFrame(Widget_Main)
        self.mainBox.setObjectName(u"mainBox")
        self.mainBox.setGeometry(QRect(0, 0, 1366, 768))
        self.mainBox.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 33, 61);\n"
"\n"
"\n"
"}")
        self.mainBox.setFrameShape(QFrame.StyledPanel)
        self.mainBox.setFrameShadow(QFrame.Raised)
        self.stackedPages_main = QStackedWidget(self.mainBox)
        self.stackedPages_main.setObjectName(u"stackedPages_main")
        self.stackedPages_main.setGeometry(QRect(150, 120, 1214, 651))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(39)
        self.gridLayout.setVerticalSpacing(15)
        self.openDrawingWindow_button = QPushButton(self.page)
        self.openDrawingWindow_button.setObjectName(u"openDrawingWindow_button")
        self.openDrawingWindow_button.setMinimumSize(QSize(155, 30))
        self.openDrawingWindow_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"	\n"
"	color: rgb(20, 33, 61);\n"
"}")

        self.gridLayout.addWidget(self.openDrawingWindow_button, 2, 4, 1, 1)

        self.inputText = QTextEdit(self.page)
        self.inputText.setObjectName(u"inputText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputText.sizePolicy().hasHeightForWidth())
        self.inputText.setSizePolicy(sizePolicy1)
        self.inputText.setMinimumSize(QSize(350, 350))
        self.inputText.setMaximumSize(QSize(350, 350))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputText.setFont(font1)
        self.inputText.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 17px;\n"
"	padding:10px;\n"
"	color: rgb(229, 229, 229);\n"
"\n"
"}")
        self.inputText.setTabChangesFocus(False)
        self.inputText.setOverwriteMode(True)

        self.gridLayout.addWidget(self.inputText, 0, 0, 1, 1)

        self.closeDrawingWindow_button = QPushButton(self.page)
        self.closeDrawingWindow_button.setObjectName(u"closeDrawingWindow_button")
        self.closeDrawingWindow_button.setMinimumSize(QSize(155, 30))
        self.closeDrawingWindow_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"	\n"
"	color: rgb(20, 33, 61);\n"
"}")

        self.gridLayout.addWidget(self.closeDrawingWindow_button, 2, 5, 1, 1)

        self.comboBox_Source = QComboBox(self.page)
        self.comboBox_Source.setObjectName(u"comboBox_Source")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(19)
        sizePolicy2.setHeightForWidth(self.comboBox_Source.sizePolicy().hasHeightForWidth())
        self.comboBox_Source.setSizePolicy(sizePolicy2)
        self.comboBox_Source.setMinimumSize(QSize(350, 30))
        self.comboBox_Source.setMaximumSize(QSize(350, 27))
        self.comboBox_Source.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	padding: 20px;\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.gridLayout.addWidget(self.comboBox_Source, 2, 0, 1, 1)

        self.tableCode = QTableWidget(self.page)
        if (self.tableCode.columnCount() < 3):
            self.tableCode.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCode.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCode.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCode.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableCode.setObjectName(u"tableCode")
        self.tableCode.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableCode.sizePolicy().hasHeightForWidth())
        self.tableCode.setSizePolicy(sizePolicy3)
        self.tableCode.setMinimumSize(QSize(350, 350))
        self.tableCode.setMaximumSize(QSize(350, 350))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.tableCode.setFont(font2)
        self.tableCode.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 17px;\n"
"selection-background-color: #fca311;\n"
"selection-color: rgb(0, 0, 0);\n"
"padding:5px;\n"
"	color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"                    border-top: 0px solid 4181C0;\n"
"                    border-bottom: 1px solid 4181C0;\n"
"                    border-right: 1px solid 4181C0;\n"
"                    background:rgb(252, 163, 17);\n"
"                    color: #fff;\n"
"border-radius: 37px;\n"
"text-align: center;\n"
"                    }\n"
"\n"
"")
        self.tableCode.setSortingEnabled(False)

        self.gridLayout.addWidget(self.tableCode, 0, 1, 1, 2)

        self.outputCode = QTextBrowser(self.page)
        self.outputCode.setObjectName(u"outputCode")
        sizePolicy3.setHeightForWidth(self.outputCode.sizePolicy().hasHeightForWidth())
        self.outputCode.setSizePolicy(sizePolicy3)
        self.outputCode.setMinimumSize(QSize(350, 350))
        self.outputCode.setMaximumSize(QSize(350, 350))
        self.outputCode.setFont(font1)
        self.outputCode.setStyleSheet(u"QTextBrowser{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 17px;\n"
"	padding:10px;\n"
"	color: rgb(229, 229, 229);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.outputCode, 0, 4, 1, 2)

        self.clearButton = QPushButton(self.page)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy3.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy3)
        self.clearButton.setMinimumSize(QSize(155, 30))
        self.clearButton.setMaximumSize(QSize(160, 16777215))
        self.clearButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"	\n"
"	color: rgb(20, 33, 61);\n"
"}")

        self.gridLayout.addWidget(self.clearButton, 2, 1, 1, 1)

        self.encodeButton = QPushButton(self.page)
        self.encodeButton.setObjectName(u"encodeButton")
        sizePolicy3.setHeightForWidth(self.encodeButton.sizePolicy().hasHeightForWidth())
        self.encodeButton.setSizePolicy(sizePolicy3)
        self.encodeButton.setMinimumSize(QSize(155, 30))
        self.encodeButton.setMaximumSize(QSize(160, 16777215))
        self.encodeButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"	\n"
"	color: rgb(20, 33, 61);\n"
"}")

        self.gridLayout.addWidget(self.encodeButton, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"Berlin Sans FB Demi"])
        font3.setPointSize(26)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(229, 229, 229);")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.stackedPages_main.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1221, 651))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(39)
        self.gridLayout_14.setVerticalSpacing(15)
        self.clearButton_decoder = QPushButton(self.frame)
        self.clearButton_decoder.setObjectName(u"clearButton_decoder")
        sizePolicy3.setHeightForWidth(self.clearButton_decoder.sizePolicy().hasHeightForWidth())
        self.clearButton_decoder.setSizePolicy(sizePolicy3)
        self.clearButton_decoder.setMinimumSize(QSize(155, 30))
        self.clearButton_decoder.setMaximumSize(QSize(160, 16777215))
        self.clearButton_decoder.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"	\n"
"	color: rgb(20, 33, 61);\n"
"}")

        self.gridLayout_14.addWidget(self.clearButton_decoder, 2, 1, 1, 1)

        self.outputText_decoder = QTextBrowser(self.frame)
        self.outputText_decoder.setObjectName(u"outputText_decoder")
        sizePolicy3.setHeightForWidth(self.outputText_decoder.sizePolicy().hasHeightForWidth())
        self.outputText_decoder.setSizePolicy(sizePolicy3)
        self.outputText_decoder.setMinimumSize(QSize(350, 350))
        self.outputText_decoder.setMaximumSize(QSize(350, 350))
        self.outputText_decoder.setFont(font1)
        self.outputText_decoder.setStyleSheet(u"QTextBrowser{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 17px;\n"
"	padding:10px;\n"
"	color: rgb(229, 229, 229);\n"
"\n"
"}")

        self.gridLayout_14.addWidget(self.outputText_decoder, 0, 4, 1, 2)

        self.tableCode_decoder = QTableWidget(self.frame)
        if (self.tableCode_decoder.columnCount() < 3):
            self.tableCode_decoder.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCode_decoder.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCode_decoder.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCode_decoder.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableCode_decoder.setObjectName(u"tableCode_decoder")
        self.tableCode_decoder.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.tableCode_decoder.sizePolicy().hasHeightForWidth())
        self.tableCode_decoder.setSizePolicy(sizePolicy3)
        self.tableCode_decoder.setMinimumSize(QSize(350, 350))
        self.tableCode_decoder.setMaximumSize(QSize(350, 350))
        self.tableCode_decoder.setFont(font2)
        self.tableCode_decoder.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 17px;\n"
"selection-background-color: #fca311;\n"
"selection-color: rgb(0, 0, 0);\n"
"padding:5px;\n"
"	color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"                    border-top: 0px solid 4181C0;\n"
"                    border-bottom: 1px solid 4181C0;\n"
"                    border-right: 1px solid 4181C0;\n"
"                    background:rgb(252, 163, 17);\n"
"                    color: #fff;\n"
"border-radius: 37px;\n"
"text-align: center;\n"
"                    }\n"
"\n"
"")
        self.tableCode_decoder.setSortingEnabled(False)

        self.gridLayout_14.addWidget(self.tableCode_decoder, 0, 1, 1, 2)

        self.decodeButton = QPushButton(self.frame)
        self.decodeButton.setObjectName(u"decodeButton")
        sizePolicy3.setHeightForWidth(self.decodeButton.sizePolicy().hasHeightForWidth())
        self.decodeButton.setSizePolicy(sizePolicy3)
        self.decodeButton.setMinimumSize(QSize(155, 30))
        self.decodeButton.setMaximumSize(QSize(160, 16777215))
        self.decodeButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 12px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(252, 163, 17);\n"
"\n"
"	\n"
"	color: rgb(20, 33, 61);\n"
"}")

        self.gridLayout_14.addWidget(self.decodeButton, 2, 2, 1, 1)

        self.inputCode_decoder = QTextBrowser(self.frame)
        self.inputCode_decoder.setObjectName(u"inputCode_decoder")
        sizePolicy3.setHeightForWidth(self.inputCode_decoder.sizePolicy().hasHeightForWidth())
        self.inputCode_decoder.setSizePolicy(sizePolicy3)
        self.inputCode_decoder.setMinimumSize(QSize(350, 350))
        self.inputCode_decoder.setMaximumSize(QSize(350, 350))
        self.inputCode_decoder.setFont(font1)
        self.inputCode_decoder.setStyleSheet(u"QTextBrowser{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 17px;\n"
"	padding:10px;\n"
"	color: rgb(229, 229, 229);\n"
"\n"
"}")

        self.gridLayout_14.addWidget(self.inputCode_decoder, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_14, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(229, 229, 229);")

        self.gridLayout_16.addWidget(self.label_4, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.stackedPages_main.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 1215, 648))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM "
                        "- SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
""
                        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -246, 1179, 1018))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 1000))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.textBrowser = QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 1151, 991))

        self.verticalLayout_2.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedPages_main.addWidget(self.page_3)
        self.label = QLabel(self.mainBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 1211, 121))
        font4 = QFont()
        font4.setFamilies([u"Genghis Khan"])
        font4.setPointSize(50)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.mainBox.raise_()
        self.menuBox.raise_()

        self.retranslateUi(Widget_Main)

        self.stackedPages_main.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget_Main)
    # setupUi

    def retranslateUi(self, Widget_Main):
        Widget_Main.setWindowTitle(QCoreApplication.translate("Widget_Main", u"Widget_Main", None))
        self.encoderPage_button.setText(QCoreApplication.translate("Widget_Main", u"Encoder", None))
        self.decoderPage_button.setText(QCoreApplication.translate("Widget_Main", u"Decode", None))
        self.pushButton_11.setText(QCoreApplication.translate("Widget_Main", u"Calculations", None))
        self.pushButton_12.setText(QCoreApplication.translate("Widget_Main", u"History", None))
        self.pushButton_13.setText(QCoreApplication.translate("Widget_Main", u"About", None))
        self.openDrawingWindow_button.setText(QCoreApplication.translate("Widget_Main", u"Open drawing window", None))
        self.inputText.setDocumentTitle("")
        self.inputText.setMarkdown("")
        self.inputText.setHtml(QCoreApplication.translate("Widget_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.closeDrawingWindow_button.setText(QCoreApplication.translate("Widget_Main", u"Close drawing window", None))
        ___qtablewidgetitem = self.tableCode.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget_Main", u"char", None));
        ___qtablewidgetitem1 = self.tableCode.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget_Main", u"quant", None));
        ___qtablewidgetitem2 = self.tableCode.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget_Main", u"code", None));
        self.outputCode.setHtml(QCoreApplication.translate("Widget_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.clearButton.setText(QCoreApplication.translate("Widget_Main", u"Clear", None))
        self.encodeButton.setText(QCoreApplication.translate("Widget_Main", u"Encode", None))
        self.label_2.setText(QCoreApplication.translate("Widget_Main", u"   Encoder page", None))
        self.clearButton_decoder.setText(QCoreApplication.translate("Widget_Main", u"Clear", None))
        self.outputText_decoder.setHtml(QCoreApplication.translate("Widget_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        ___qtablewidgetitem3 = self.tableCode_decoder.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget_Main", u"char", None));
        ___qtablewidgetitem4 = self.tableCode_decoder.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget_Main", u"quant", None));
        ___qtablewidgetitem5 = self.tableCode_decoder.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget_Main", u"code", None));
        self.decodeButton.setText(QCoreApplication.translate("Widget_Main", u"Decode", None))
        self.inputCode_decoder.setHtml(QCoreApplication.translate("Widget_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget_Main", u"   Decoder page", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbont"
                        "epovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoi"
                        "reuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkf"
                        "ghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjk"
                        "dhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovu"
                        "eiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvt"
                        "poiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlk"
                        "shglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjk"
                        "ldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjdfgkldjsnvtoireuvtpoiwnvuiope"
                        "urtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljgdbhsdkhgfjkdhgjkldfshgkjlfdhgklhdlkfghdlkshglkshdfgkldjsnvtoireuvtpoiwnvuiopeurtpvbontepovueiwopvtpeoiljg</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget_Main", u"    Huffman Coding", None))
    # retranslateUi

