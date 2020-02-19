# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datashowDflg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWebEngineWidgets as QtWebKitWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QDesktopWidget, QMessageBox
import pandas as pd
import  numpy as np
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form,path,path2):
        Form.setObjectName("Form")
        Form.resize(830, 569)
        self.Form=Form
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 831, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 831, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.creat_table_show(path)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.webView = QtWebKitWidgets.QWebEngineView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(0, 0, 831, 531))
        self.create_webview(path2)
        self.webView.setObjectName("webView")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(740, 10, 71, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:9px;}QPushButton:hover{background:red;}''')
        # self.left_visit.setStyleSheet(
        #     '''QPushButton{background:#F7D674;border-radius:30px;}QPushButton:hover{background:yellow;}''')
        self.pushButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:9px;}QPushButton:hover{background:yellow;}''')
        self.Form.setWindowOpacity(0.9)  # 设置窗口透明度
        self.pushButton_2.setWindowOpacity(0.8)

        self.Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        qr = self.Form.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.Form.move(qr.topLeft())

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.clicked.connect(self.Form.showMaximized)

        self.pushButton_2.clicked.connect(self.on_pushButton_clicked1)

    def on_pushButton_clicked1(self):
        self.Form.close()
        return True

    def on_pushButton_clicked(self):
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.webView.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.widget.setGeometry(QtCore.QRect(1850, 0, 61, 31))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "表格数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "图形化数据"))

    def creat_table_show(self,path):
        path_openfile_name = path
        ###===========读取表格，转换表格，===========================================
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name)
        #print(input_table)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
        #print(input_table_rows)
        #print(input_table_colunms)
            input_table_header = input_table.columns.values.tolist()
        #print(input_table_header)

        ###===========读取表格，转换表格，============================================
        ###======================给tablewidget设置行列表头============================

            self.tableWidget.setColumnCount(input_table_colunms)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)

        ###======================给tablewidget设置行列表头============================

        ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                #print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            #print(input_table_rows_values_list)
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                #print(input_table_items_list)
                # print(type(input_table_items_list))

        ###==============将遍历的元素添加到tablewidget中并显示=======================

                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items)
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)

        ###================遍历表格每个元素，同时添加到tablewidget中========================
        else:
            self.centralWidget.show()

    def create_webview(self,path2):
        self.webView.setUrl(QtCore.QUrl.fromLocalFile(path2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    path='/home/dang/Nutstore Files/我的坚果云/dataVisualization/datavisual/账户交易明细表.xls'
    path2='/home/dang/Nutstore Files/我的坚果云/GUI/project/html/pr值前50.html'
    ui.setupUi(Form,path,path2)
    Form.show()
    sys.exit(app.exec_())
