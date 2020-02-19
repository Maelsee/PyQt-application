# import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip, QMessageBox, QDesktopWidget, QPushButton, QApplication, QMainWindow,QHBoxLayout, QVBoxLayout,
#                              QAction, qApp, QMenu)
# from PyQt5.QtGui import QFont
#
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication
#
# # class Example(QWidget):
# #
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.initUI()
# #
# #
# #     def initUI(self):
# #         # QToolTip.setFont(QFont('SansSerif', 10))
# #         #
# #         # self.setToolTip('This is a <b>QWidget</b> widget')
# #         #
# #         # btn = QPushButton('Quit', self)
# #         # btn.setToolTip('This is a <b>QPushButton</b> widget')
# #         # btn.clicked.connect(QCoreApplication.instance().quit)
# #         # btn.resize(btn.sizeHint())
# #         # btn.move(120, 100)
# #
# #
# #         # self.setGeometry(300, 300, 300, 220)
# #         # self.setWindowTitle('message box')
# #         # # self.setWindowIcon(QIcon('/home/dang/Nutstore Files/我的坚果云/GUI/project/web.png'))
# #         # self.show()
# #         self.resize(1000, 600)
# #         self.center()
# #
# #         self.setWindowTitle('Center')
# #         self.show()
# #
# #     def center(self):
# #
# #         qr = self.frameGeometry()
# #         cp = QDesktopWidget().availableGeometry().center()
# #         qr.moveCenter(cp)
# #         self.move(qr.topLeft())
# #
# #     def closeEvent(self, event):
# #
# #         reply = QMessageBox.question(self, 'Message',
# #                                      "Are you sure to quit?", QMessageBox.Yes |
# #                                      QMessageBox.No, QMessageBox.No)
# #
# #         if reply == QMessageBox.Yes:
# #             event.accept()
# #         else:
# #             event.ignore()
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.statusbar = self.statusBar()
#         self.statusbar.showMessage('Ready')
#
#
#         exitAct = QAction(QIcon('exit.png'), '&Exit', self)
#         exitAct.setShortcut('Ctrl+Q')
#         exitAct.setStatusTip('Exit application')
#         exitAct.triggered.connect(qApp.quit)
#
#         impMenu = QMenu('Import', self)
#         impAct = QAction('Import mail', self)
#         impMenu.addAction(impAct)
#
#         newAct = QAction('New', self)
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu1 = menubar.addMenu('&Input')
#         viewMenu = menubar.addMenu('View')
#
#         viewStatAct = QAction('View statusbar', self, checkable=True)
#         viewStatAct.setStatusTip('View statusbar')
#         viewStatAct.setChecked(True)
#         viewStatAct.triggered.connect(self.toggleMenu)
#
#         viewMenu.addAction(viewStatAct)
#         fileMenu.addAction(exitAct)
#         fileMenu.addAction(newAct)
#         fileMenu.addMenu(impMenu)
#         self.statusBar()
#
#
#
#         # self.statusBar().showMessage('Ready')
#
#         self.resize(1000, 600)
#         self.setWindowTitle('Check menu ')
#         self.center()
#         self.show()
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#     def closeEvent(self, event):
#
#         reply = QMessageBox.question(self, 'Message',
#                                      "Are you sure to quit?", QMessageBox.Yes |
#                                      QMessageBox.No, QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#     def toggleMenu(self, state):
#
#         if state:
#             self.statusbar.show()
#         else:
#             self.statusbar.hide()
#
#     def contextMenuEvent(self, event):
#
#         cmenu = QMenu(self)
#
#         newAct = cmenu.addAction("New")
#         opnAct = cmenu.addAction("Open")
#         quitAct = cmenu.addAction("Quit")
#         action = cmenu.exec_(self.mapToGlobal(event.pos()))
#
#         if action == quitAct:
#             qApp.quit()
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_()) # enter the mainloop
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets as QtWebKitWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QDesktopWidget
import pandas as pd
import  numpy as np

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self,path,path2):
        super().__init__()
        self.init_ui(path,path2)

    def init_ui(self,path,path2):
        self.resize(1000,800)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget_layout = QtWidgets.QGridLayout()
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 991, 701))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 981, 671))
        self.tableWidget.setObjectName("tableWidget")
        self.creat_table_show(path)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.webView = QtWebKitWidgets.QWebEngineView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(0, 0, 981, 671))
        self.create_webview(path2)
        self.webView.setObjectName("webView")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(909, 0, 61, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setText("o")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setText("o")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.centralwidget_layout.addWidget(self.tableWidget,0,0,9,9)
        self.centralwidget_layout.addWidget(self.widget)


        self.main_layout.addWidget(self.centralwidget)  # 左侧部件在第0行第0列，占8行3列

        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:9px;}QPushButton:hover{background:red;}''')
        # self.left_visit.setStyleSheet(
        #     '''QPushButton{background:#F7D674;border-radius:30px;}QPushButton:hover{background:yellow;}''')
        self.pushButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:9px;}QPushButton:hover{background:yellow;}''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.main_layout.setSpacing(0)  # 去除缝隙

        self.center()  # 在显示器中央显示

        # self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.clicked.connect(self.showMaximized)

        self.pushButton_2.clicked.connect(self.close)

    # def on_pushButton_clicked(self, MainWindow):
    #
    #     self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
    #     self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
    #     self.webView.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
    #     self.widget.setGeometry(QtCore.QRect(1850, 0, 61, 31))


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
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

def main():
    import  sys
    path = '/home/dang/Nutstore Files/我的坚果云/dataVisualization/datavisual/账户交易明细表.xls'
    path2 = '/home/dang/Nutstore Files/我的坚果云/GUI/project/pr值前50.html'
    app = QtWidgets.QApplication(sys.argv)
    gui = Ui_MainWindow(path,path2)
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()