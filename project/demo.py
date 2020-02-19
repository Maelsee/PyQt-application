import json
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import  os
import qtawesome
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, QSystemTrayIcon, QApplication, QMenu, QAction, qApp, \
    QFileDialog
from PyQt5 import QtWebEngineWidgets as QtWebKitWidgets
from PyQt5.QtCore import *
import  filetomembership
from datess import  Ui_Form
from datesDialog import  Ui_Dialog as Ui_TrueForm
from pagerank import    pagerankIterator
from hits import  hitIterator


class MainUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        # self.right_layout = QtWidgets.QVBoxLayout()

        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("算法介绍")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("文件导入")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("结果展示")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='white'), "pagerank")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='white'), "hits")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='white'), "其他")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.table', color='white'), "execl文件")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.file-text', color='white'), "json文件")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.files-o', color='white'), "其他文件")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.subscript', color='white'), "隶属度计算")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart', color='white'), "pagerank")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart', color='white'), "hits")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.lay_out_init()

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.main_layout.setSpacing(0) #去除缝隙

        self.center() # 在显示器中央显示
#=====================================================================================================

###==================事件====================================================================================
        self.left_close.setToolTip('Quit') #红色按钮退出
        self.left_close.clicked.connect(QCoreApplication.instance().quit)
        self.left_mini.setToolTip('最小化') #绿色按钮最小化
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_button_1.clicked.connect(self.changelayout_orian)
        self.left_button_1.clicked.connect(self.pagerankclick)

        self.left_button_2.clicked.connect(self.changelayout_orian)
        self.left_button_2.clicked.connect(self.hitsclick)

        self.left_button_3.clicked.connect(self.changelayout_orian)
        self.left_button_3.clicked.connect(self.otherclick)

        self.left_button_4.clicked.connect(self.changelayout_orian)
        self.left_button_4.clicked.connect(self.msg_execl)

        self.left_button_5.clicked.connect(self.changelayout_orian)
        self.left_button_5.clicked.connect(self.msg_json)

        self.left_button_6.clicked.connect(self.changelayout_orian)
        self.left_button_6.clicked.connect(self.msg_others)

        self.left_button_7.clicked.connect(self.changelayout1)

        self.left_button_8.clicked.connect(self.changelayout_orian)
        self.left_button_8.clicked.connect(self.pagerankclicked)

        self.left_button_9.clicked.connect(self.changelayout_orian)
        self.left_button_9.clicked.connect(self.hitsclicked)




####================第一部分：算法介绍=====================================================================
    def initcontent(self):
        htmlf = open('./html/init.html', 'r', encoding="utf-8")
        htmlcont = htmlf.read()

        self.webView.setHtml(htmlcont)

    def pagerankclick(self):
        htmlf = open('./html/pagerank.html', 'r', encoding="utf-8")
        htmlcont=htmlf.read()

        # self.webView.setHtml(htmlcont)
        self.webView.setUrl(QtCore.QUrl("https://baike.baidu.com/item/google%20pagerank/2465380?fr=aladdin"))


    def hitsclick(self):
        htmlf = open('./html/hits.html', 'r', encoding="utf-8")
        htmlcont=htmlf.read()
        # self.textbox.setHtml(htmlcont)
        self.webView.setUrl(QtCore.QUrl("https://blog.csdn.net/hguisu/article/details/8013489"))

    def otherclick(self):
        htmlf = open('./html/other.html', 'r', encoding="utf-8")
        htmlcont=htmlf.read()
        self.webView.setUrl(QtCore.QUrl("https://www.baidu.com/?tn=92495750_hao_pg"))        # self.textbox.setText(htmlcont)
        # self.textbox.setHtml(htmlcont)

####===============第二部分:导入文件===============================================================
    def msg_execl(self):
        global filepath,filebasepath
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
        filepath=openfile_name[0]
        if len(filepath) > 2:
            self.webView.setHtml("<h3>文件导入成功!</h3><br>路径：%s"%filepath)
        filebasepath=os.path.dirname(filepath)
        print(filepath)

    def msg_json(self):
        global filepath,filebasepath
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', '(*.json)')
        filepath=openfile_name[0]
        if len(filepath) > 2:
            self.webView.setHtml("<h3>文件导入成功!</h3><br>路径：%s"%filepath)
        print(filepath)
        filebasepath = os.path.dirname(filepath)
    def msg_others(self):
        global filepath,filebasepath
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', "All Files (*);;Text Files (*.txt)")
        filepath=openfile_name[0]
        if len(filepath) > 2:
            self.webView.setHtml("<h3>文件导入成功!</h3><br>路径：%s"%filepath)
        print(filepath)
        filebasepath = os.path.dirname(filepath)

####===============第三部分:算法结果===============================================================
    #计算隶属度
    def runmembership(self):
        self.progressBar.setVisible(True)

        # self.timer = QBasicTimer()
        # self.step=0
        # # self.timer.start(100, self)
        boolvcter=filetomembership.filetomembership(filepath)
        if boolvcter=="支持此格式文件":
            # self.timer.stop()
            self.progressBar.setProperty("value", 100)
        elif boolvcter=="不支持此格式文件！":
            self.webView_membership.setHtml("<h3>不支持此格式文件！</h3><br>请重新导入文件!")
            self.progressBar.setVisible(False)
            self.pushButton_result.setEnabled(False)
            self.pushButton_run.setEnabled(False)

    # def timerEvent(self, event):
    #     if self.step >= 100:
    #         self.timer.stop()
    #         return
    #     self.step = self.step + 5
    #     if self.step>95:
    #         self.step=95
    #     self.progressBar.setValue(self.step)

    def resultshow(self):
        execlpath=filebasepath+"/membership.xlsx"
        htmlpath=filebasepath+'/membership.html'
        self.setVisible(False)
        Form1 = QtWidgets.QDialog()
        ui = Ui_TrueForm()
        ui.setupUi(Form1,execlpath,htmlpath)
        Form1.show()
        Form1.exec_()
        self.setVisible(True)

    def pagerankclicked(self):
        print(filepath)
        print(filebasepath)
        self.webView.setHtml("计算文件path%s"%filepath+"<br><p>请稍等。。。。。。</p>")
        with open(filebasepath+"/membership.json","r",encoding="utf-8") as f:
            edges=json.load(f)["edges"]

        page=pagerankIterator(edges,filebasepath)
        x=page.pagerank()
        if x:
            self.webView.setHtml("<h3>pagerank计算完成！</h3>")
            execlpath = filebasepath + "/Prresult.xlsx"
            htmlpath = filebasepath + '/Prresult.html'
            self.setVisible(False)
            Form1 = QtWidgets.QDialog()
            ui = Ui_TrueForm()
            ui.setupUi(Form1, execlpath, htmlpath)
            Form1.show()
            Form1.exec_()
            self.setVisible(True)

    def hitsclicked(self):
        self.webView.setHtml("计算文件path%s"%filepath+"<br><p>请稍等。。。。。。</p>")

        with open(filebasepath+"/membership.json","r",encoding="utf-8") as f:
            edges=json.load(f)["edges"]
        hit=hitIterator(edges,filebasepath)
        x=hit.hits()
        if x:
            self.webView.setHtml("<h3>Hits计算完成！</h3>")

            execlpath = filebasepath + "/Hitsresult.xlsx"
            htmlpath = filebasepath + '/Hitsresult.html'
            self.setVisible(False)
            Form1 = QtWidgets.QDialog()
            ui = Ui_TrueForm()
            ui.setupUi(Form1, execlpath, htmlpath)
            Form1.show()
            Form1.exec_()
            self.setVisible(True)
    #隶属度布局
    def changelayout1(self):
        try:
            self.right_layout.removeWidget(self.right_bar_widget)
            self.right_bar_widget.deleteLater()
            self.right_bar_widget = None
            self.right_layout.removeWidget(self.textbox_widget)
            self.textbox_widget.deleteLater()
            self.textbox_widget = None
        except AttributeError:
            pass

        # 创建新布局
        self.widget = QtWidgets.QWidget()
        self.widget.resize(751, 641)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout()
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget.setLayout(self.gridLayout)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_run = QtWidgets.QPushButton()
        self.pushButton_run.setObjectName("pushButton_run")
        self.pushButton_run.setText("开始运行")
        self.horizontalLayout.addWidget(self.pushButton_run)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_result = QtWidgets.QPushButton()
        self.pushButton_result.setObjectName("pushButton_result")
        self.pushButton_result.setText("查看结果")
        self.horizontalLayout.addWidget(self.pushButton_result)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 2)
        self.webView_membership = QtWebKitWidgets.QWebEngineView()
        self.webView_membership.setUrl(QtCore.QUrl("https://baike.baidu.com/item/%E9%9A%B6%E5%B1%9E%E5%BA%A6%E5%87%BD%E6%95%B0/7625151?fr=aladdin"))
        self.webView_membership.setObjectName("webView_membership")
        self.gridLayout.addWidget(self.webView_membership, 0, 0, 2, 2)
        self.right_layout.addWidget(self.widget, 0, 0, 9, 9)
        # rightlay_ouList.append(self.widget)
        self.right_widget.setStyleSheet('''
                    QWidget#right_widget{
                           color:#232C51;
                           background:white;
                           border-top:1px solid darkGray;
                           border-bottom:1px solid darkGray;
                           border-right:1px solid darkGray;
                           border-top-right-radius:10px;
                           border-bottom-right-radius:10px;
                       }
                       QPushButton#pushButton_run{color:darkGray,border-radius:3px;}
                       QWebEngineView#webView_membership{
                               border:1px solid gray;
                               border-radius:10px;
                               padding:2px 4px;
                       }
                   ''')
        self.progressBar.setVisible(False)

        self.pushButton_run.clicked.connect(self.runmembership)

        self.pushButton_result.clicked.connect(self.resultshow)

    #恢复到初始布局
    def changelayout_orian(self):
        try:
            self.right_layout.removeWidget(self.widget)
            self.widget.deleteLater()
            self.widget = None
        except AttributeError :
            pass
        self.lay_out_init()
    #初始右侧布局
    def lay_out_init(self):
        # 搜索框
        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入，回车进行搜索")


        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        # rightlay_ouList.append(self.right_bar_widget)
        # 浏览器
        self.textbox_widget = QtWidgets.QWidget()
        self.textbox_layout = QtWidgets.QGridLayout()
        self.textbox_widget.setLayout(self.textbox_layout)
        self.webView = QtWebKitWidgets.QWebEngineView()
        self.initcontent()
        # self.webView.setUrl(QtCore.QUrl.fromLocalFile("/home/dang/Nutstore Files/我的坚果云/GUI/project/html/init.html"))
        self.webView.setObjectName("webView")
        self.textbox_layout.addWidget(self.webView, 2, 0, 7, 8)
        self.right_layout.addWidget(self.textbox_widget, 1, 0, 8, 9)
        # rightlay_ouList.append(self.textbox_widget)



        ###=============================美化============================================================================
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
                    QPushButton{border:none;color:white;}
                    QPushButton#left_label{
                        border:none;
                        border-bottom:1px solid white;
                        font-size:18px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                    QWidget#left_widget{
                        background:gray;
                        border-top:1px solid white;
                        border-bottom:1px solid white;
                        border-left:1px solid white;
                        border-top-left-radius:10px;
                        border-bottom-left-radius:10px;
                    } 
                ''')

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_widget.setStyleSheet('''
                    QWidget#right_widget{
                        color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-right-radius:10px;
                        border-bottom-right-radius:10px;
                    }
                    QLabel#right_lable{
                        border:none;
                        font-size:16px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                    QTextEdit{
                            border:1px solid gray;
                            width:300px;
                            border-radius:10px;
                            padding:2px 4px;
                    }
                ''')

        self.right_bar_widget_search_input.editingFinished.connect(self.search)

    def search(self):
        text=self.right_bar_widget_search_input.text()
        print(text)
        s="https://www.baidu.com/s?ie=UTF-8&wd=%s" % text
        print(s)
        self.webView.setUrl(QtCore.QUrl(s))
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':

    main()
