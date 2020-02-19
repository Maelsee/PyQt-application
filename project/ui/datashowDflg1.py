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


class Ui_Dialog(object):
    def setupUi(self, Dialog,path,path2):
        Dialog.setObjectName("Dialog")
        Dialog.resize(913, 656)
        self.Form=Dialog
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget_2")
        self.creat_table_show(path)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.webView = QtWebKitWidgets.QWebEngineView(self.tab_4)
        self.create_webview(path2)
        self.webView.setObjectName("webView_2")
        self.gridLayout_2.addWidget(self.webView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:4px;}QPushButton:hover{background:red;}''')
        # self.left_visit.setStyleSheet(
        #     '''QPushButton{background:#F7D674;border-radius:30px;}QPushButton:hover{background:yellow;}''')
        self.pushButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:4px;}QPushButton:hover{background:yellow;}''')
        self.Form.setWindowOpacity(0.9)  # 设置窗口透明度
        # self.Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        qr = self.Form.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.Form.move(qr.topLeft())

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_clicked1)

    def on_pushButton_clicked1(self):
        self.Form.close()
        return True

    def on_pushButton_clicked(self):
        self.Form.resize(1920, 1080)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "表格数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "图形化数据"))
        self.pushButton.setText(_translate("Dialog", "最大化"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))


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
    Form = QtWidgets.QDialog()
    ui = Ui_Dialog()
    path='/home/dang/Nutstore Files/我的坚果云/dataVisualization/datavisual/账户交易明细表.xls'
    path2='/home/dang/Nutstore Files/我的坚果云/GUI/project/html/pr值前50.html'
    ui.setupUi(Form,path,path2)
    Form.show()
    sys.exit(app.exec_())