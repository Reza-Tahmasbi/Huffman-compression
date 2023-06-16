# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget , QTableWidgetItem
from Huffman import huffman_encoder_decoder
import Hafez
import Calc

from collections import defaultdict
import tkinter as tk
import colorama
from colorama import Fore, Style
from art import * 

from tkinter import *


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget_Main


colorama.init()
def draw_tree(node, x, y, dx):

    if node is None:
        return

    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#fca311")
    canvas.create_text(x, y, text=f"{node.key}\n{node.freq}", font="Arial 12 bold")
    
    if node.left is not None:
        x_left = x - dx
        y_left = y + 80
        canvas.create_line(x, y + 20, x_left, y_left - 20, width=2 , fill="#e5e5e5")
        draw_tree(node.left, x_left, y_left, dx // 2)

    if node.right is not None:
        x_right = x + dx
        y_right = y + 80
        canvas.create_line(x, y + 20, x_right, y_right - 20, width=2 , fill="#e5e5e5")
        draw_tree(node.right, x_right, y_right, dx // 2)


def height(root):
    if root is None:
        return 0
    leftHeight=height(root.left)
    rightHeight=height(root.right)
    max_height= leftHeight
    if rightHeight>max_height:
        max_height = rightHeight
    return max_height+1




class Widget_Main(QWidget):
    default_style = """
        QPushButton{
	        background-color: rgb(252, 163, 17);
	        color: rgb(20, 33, 61);
	        border:none;
        }
        QPushButton:hover{
	    	color: rgb(229, 229, 229);
	    }    
        """
    current_style = "background-color: rgb(20, 33, 61); color:#e5e5e5" 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget_Main()
        self.ui.setupUi(self)
        self.ui.stackedPages_main.setCurrentIndex(2)
        self.ui.comboBox_Source.activated.connect(self.change_inputText)
        self.ui.encodeButton.clicked.connect(self.encode_inputText)

        #set column with for table codes
        self.ui.tableCode.setColumnWidth(0, 50)
        self.ui.tableCode.setColumnWidth(1, 60)
        self.ui.tableCode.setColumnWidth(2, 160)
        self.ui.tableCode_decoder.setColumnWidth(0, 50)
        self.ui.tableCode_decoder.setColumnWidth(1, 60)
        self.ui.tableCode_decoder.setColumnWidth(2, 160)

        #clear button click
        self.ui.clearButton.clicked.connect(self.clearAll_encoderPage)
        self.ui.clearButton_decoder.clicked.connect(self.clearAll_decoderPage)

        #set place holder text
        self.ui.inputText.setPlaceholderText("Write here the text to encode . . .")
        self.ui.inputCode_decoder.setPlaceholderText("Please enter a text from the encoder page first . . .")
        self.ui.outputCode.setPlaceholderText("Output coded by Huffman algorithm . . .")
        self.ui.outputText_decoder.setPlaceholderText("Output decoded by Huffman algorithm . . .")

        #buttons menu click
        self.ui.encoderPage_button.clicked.connect(self.encoderPage)
        self.ui.decoderPage_button.clicked.connect(self.decoderPage)
        self.ui.calcPage_button.clicked.connect(self.calcPage)
        self.ui.historyPage_button.clicked.connect(self.historyPage)
        self.ui.aboutPage_button.clicked.connect(self.aboutPage)
        self.ui.logoButton.clicked.connect(self.welcomePage)

        #encoder page buttons
        self.ui.openDrawingWindow_button.clicked.connect(self.openDrawingWindow)
        self.ui.closeDrawingWindow_button.clicked.connect(self.closeDrawingWindow)
        self.ui.decodeButton.clicked.connect(self.decode_inputCode)
        self.ui.tryButton.clicked.connect(self.goToPage_decoder)
        calcHafez = Calc.compressionRatioAverageForSampleTexts()
        self.ui.calculatedRatio_hafez.setText(str(round(calcHafez,1)) + "%")
        self.ui.progressBar_hafez.setValue(calcHafez)        

        for x in Hafez.Divan_e_Hafez:
            self.ui.comboBox_Source.addItem(x)
        
        #self.ui.tableWidget.item(1,1).setText()

    #go to page decoder with click try it out button
    def goToPage_decoder(self):
        self.encoderPage()

    def decode_inputCode(self):
        encoded, decoded, code_map2, freq_map2, root = huffman_encoder_decoder(self.ui.inputText.toPlainText())
        self.ui.outputText_decoder.setText(decoded)
    
    #welcome Page
    def welcomePage(self):
        self.ui.stackedPages_main.setCurrentIndex(2)  
        self.ui.decoderPage_button.setStyleSheet(self.default_style)
        self.ui.encoderPage_button.setStyleSheet(self.default_style)
        self.ui.historyPage_button.setStyleSheet(self.default_style)       
        self.ui.aboutPage_button.setStyleSheet(self.default_style)

    #encoder Page
    def encoderPage(self):
        self.ui.stackedPages_main.setCurrentIndex(0)
        self.ui.encoderPage_button.setStyleSheet(self.current_style)
        self.ui.decoderPage_button.setStyleSheet(self.default_style)
        self.ui.historyPage_button.setStyleSheet(self.default_style)
        self.ui.aboutPage_button.setStyleSheet(self.default_style)
        self.ui.calcPage_button.setStyleSheet(self.default_style)

    #decoder Page
    def decoderPage(self):
        self.ui.stackedPages_main.setCurrentIndex(1)
        self.ui.decoderPage_button.setStyleSheet(self.current_style)
        self.ui.encoderPage_button.setStyleSheet(self.default_style)
        self.ui.historyPage_button.setStyleSheet(self.default_style)
        self.ui.aboutPage_button.setStyleSheet(self.default_style)
        self.ui.calcPage_button.setStyleSheet(self.default_style)

    #calculated Page
    def calcPage(self):
        self.ui.stackedPages_main.setCurrentIndex(3)
        self.ui.calcPage_button.setStyleSheet(self.current_style)
        self.ui.decoderPage_button.setStyleSheet(self.default_style)
        self.ui.encoderPage_button.setStyleSheet(self.default_style)
        self.ui.historyPage_button.setStyleSheet(self.default_style)
        self.ui.aboutPage_button.setStyleSheet(self.default_style)

    #history Page
    def historyPage(self):
        self.ui.stackedPages_main.setCurrentIndex(4)
        self.ui.historyPage_button.setStyleSheet(self.current_style)
        self.ui.encoderPage_button.setStyleSheet(self.default_style)
        self.ui.decoderPage_button.setStyleSheet(self.default_style) 
        self.ui.aboutPage_button.setStyleSheet(self.default_style)
        self.ui.calcPage_button.setStyleSheet(self.default_style)

    #about Page
    def aboutPage(self):
        self.ui.stackedPages_main.setCurrentIndex(5)
        self.ui.aboutPage_button.setStyleSheet(self.current_style)
        self.ui.historyPage_button.setStyleSheet(self.default_style)
        self.ui.encoderPage_button.setStyleSheet(self.default_style)
        self.ui.decoderPage_button.setStyleSheet(self.default_style)       
        self.ui.calcPage_button.setStyleSheet(self.default_style)

    #clear all contents in encoder Page
    def clearAll_encoderPage(self):
        self.ui.tableCode.clearContents()
        self.ui.inputText.clear()
        self.ui.outputCode.clear()

    #clear all contents in decoder Page
    def clearAll_decoderPage(self):
        self.ui.tableCode_decoder.clearContents()
        self.ui.inputCode_decoder.clear()
        self.ui.outputText_decoder.clear()

    def change_inputText(self):
        self.ui.inputText.setText(Hafez.Divan_e_Hafez[self.ui.comboBox_Source.currentText()])

    def encode_inputText(self):
        print(self.ui.inputText.toPlainText())
        encoded, decoded, code_map2, freq_map2, root = huffman_encoder_decoder(self.ui.inputText.toPlainText())
        calculatedRatio = Calc.compressionRatioCalculator(encoded,decoded)
        self.clearAll_decoderPage()
        charList = sorted(code_map2)
        charList = code_map2
        #for delete_row in self.ui.tableCode.rowCount():
        #    self.ui.tableCode.removeRow(delete_row)
        #    print(delete_row)
        self.ui.calculatedRatio.setText(str(round(calculatedRatio,1)) + "%")
        self.ui.progressBar.setValue(calculatedRatio)
        self.ui.tableCode.setRowCount(len(charList))
        self.ui.tableCode_decoder.setRowCount(len(charList))
        row = 0
        e = 0
        for e in charList:  
            print(e)
            self.ui.tableCode.setItem(row, 0, QTableWidgetItem(e))
            self.ui.tableCode.setItem(row, 1, QTableWidgetItem(str(freq_map2[e])))
            self.ui.tableCode.setItem(row, 2, QTableWidgetItem(code_map2[e]))
            
            self.ui.tableCode_decoder.setItem(row, 0, QTableWidgetItem(e))
            self.ui.tableCode_decoder.setItem(row, 1, QTableWidgetItem(str(freq_map2[e])))
            self.ui.tableCode_decoder.setItem(row, 2, QTableWidgetItem(code_map2[e]))
            row += 1 
        self.ui.outputCode.setText(encoded)
        self.ui.inputCode_decoder.setText(encoded)
        print("finish")

    #open Drawing Window
    def openDrawingWindow(self):
        encoded, decoded, code_map, freq_map2, root2 = huffman_encoder_decoder(self.ui.inputText.toPlainText())
        if(height(root2) < 7 ):
            dx = height(root2)*60
            widthScreen1 = 800
            xStart = 900
        elif(height(root2) < 8):
            dx = height(root2)*100
            widthScreen1 = 3000
            xStart = 1400
        elif(height(root2) < 10):
            dx = height(root2)*200
            widthScreen1 = 8000
            xStart = 4000
        elif(height(root2) < 12):
            dx = height(root2)*300
            widthScreen1 = 17000
            xStart = 9000
        else:
            dx = height(root2)*1100
            widthScreen1 = 52000
            xStart = 25000

        print(height(root2))
        window.state('zoomed')
        draw_tree(root2, xStart, 50, dx)
        print(xStart)
        print(dx)
        window.deiconify()  

    #close Drawing Window
    def closeDrawingWindow(self):
        window.withdraw()
        canvas.delete("all")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget_Main()
    widget.show()
    #tkinter
    window=Tk()
    window.state('zoomed')
    frame=Frame(window,width=1900,height=300)
    frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)

    canvas=Canvas(frame,bg='#14213d',width=52000,height=1000,scrollregion=(0,0,52000,1000))
    hbar=Scrollbar(frame,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=canvas.xview)
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=1000,height=800)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT,expand=True,fill=BOTH)


    #encoded, decoded, code_map, freq_map, root = huffman_encoder_decoder("input()")

    #charList = sorted(code_map)
    #for key in charList:
        #print(key, code_map[key])
    #print(encoded)
    #print(decoded)

    window.withdraw()
    window.mainloop()    

    sys.exit(app.exec())
