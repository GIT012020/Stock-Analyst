from PyQt5 import QtCore, QtGui, QtWidgets
from interfaceLogic import open_file, read_file, data_analyst, closing_price, data_to_charts, show_data_table
from pdf_save import save_pdf
from tkinter import messagebox
from introduction import Ui_Form
import tkinter as tk
import os

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 899)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 350, 651, 211))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 570, 651, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 651, 155))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 651, 136))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 810, 651, 51))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 10, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_5.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.checkBox_3)
        MainWindow.setTabOrder(self.checkBox_3, self.checkBox_4)
        MainWindow.setTabOrder(self.checkBox_4, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_4)

        "connections"
        self.pushButton.clicked.connect(self.uploadData)
        self.pushButton_3.clicked.connect(self.stock_calculation)
        self.pushButton_2.clicked.connect(self.chart)
        self.pushButton_5.clicked.connect(self.show_data)
        self.pushButton_4.clicked.connect(save_pdf)

        '''if exit button "X" clicked delete "chosen_file.txt" '''
        app1.aboutToQuit.connect(self.Xclose)

    def uploadData(self):

        data = read_file(open_file())

        '''error if no file is choose'''
        if data == 'FileNotFoundError':
            self.label.setText('UPLOAD ERROR')
            self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.message_box('Please choose data to upload.')
            return
        if data == 'UnicodeDecodeError':
            self.label.setText('UPLOAD ERROR')
            self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.message_box('Please choose correct file to upload.')
            return

        if data == 'ValueError':
            self.label.setText('UPLOAD ERROR')
            self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.message_box('Please correct file format.')
            return

        if data == 'IndexError':
            self.label.setText('UPLOAD ERROR')
            self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.message_box('Selected file is empty.')
            return

        analysed_data = data_analyst(data)

        '''error if incorrect file is choose'''
        if analysed_data == 'IndexError':
            self.label.setText('UPLOAD ERROR')
            self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.message_box('Please choose correct file.')
            return

        self.lineEdit_13.setText(analysed_data[0])

        if len(analysed_data) == 6:
            self.label.setText('UPLOAD SUCCESSFUL')
            self.label.setStyleSheet("background-color: rgb(0, 255, 0);")

        if analysed_data[1] > 0:
            self.lineEdit_3.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.lineEdit_3.setText('INCREASE')
            self.lineEdit_7.setText(str(analysed_data[1]))
        if analysed_data[1] == 0:
            self.lineEdit_3.setStyleSheet("background-color: rgb(206, 206, 206);")
            self.lineEdit_3.setText('NO CHANGE')
            self.lineEdit_7.setText(str(analysed_data[1]))
        if analysed_data[1] < 0:
            self.lineEdit_3.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.lineEdit_3.setText('DECREASE')
            self.lineEdit_7.setText(str(analysed_data[1]))

        self.lineEdit_9.setText(str(analysed_data[2]))
        self.lineEdit_8.setText(str(analysed_data[3]))

        self.lineEdit_11.setText(str(analysed_data[4]))
        self.lineEdit_10.setText(str(analysed_data[5]))

    def stock_calculation(self):

        units = self.lineEdit_5.text()
        bought_price = self.lineEdit_4.text()
        end_price = closing_price()

        if units == '' or bought_price == '':
            self.message_box('Please provide "Number of shares" and "Purchase price"')
            return

        if end_price == 'FileNotFoundError':
            self.message_box('Please upload data first')
            return

        try:
            result = (float(end_price) - float(bought_price))*float(units)
        except ValueError:
            self.message_box('Please insert correct value e.g. "3" or "3.4" ')
            return

        self.lineEdit_6.setText(str(result))
        if result > 0:
            self.lineEdit_6.setStyleSheet("background-color: rgb(0, 255, 0);")
        if result == 0:
            self.lineEdit_6.setStyleSheet("background-color: rgb(206, 206, 206);")
        if result < 0:
            self.lineEdit_6.setStyleSheet("background-color: rgb(255, 0, 0);")

    def chart(self):
        """blocking button"""
        self.pushButton_5.setEnabled(False)

        if self.checkBox.isChecked():
            user_choice1 = 'OP'
            data_to_charts(user_choice1)
        if self.checkBox_2.isChecked():
            user_choice2 = 'DC'
            data_to_charts(user_choice2)
        if self.checkBox_3.isChecked():
            user_choice3 = 'CP'
            data_to_charts(user_choice3)
        if self.checkBox_4.isChecked():
            user_choice4 = 'DV'
            data_to_charts(user_choice4)

        """unblocking button"""
        self.pushButton_5.setEnabled(True)

    def show_data(self):
        self.pushButton_5.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        show_data_table()
        self.pushButton_5.setEnabled(True)
        self.pushButton_2.setEnabled(True)

    def message_box(self, text):
        root = tk.Tk()
        root.withdraw()
        canvas1 = tk.Canvas(root, width=300, height=300)
        canvas1.pack()
        tk.messagebox.showerror('Error', f'{text}', icon='error')
        root.destroy()

    def Xclose(self):
        file_delete = os.path.isfile('./chosen_file.txt')
        if file_delete:
            file_path = os.path.abspath('chosen_file.txt')
            os.remove(file_path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STOCK ANALYST"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Maximum price in the given period:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Minimum price in the given period:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Opening price in the given period:</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Closing price in the given period:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Price change in the given period:</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Gross Value Calculation (Purchase price - closing period price)"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Number of shares:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Purchase price:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Your gross result:</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Choose chart type:"))
        self.checkBox.setText(_translate("MainWindow", "Stock quotes - opening price"))
        self.checkBox_2.setText(_translate("MainWindow", "Stock daily change"))
        self.checkBox_3.setText(_translate("MainWindow", "Stock quotes - closing price"))
        self.checkBox_4.setText(_translate("MainWindow", "Stock daily volume"))
        self.pushButton_2.setText(_translate("MainWindow", "Display Chart"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DATA STATUS</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "UPLOAD DATA"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Period date (since / to):</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Period result (INCREASE / DECREASE):</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Show data in the table"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":

    import sys
    '''open introduction'''
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec()

    '''open interface'''
    app1 = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui1 = Ui_MainWindow()
    ui1.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app1.exec_())
