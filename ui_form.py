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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPlainTextEdit, QProgressBar, QPushButton, QScrollArea,
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
"	border-top-right-radius:25px;\n"
"	border-bottom-right-radius:25px;\n"
"\n"
"}")
        self.menuBox.setFrameShape(QFrame.StyledPanel)
        self.menuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.menuBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 190, 154, 422))
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

        self.calcPage_button = QPushButton(self.verticalLayoutWidget)
        self.calcPage_button.setObjectName(u"calcPage_button")
        self.calcPage_button.setMinimumSize(QSize(0, 60))
        self.calcPage_button.setFont(font)
        self.calcPage_button.setStyleSheet(u"QPushButton{\n"
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
        self.calcPage_button.setCheckable(False)
        self.calcPage_button.setAutoRepeat(False)
        self.calcPage_button.setAutoExclusive(False)
        self.calcPage_button.setFlat(False)

        self.verticalLayout.addWidget(self.calcPage_button)

        self.historyPage_button = QPushButton(self.verticalLayoutWidget)
        self.historyPage_button.setObjectName(u"historyPage_button")
        self.historyPage_button.setMinimumSize(QSize(0, 60))
        self.historyPage_button.setFont(font)
        self.historyPage_button.setStyleSheet(u"QPushButton{\n"
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
        self.historyPage_button.setCheckable(False)
        self.historyPage_button.setAutoRepeat(False)
        self.historyPage_button.setAutoExclusive(False)
        self.historyPage_button.setFlat(False)

        self.verticalLayout.addWidget(self.historyPage_button)

        self.aboutPage_button = QPushButton(self.verticalLayoutWidget)
        self.aboutPage_button.setObjectName(u"aboutPage_button")
        self.aboutPage_button.setMinimumSize(QSize(0, 60))
        self.aboutPage_button.setFont(font)
        self.aboutPage_button.setStyleSheet(u"QPushButton{\n"
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
        self.aboutPage_button.setCheckable(False)
        self.aboutPage_button.setAutoRepeat(False)
        self.aboutPage_button.setAutoExclusive(False)
        self.aboutPage_button.setFlat(False)

        self.verticalLayout.addWidget(self.aboutPage_button)

        self.logoButton = QPushButton(self.menuBox)
        self.logoButton.setObjectName(u"logoButton")
        self.logoButton.setGeometry(QRect(0, 50, 151, 131))
        self.logoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoButton.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u"E:/\u0637\u0631\u0627\u062d\u06cc/Huffman/logo_huffman.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoButton.setIcon(icon)
        self.logoButton.setIconSize(QSize(90, 90))
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
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left"
                        "-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"/*"
                        " HORIZONTAL SCROLLBAR - HOMEWORK */\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
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
"	padding: 0px 15px;\n"
"	\n"
"	color: rgb(229, 229, 229);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"\n"
"        border-top: 6;\n"
"        border-left: 6;\n"
"        border-right: 6;\n"
"        border-bottom: 6;\n"
"        background-color: #283050;\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QListView::item:selected {\n"
"      border: 1px solid #6a6ea9;\n"
"\n"
"  }\n"
"\n"
"  QListView::item:selected:!active {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"\n"
"  }\n"
"\n"
"  QListView::item:selected:active {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"	background-color: rgb(252, 163, 17);\n"
"color: rgb(20, 33, 61);\n"
"  }\n"
""
                        "\n"
"  QListView::item:hover {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"	\n"
"	background-color: rgb(107, 107, 107);\n"
"\n"
"  }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(5"
                        "9, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
                        "\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
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
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BA"
                        "R VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	s"
                        "ubcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.tableCode.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableCode.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
"}\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-t"
                        "op-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"/* HORIZONTAL SCROLLBAR - HOM"
                        "EWORK */\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
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
"}\n"
"\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	bor"
                        "der-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"/* HORIZONTAL SCROLLBAR "
                        "- HOMEWORK */\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
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
"\n"
"\n"
"\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handl"
                        "e:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	su"
                        "bcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}\n"
"")
        self.tableCode_decoder.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableCode_decoder.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
"}\n"
"\n"
"\n"
"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	bor"
                        "der-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"/* HORIZONTAL SCROLLBAR "
                        "- HOMEWORK */\n"
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
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
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
        self.frame_2.setGeometry(QRect(0, 50, 1221, 601))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScroll"
                        "Bar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
""
                        "    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1187, 1360))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"Forte"])
        font4.setPointSize(37)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.tryButton = QPushButton(self.frame_3)
        self.tryButton.setObjectName(u"tryButton")
        self.tryButton.setMinimumSize(QSize(150, 31))
        font5 = QFont()
        font5.setFamilies([u"MV Boli"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.tryButton.setFont(font5)
        self.tryButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 1px solid rgb(252, 163, 17);\n"
"	border-radius: 15px;\n"
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

        self.horizontalLayout.addWidget(self.tryButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_4.addWidget(self.frame_3, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.tableWidget_2 = QTableWidget(self.frame_4)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem16)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setFamilies([u"Segoe Print"])
        font6.setPointSize(18)
        self.tableWidget_2.setFont(font6)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(20, 33, 61);\n"
"	border: 0px solid rgb(252, 163, 17);\n"
"	border-right: 1px solid #fff;\n"
"selection-background-color: #fca311;\n"
"selection-color: rgb(0, 0, 0);\n"
"padding:0px;\n"
"	color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"					\n"
"	font: 700 9pt \"Segoe UI\";\n"
"                    border-top: 0px solid 4181C0;\n"
"                    border-bottom: 1px solid 4181C0;\n"
"                    border-right: 1px solid 4181C0;\n"
"                    background:rgb(252, 163, 17);\n"
"                    color: #fff;\n"
"border-radius: 0px;\n"
"text-align: center;\n"
"padding:5px\n"
"                    }\n"
"\n"
"")
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(True)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.tableWidget_2)

        self.plainTextEdit_5 = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.plainTextEdit_5.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_5.setSizePolicy(sizePolicy5)
        self.plainTextEdit_5.setMinimumSize(QSize(0, 150))
        font7 = QFont()
        font7.setFamilies([u"Segoe Print"])
        font7.setPointSize(11)
        self.plainTextEdit_5.setFont(font7)
        self.plainTextEdit_5.setStyleSheet(u"border: 0px solid #fff;\n"
"border-left: 1px solid #fff;\n"
"color: rgb(252, 163, 17);\n"
"margin:0px;\n"
"padding:10px;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.plainTextEdit_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.plainTextEdit_4 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMinimumSize(QSize(0, 750))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Emoji"])
        font8.setPointSize(18)
        self.plainTextEdit_4.setFont(font8)
        self.plainTextEdit_4.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"margin:0px;\n"
"padding:50px;\n"
"")

        self.gridLayout_4.addWidget(self.plainTextEdit_4, 2, 0, 1, 2)

        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy6)
        self.plainTextEdit_2.setMinimumSize(QSize(0, 303))
        self.plainTextEdit_2.setFont(font8)
        self.plainTextEdit_2.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"margin:0px;\n"
"padding:50px;\n"
"")

        self.gridLayout_4.addWidget(self.plainTextEdit_2, 0, 0, 1, 2)


        self.verticalLayout_6.addLayout(self.gridLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedPages_main.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.frame_5 = QFrame(self.page_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 1221, 651))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        font9 = QFont()
        font9.setFamilies([u"Forte"])
        font9.setPointSize(20)
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_10, 2, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 4, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.widget_2 = QWidget(self.frame_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 300))
        self.widget_2.setStyleSheet(u"border:1px solid #fff;\n"
"border-radius:25px")
        self.calculatedRatio_hafez = QLabel(self.widget_2)
        self.calculatedRatio_hafez.setObjectName(u"calculatedRatio_hafez")
        self.calculatedRatio_hafez.setGeometry(QRect(40, 60, 241, 106))
        font10 = QFont()
        font10.setPointSize(60)
        self.calculatedRatio_hafez.setFont(font10)
        self.calculatedRatio_hafez.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")
        self.progressBar_hafez = QProgressBar(self.widget_2)
        self.progressBar_hafez.setObjectName(u"progressBar_hafez")
        self.progressBar_hafez.setGeometry(QRect(60, 190, 171, 26))
        self.progressBar_hafez.setValue(0)

        self.gridLayout_6.addWidget(self.widget_2, 4, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 4, 4, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 5, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 4, 0, 1, 1)

        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 300))
        self.widget.setStyleSheet(u"border:1px solid #fff;\n"
"border-radius:25px")
        self.calculatedRatio = QLabel(self.widget)
        self.calculatedRatio.setObjectName(u"calculatedRatio")
        self.calculatedRatio.setGeometry(QRect(40, 60, 241, 106))
        self.calculatedRatio.setFont(font10)
        self.calculatedRatio.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 190, 171, 26))
        self.progressBar.setValue(0)

        self.gridLayout_6.addWidget(self.widget, 4, 1, 1, 1)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color:rgb(252, 163, 17);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_11, 3, 3, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color:rgb(252, 163, 17);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_9, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font9)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_7, 2, 1, 1, 1)

        self.stackedPages_main.addWidget(self.page_6)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.scrollArea_2 = QScrollArea(self.page_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 60, 1211, 581))
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        self.scrollArea_2.setStyleSheet(u"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScroll"
                        "Bar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
""
                        "    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1197, 757))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.gridLayout_5.addLayout(self.horizontalLayout_5, 4, 1, 1, 2)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(400, 279))
        self.label_6.setStyleSheet(u"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:50px;\n"
"padding-right:0px")
        self.label_6.setPixmap(QPixmap(u"E:/\u0637\u0631\u0627\u062d\u06cc/Huffman/David Huffman.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy7)
        self.plainTextEdit_3.setMinimumSize(QSize(700, 700))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI Emoji"])
        font11.setPointSize(18)
        font11.setStrikeOut(False)
        font11.setKerning(True)
        font11.setStyleStrategy(QFont.PreferAntialias)
        self.plainTextEdit_3.setFont(font11)
        self.plainTextEdit_3.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"margin:0px;\n"
"padding:50px;\n"
"")
        self.plainTextEdit_3.setLineWidth(1)
        self.plainTextEdit_3.setBackgroundVisible(False)
        self.plainTextEdit_3.setCenterOnScroll(False)

        self.gridLayout_5.addWidget(self.plainTextEdit_3, 1, 1, 1, 2)


        self.verticalLayout_7.addLayout(self.gridLayout_5)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedPages_main.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.scrollArea_6 = QScrollArea(self.page_5)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setGeometry(QRect(0, 70, 1211, 581))
        sizePolicy4.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy4)
        self.scrollArea_6.setStyleSheet(u"QScrollArea{\n"
"border: 0px;\n"
"\n"
"margin:0px;\n"
"padding:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0px 15px 0;\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScroll"
                        "Bar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
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
"	background-color: rgb(252, 163, 17);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(221, 142, 15)\n"
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
""
                        "    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollArea_6.setFrameShape(QFrame.NoFrame)
        self.scrollArea_6.setFrameShadow(QFrame.Plain)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1211, 581))
        self.scrollAreaWidgetContents_11.setMinimumSize(QSize(0, 0))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_19)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.plainTextEdit_19 = QPlainTextEdit(self.scrollAreaWidgetContents_11)
        self.plainTextEdit_19.setObjectName(u"plainTextEdit_19")
        sizePolicy7.setHeightForWidth(self.plainTextEdit_19.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_19.setSizePolicy(sizePolicy7)
        self.plainTextEdit_19.setMinimumSize(QSize(700, 100))
        self.plainTextEdit_19.setFont(font11)
        self.plainTextEdit_19.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"margin:0px;\n"
"padding:50px;\n"
"")
        self.plainTextEdit_19.setLineWidth(1)
        self.plainTextEdit_19.setBackgroundVisible(False)
        self.plainTextEdit_19.setCenterOnScroll(False)

        self.gridLayout_18.addWidget(self.plainTextEdit_19, 1, 0, 1, 2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.gridLayout_18.addLayout(self.horizontalLayout_18, 4, 0, 1, 2)


        self.verticalLayout_15.addLayout(self.gridLayout_18)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_11)
        self.stackedPages_main.addWidget(self.page_5)
        self.label = QLabel(self.mainBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 1211, 121))
        font12 = QFont()
        font12.setFamilies([u"Genghis Khan"])
        font12.setPointSize(50)
        self.label.setFont(font12)
        self.label.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.mainBox.raise_()
        self.menuBox.raise_()

        self.retranslateUi(Widget_Main)

        self.logoButton.setDefault(False)
        self.stackedPages_main.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Widget_Main)
    # setupUi

    def retranslateUi(self, Widget_Main):
        Widget_Main.setWindowTitle(QCoreApplication.translate("Widget_Main", u"Widget_Main", None))
        self.encoderPage_button.setText(QCoreApplication.translate("Widget_Main", u"Encoder", None))
        self.decoderPage_button.setText(QCoreApplication.translate("Widget_Main", u"Decode", None))
        self.calcPage_button.setText(QCoreApplication.translate("Widget_Main", u"Calculations", None))
        self.historyPage_button.setText(QCoreApplication.translate("Widget_Main", u"History", None))
        self.aboutPage_button.setText(QCoreApplication.translate("Widget_Main", u"About", None))
        self.logoButton.setText("")
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
        self.label_3.setText(QCoreApplication.translate("Widget_Main", u"What is Huffman Coding?", None))
        self.tryButton.setText(QCoreApplication.translate("Widget_Main", u"try it out!", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget_Main", u"Naive Coding", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget_Main", u"number", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget_Main", u"1", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget_Main", u"2", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget_Main", u"3", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget_Main", u"A", None));
        ___qtablewidgetitem12 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Widget_Main", u"00", None));
        ___qtablewidgetitem13 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Widget_Main", u"B", None));
        ___qtablewidgetitem14 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Widget_Main", u"10", None));
        ___qtablewidgetitem15 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Widget_Main", u"C", None));
        ___qtablewidgetitem16 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Widget_Main", u"11", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("Widget_Main", u"Encoded output:\n"
"\n"
"00 01 00 11 00\n"
"10 char * 8 bits/char = 80 bits", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("Widget_Main", u"With the obtained table, we could later translate the binary codes back to the text without loosing information on the process, but is this the best way to do this?\n"
"\n"
"Huffman coding improves this process, being a lossless data compression algorithm that assigns variable-length codes based on the frequencies of our input characters.\n"
"\n"
"To determine how to assign the codes to each symbol, we have to take the following steps:\n"
"\n"
"	1- Analyse the frequency of each character\n"
"	2- Build the binary tree:\n"
"		* Take the pair of nodes with the least frequency\n"
"		* Iterate until left with one node\n"
"	3- Starting at the root, label the edge to the left child as 0 and the edge to the right child as 1. Iterate for every child.\n"
"	4- Go over the tree from each leaf to the root, writing down the labeled binary numbers, to generate the code word for each symbol.\n"
"\n"
"Once we get the code words, we will notice that using this method, shorter words are assigned to the most frequent symbols. Thi"
                        "s way, the resulted encoded string is shorter! You can try it out and see the difference using this project:", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("Widget_Main", u"First of all, let's start with codification in general. When we transmit information, need to convert the data (text, music, video, etc.) into binary code. To do this, we assign a code to each piece of data so we can distinguish them, and decode them later.\n"
"\n"
"If we take a string as an example, for example 'ABACA', we could assign a same-length code to each one of the unique symbols (usually called naive coding).", None))
        self.label_10.setText(QCoreApplication.translate("Widget_Main", u"compression ratio", None))
        self.calculatedRatio_hafez.setText(QCoreApplication.translate("Widget_Main", u"....", None))
        self.calculatedRatio.setText(QCoreApplication.translate("Widget_Main", u"....", None))
        self.label_11.setText(QCoreApplication.translate("Widget_Main", u" for hundred Hafiz poets", None))
        self.label_9.setText(QCoreApplication.translate("Widget_Main", u" for input text", None))
        self.label_7.setText(QCoreApplication.translate("Widget_Main", u"compression ratio", None))
        self.label_5.setText(QCoreApplication.translate("Widget_Main", u"Discovery of Huffman Codes", None))
        self.label_6.setText("")
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("Widget_Main", u"The story of the invention of Huffman codes is a great story that demonstrates that students can do better than professors. David Huffman (1925-1999) was a student in an electrical engineering course in 1951. His professor, Robert Fano, offered students a choice of taking a final exam or writing a term paper. Huffman did not want to take the final so he started working on the term paper. The topic of the paper was to find the most efficient (optimal) code. What Professor Fano did not tell his students was the fact that it was an open problem and that he was working on the problem himself. Huffman spent a lot of time on the problem and was ready to give up when the solution suddenly came to him. The code he discovered was optimal, that is, it had the lowest possible average message length. The method that Fano had developed for this problem did not always produce an optimal code. Therefore, Huffman did better than his professor. Later Huffman said that likely he would not have even attempted the problem if he h"
                        "ad known that his professor was struggling with it.", None))
        self.label_19.setText(QCoreApplication.translate("Widget_Main", u"programmers", None))
        self.plainTextEdit_19.setPlainText(QCoreApplication.translate("Widget_Main", u"We would like to acknowledge and thank the following coders for their contributions to this project:\n"
"Mohammad Biabani - @Mohammad-Biabani\n"
"Reza Tahmasbi - @rezatb\n"
"Ali Aziz - @S-AliAziz\n"
"\n"
"Shahrud University of Technology 2023 \u00ae", None))
        self.label.setText(QCoreApplication.translate("Widget_Main", u"    Huffman Coding", None))
    # retranslateUi

