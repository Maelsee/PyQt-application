
from PyQt5 import QtWebEngineWidgets as QtWebKitWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd
import  numpy as np
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,path,path2):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 861, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.creat_table_show(path)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.webView = QtWebKitWidgets.QWebEngineView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(0, 0, 851, 591))
        self.create_webview(path2)
        self.webView.setObjectName("webView")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pagerank结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "数据显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "数据可视化"))














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
        # else:
        #     self.centralWidget.show()
    def create_webview(self,path2):

        self.webView.setUrl(QtCore.QUrl.fromLocalFile(path2))
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     path='/home/dang/Nutstore Files/我的坚果云/dataVisualization/datavisual/账户交易明细表.xls'
#     path2='/home/dang/Nutstore Files/我的坚果云/GUI/project/pr值前50.html'
#     ui.setupUi(MainWindow,path,path2)
#     MainWindow.show()
#     sys.exit(app.exec_())