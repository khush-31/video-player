from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5 import QtCore, QtGui
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import recmandation as rmp
from logged import *
import cv2

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.watchlaterlist = []
        self.recmovielist = rmp.recmovieposterlist()
        self.recmoviesname = rmp.recmoviename()
        Dialog.setObjectName("Dialog")
        Dialog.resize(3000, 3000)
        Dialog.setMinimumSize(QtCore.QSize(1930, 1910))
        Dialog.setMaximumSize(QtCore.QSize(1930, 1910))
        Dialog.setStyleSheet("background-image:url(icon/bgg.jpg)")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(Dialog)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 10, 2000, 100))  # 9,9,1111,79
        self.horizontalWidget.setMaximumSize(QtCore.QSize(1900, 100))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(8, 5, 12, 4)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.verticalLayout.addLayout(self.horizontalLayout)
        self.Micon = QtWidgets.QLabel(self.horizontalWidget)
        self.Micon.setMaximumSize(QtCore.QSize(61, 61))
        self.Micon.setText("")
        self.Micon.setPixmap(QtGui.QPixmap("icon/micon3.png"))
        self.Micon.setScaledContents(True)
        self.Micon.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.Micon.setObjectName("Micon")
        self.horizontalLayout.addWidget(self.Micon)
        self.searchB = QtWidgets.QPushButton(self.horizontalWidget)
        self.searchB.setStyleSheet("background-color:rgb(212,0,0)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/search2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchB.setIcon(icon)
        self.searchB.setIconSize(QtCore.QSize(30, 30))
        self.searchB.setObjectName("searchB")
        self.horizontalLayout.addWidget(self.searchB)
        self.search = QtWidgets.QLineEdit(self.horizontalWidget)
        self.searchB.clicked.connect(self.searchb)
        # self.searchB.setAutoDefault(True)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.search.setFont(font)
        self.search.setStyleSheet('color:red;')
        self.search.setMaxLength(50748)
        self.search.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.search.returnPressed.connect(self.searchb)

        self.horizontalLayout.addWidget(self.search)
        self.clearB = QtWidgets.QPushButton(self.horizontalWidget)
        self.clearB.setText("")
        self.clearB.clicked.connect(self.searchclear)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/cross.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearB.setIcon(icon1)
        self.clearB.setIconSize(QtCore.QSize(20, 21))
        self.clearB.setObjectName("clearB")

        self.clearB.setStyleSheet("background-color:rgb(212,0,0)")
        self.horizontalLayout.addWidget(self.clearB)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/profile.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.logic4LIO)
        self.pushButton.setStyleSheet("background-color:red")
        self.horizontalLayout.addWidget(self.pushButton)
        self.profilecbox = QtWidgets.QComboBox(self.horizontalWidget)
        self.profilecbox.setMaximumSize(QtCore.QSize(600, 60))
        self.profilecbox.setObjectName("profilecbox")
        self.profilecbox.setStyleSheet('background-color:red')
        self.profilecbox.setStyleSheet('color:red')
        profilelistB = ["🡸 Click TO LOGIN"]
        self.profilecbox.addItems(profilelistB)
        self.profilecbox.setEditable(False)
        self.profilecbox.setInsertPolicy(QComboBox.NoInsert)
        self.profilecbox.setStyleSheet('border : 1px solid black')
        self.profilecbox.activated[str].connect(self.decide)
        self.profilecbox.setStyleSheet("background-color:rgb(212,0,0)")
        self.profilecbox.setStyleSheet('color:red;')
        font.setPointSize(10)
        self.profilecbox.setFont(font)
        self.horizontalLayout.addWidget(self.profilecbox)

        self.horizontalLayout.addWidget(self.profilecbox)
        self.wlb = QtWidgets.QPushButton(self.horizontalWidget)
        self.horizontalLayout.addWidget(self.wlb)
        self.wlb.clicked.connect(self.wl)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/wl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wlb.setIcon(icon11)
        self.wlb.setIconSize(QtCore.QSize(45, 45))
        self.wlb.setObjectName("wlb")
        # ---------------------------------------------------------------------------------------------------------------------------111111111111

        self.highlight = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.highlight.setFont(font)
        self.highlight.setText("🔔: PLEASE LOGIN FIRST")
        self.highlight.setObjectName("highlight")
        self.highlight.setStyleSheet('color:red')
        self.highlight.setGeometry(QtCore.QRect(0, 100, 1900, 20))
        # -----------------------------------------------------------------------------------------------------------------------------
        self.recommendation = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.recommendation.setFont(font)
        self.recommendation.setText("   RECOMMENDATION FOR YOU : ")
        self.recommendation.setObjectName("recommendation")
        self.recommendation.setStyleSheet('color:red')
        self.recommendation.setGeometry(QtCore.QRect(0, 130, 1900, 20))
        # --------------------------------------------------------------------------------------------------------------------------33333333333

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 170, 1700, 300))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.m2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m2.setText("")
        # self.m2.clicked.connect(self.searchb)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.recmovielist[1]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m2.setIcon(icon3)
        self.m2.setIconSize(QtCore.QSize(300, 300))
        self.m2.setObjectName("m2")
        self.m2.setMaximumSize(300, 300)
        self.gridLayout_3.addWidget(self.m2, 0, 1,1,1)
        self.m2.clicked.connect(self.watching)
        self.wl2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wl2.setFont(font)
        self.wl2.setStyleSheet("QPushButton{\n"
                               "color:red\n"
                               "}")

        self.wl2.setObjectName("wl2")
        # self.wl2.clicked.connect(self.wl)
        self.wl2.setMaximumSize(300, 40)
        self.gridLayout_3.addWidget(self.wl2, 1, 1, 1, 1)
        self.wl1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.wl1.setFont(font)
        self.wl1.setStyleSheet("QPushButton{\n"
                               "color:red\n"
                               "}")
        self.wl1.setMaximumSize(300,40)
        self.gridLayout_3.addWidget(self.wl1, 1, 0, 1, 1)
        self.wl3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.wl3.setFont(font)
        self.wl3.setStyleSheet("QPushButton{\n"
                               "color:red\n"
                               "}")
        self.wl3.setMaximumSize(300, 40)
        self.gridLayout_3.addWidget(self.wl3, 1, 2, 1, 1)
        self.m3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.recmovielist[2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m3.setIcon(icon4)
        self.m3.setIconSize(QtCore.QSize(300, 300))
        self.m3.setObjectName("m3")
        self.m3.setMaximumSize(300, 300)
        self.gridLayout_3.addWidget(self.m3, 0, 2, 1, 1)
        self.m1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(self.recmovielist[0]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m1.setIcon(icon5)
        self.m1.setIconSize(QtCore.QSize(300, 300))
        self.m1.setMaximumSize(300, 300)
        self.gridLayout_3.addWidget(self.m1, 0, 0, 1, 1)

        self.m4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(self.recmovielist[3]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m4.setIcon(icon6)
        self.m4.setIconSize(QtCore.QSize(300, 300))
        self.m4.setObjectName('m4')
        self.m4.setMaximumSize(300, 300)
        self.gridLayout_3.addWidget(self.m4, 0, 3, 1, 1)

        self.wl4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wl4.setFont(font)
        self.wl4.setStyleSheet("QPushButton{" "color:red\n""}")
        self.wl4.setObjectName("wl3")
        self.wl4.setMaximumSize(300, 40)
        self.gridLayout_3.addWidget(self.wl4, 1, 3, 1, 1)
        self.m5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.recmovielist[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m5.setIcon(icon4)
        self.m5.setIconSize(QtCore.QSize(300, 300))
        self.m5.setObjectName("m5self.m5")
        self.m5.setMaximumSize(300, 300)
        self.gridLayout_3.addWidget(self.m5, 0, 4, 1, 1)

        self.wl5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wl5.setFont(font)
        self.wl5.setStyleSheet("QPushButton{\n"
                               "color:red\n"
                               "}")
        self.wl5.setObjectName("wl5self.wl5")
        self.wl5.setMaximumSize(300, 40)
        self.gridLayout_3.addWidget(self.wl5, 1, 4, 1, 1)

        self.m6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.recmovielist[5]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m6.setIcon(icon4)
        self.m6.setIconSize(QtCore.QSize(300, 300))
        self.m6.setObjectName("m5self.m6")
        self.m6.setMaximumSize(300, 300)
        self.gridLayout_3.addWidget(self.m6, 0, 5, 1, 1)
        self.wl6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wl6.setFont(font)
        self.wl6.setStyleSheet("QPushButton{\n"
                               "color:red\n"
                               "}")
        self.wl6.setObjectName("wl5self.wl6")
        # self.wl6.clicked.connect(self.watchlater)
        self.wl6.setMaximumSize(300, 40)
        self.gridLayout_3.addWidget(self.wl6, 1, 5, 1, 1)

        self.m7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m7.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.recmovielist[6]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m7.setIcon(icon4)
        self.m7.setIconSize(QtCore.QSize(300, 300))
        self.m7.setObjectName("m5self.m7")
        self.m7.setMaximumSize(300, 300)
        # self.m7.clicked.connect(self.searchb)
        self.gridLayout_3.addWidget(self.m7, 0, 6, 1, 1)

        self.wl7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wl7.setFont(font)
        self.wl7.setStyleSheet("QPushButton{\n"
                               "color:red\n"
                               "}")
        self.wl7.setObjectName("wl5self.wl7")
        # self.wl7.clicked.connect(self.watchlater)
        self.wl7.setMaximumSize(300, 40)
        self.gridLayout_3.addWidget(self.wl7, 1, 6, 1, 1)

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.wlbdecider)
        self.buttongroup.addButton(self.wl1, 1)
        self.buttongroup.addButton(self.wl2, 2)
        self.buttongroup.addButton(self.wl3, 3)
        self.buttongroup.addButton(self.wl4, 4)
        self.buttongroup.addButton(self.wl5, 5)
        self.buttongroup.addButton(self.wl6, 6)
        self.buttongroup.addButton(self.wl7, 7)

        self.buttongroup_1 = QButtonGroup()
        self.buttongroup_1.buttonClicked[int].connect(self.vdodecider)
        self.buttongroup_1.addButton(self.m1, 1)
        self.buttongroup_1.addButton(self.m2, 2)
        self.buttongroup_1.addButton(self.m3, 3)
        self.buttongroup_1.addButton(self.m4, 4)
        self.buttongroup_1.addButton(self.m5, 5)
        self.buttongroup_1.addButton(self.m6, 6)
        self.buttongroup_1.addButton(self.m7, 7)

        self.fileList = []
        dirpath = 'rec'
        for f in os.listdir(dirpath):
            fpath = os.path.join(dirpath, f)
            if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg', '.jfif')):
                self.fileList.append(fpath)

        self.c = 0
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(35, 480, 1800, 450))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout1.setContentsMargins(10, 2, 2, 2)

        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.leftrecb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.leftrecb.setMaximumSize(QtCore.QSize(30, 50))
        self.b = False
        self.leftrecb.setText("")
        self.leftrecb.setStyleSheet("QPushButton{\n"
                                    "background-color:black\n"
                                    "}\n"
                                    "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/left.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftrecb.setIcon(icon)
        self.leftrecb.setIconSize(QtCore.QSize(30, 50))
        self.leftrecb.setObjectName("leftrecb")
        self.leftrecb.clicked.connect(self.leftrecbaction)
        self.horizontalLayout1.addWidget(self.leftrecb)
        self.recb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        # self.recb.setMaximumSize(QtCore.QSize(1800, 450))
        # self.recb.setSizeIncrement(QtCore.QSize(0, 0))
        self.recb.setStyleSheet("QPushButton{\n"
                                "background-color:black\n"
                                "border:4px solid white\n"
                                "}\n"
                                "")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.fileList[self.c]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recb.setIcon(icon1)
        self.recb.setIconSize(QtCore.QSize(1280, 480))
        self.recb.setMaximumSize(1300, 500)
        self.horizontalLayout1.addWidget(self.recb)
        self.rightrecb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rightrecb.setMaximumSize(QtCore.QSize(30, 50))

        self.rightrecb.setStyleSheet("QPushButton{\n"
                                     "background-color:black")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/right.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightrecb.setIcon(icon2)
        self.rightrecb.setIconSize(QtCore.QSize(30, 50))
        self.rightrecb.setObjectName("rightrecb")
        self.rightrecb.clicked.connect(self.rightrecbaction)
        self.horizontalLayout1.addWidget(self.rightrecb)
        # self.verticalLayout.addLayout(self.gridLayout)
        # self.verticalLayout.addLayout(self.horizontalLayout1)
        # -------------------------------------------------------------------------------------------------------
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.clearB, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.search)
        Dialog.setTabOrder(self.search, self.searchB)
        Dialog.setTabOrder(self.searchB, self.m1)
        Dialog.setTabOrder(self.m1, self.m2)
        Dialog.setTabOrder(self.m2, self.m3)
        Dialog.setTabOrder(self.m3, self.m4)
        Dialog.setTabOrder(self.m4, self.wl1)
        Dialog.setTabOrder(self.wl1, self.wl2)
        Dialog.setTabOrder(self.wl2, self.wl3)
        Dialog.setTabOrder(self.wl3, self.wl4)
        Dialog.setTabOrder(self.wl4, self.leftrecb)
        Dialog.setTabOrder(self.leftrecb, self.recb)
        Dialog.setTabOrder(self.recb, self.rightrecb)
        Dialog.setTabOrder(self.rightrecb, self.profilecbox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "VideoSearch"))
        self.wl2.setText(_translate("Dialog", "♥ WATCH LATER"))
        self.wl1.setText(_translate("Dialog", "♥ WATCH LATER"))
        self.wl3.setText(_translate("Dialog", "♥ WATCH LATER"))
        self.wl4.setText(_translate("Dialog", "♥ WATCH LATER"))
        self.wl5.setText(_translate("Dialog", "♥ WATCH LATER"))
        self.wl6.setText(_translate("Dialog", "♥ WATCH LATER"))
        self.wl7.setText(_translate("Dialog", "♥ WATCH LATER"))
        # self.wlb.setText(_translate("Dialog", "♥"))

    def logic4LIO(self):
        # if self.pushButton.clicked:
        #     print(self.pushButton.clicked)
        self.loginpage()
        self.io = 1
        self.win_ali()

    def wl(self):
        buttongrp = QButtonGroup()
        layout = QGridLayout()
        dlg1 = QDialog()
        dlg1.setGeometry(750, 100, 100, 400)
        scroll = QScrollArea()
        scroll.setGeometry(QtCore.QRect(800, 200, 1000, 1500))
        scroll.setWidgetResizable(True)
        scroll.setWidget(dlg1)
        scroll.setFixedHeight(400)
        scroll.setWindowTitle("Watchlater videos")
        scrollWidgetContents = QtWidgets.QWidget()
        scroll.setMinimumSize(1000,700)
        scrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 1109, 839))
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.show()

        layout11 = QVBoxLayout(scrollWidgetContents)
        layout.addLayout(layout11, 1, 6)
        buttongrp.buttonClicked[int].connect(scroll.close)
        # buttongrp.buttonClicked[int].connect(dlg.close)
        buttongrp.buttonClicked[int].connect(self.remove)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        ab = QPushButton(" ♥ Watch Later Videos ", dlg1)
        layout.addWidget(ab, 0, 1)
        ab.setMinimumSize(330,50)
        ab.setFont(font)
        ab.setStyleSheet("background-color:white; border:3px solid red; color:red;")
        if len(self.watchlaterlist) == 0:
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(10)
            b0 = QPushButton(" No Videos Added ", dlg1)
            layout.addWidget(b0, 1, 1)
            b0.setFont(font)
            b0.setStyleSheet("background-color:grey;border:1px solid white; color:white;")

        for i in range(len(self.watchlaterlist)):
            b1 = QtWidgets.QPushButton(scrollWidgetContents)
            a1 = QtWidgets.QPushButton(scrollWidgetContents)
            if i <= 2:
                layout.addWidget(b1, 1, i)
                layout.addWidget(a1, 2, i)
            elif i <= 5:
                layout.addWidget(b1, 3, i-3)
                layout.addWidget(a1, 4, i-3)
            else:
                layout.addWidget(b1, 5, i-6)
                layout.addWidget(a1, 6, i-6)

            b1.setStyleSheet("background-color:black;border:1px solid white;")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(
                QtGui.QPixmap(fr"recmovieposter\{self.watchlaterlist[i]}.jpg"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            b1.setIcon(icon1)
            b1.clicked.connect(dlg1.close)
            b1.setIconSize(QtCore.QSize(250, 250))
            a1.setText("REMOVE")
            a1.setStyleSheet("color:yellow;")
            buttongrp.addButton(a1, i)
        dlg1.setLayout(layout)
        dlg1.setWindowTitle("watch later")
        dlg1.setStyleSheet("background-image:url(icon/bgg.jpg)")
        dlg1.exec_()

    def remove(self, id):
        self.watchlaterlist.pop(id)
        self.b = True
        self.wl()

    def watching(self):
        pass

    def win_ali(self):
        profilelistA = ["Profile", "LogOut"]
        if self.io == 1:
            self.profilecbox.clear()
            self.profilecbox.addItems(profilelistA)
            self.profilecbox.setEditable(False)
            self.profilecbox.setInsertPolicy(QComboBox.NoInsert)
            self.pushButton.setEnabled(False)

    def vdodecider(self, id):
        from popup import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.exec_()
        for i in range(7):
            c = i + 1
            if self.buttongroup_1.button(id == c):
                if i <= 3:
                    os.system('python video/videopyfile/v0.py')
                elif i > 3 and i <= 5:
                    os.system('python video/videopyfile/v1.py')
                else:
                    os.system('python video/videopyfile/v2.py')

    def wlbdecider(self, id):
        for i in range(7):
            c = i + 1
            if self.buttongroup.button(id == c):
                bs = 'wl'
                bn = str(i + 1)
                cb = bs + bn
                cbmn = self.recmoviesname[i]
                if cbmn not in self.watchlaterlist:
                    self.watchlaterlist.append(cbmn)
                    self.highlight.setText('🔔: ✔' + cbmn + ' is Added to Watch Later')
                else:
                    self.highlight.setText('🔔: ✔' + cbmn + ' is Already Added to Watch Later')

    def loginpage(self):
        # os.system('python logged.py')
        from logged import Ui_Dialog
        Dlg = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dlg)
        Dlg.exec_()

    def decide(self, text):
        if text == "Profile":
            self.profile()
        # elif text == "Subscription":
        #     self.subscription()
        else:
            self.logout()

    def logout(self):
        profilelistBB = ["🡸 CLICK TO LOGIN"]
        self.profilecbox.clear()
        self.profilecbox.addItems(profilelistBB)
        self.pushButton.setEnabled(True)

    def profile(self):
        os.system('profilef.py')

    # def subscription(self):
    #     os.system('python subscription.py')

    def searchclear(self):
        self.search.setText("")

    def searchb(self):
        import difflib
        m = self.search.text()
        self.b = m.title()
        a = difflib.get_close_matches(self.b, self.recmoviesname, cutoff=0.6)
        if len(a) == 1:
            self.highlight.setText("❌: TO GO BACK PRESS CROSS AND THEN SEARCH BUTTON")
            for button in self.buttongroup_1.buttons():
                button.setVisible(False)
            for buttons in self.buttongroup.buttons():
                buttons.setVisible(False)
            d = self.recmoviesname.index(a[0])
            for i in range(7):
                if i==d:
                    k = self.buttongroup_1.button((d+1))
                    k.setVisible(True)
                    r = self.buttongroup.button((d+1))
                    r.setVisible(True)
        elif len(a) == 0:
            self.highlight.setText(" ❌:Nothing Found")
            cv2.waitKey(2000)
            for button in self.buttongroup_1.buttons():
                button.setVisible(True)
            for buttons in self.buttongroup.buttons():
                buttons.setVisible(True)
            self.highlight.setText("🔔: PLEASE LOGIN FIRST")

    def leftrecbaction(self):
        self.rightrecb.setEnabled(True)
        ci = self.c
        ll = self.fileList
        if ci == 0:
            self.leftrecb.setEnabled(False)
        else:
            cp = ll[ci - 1]
            self.c = ci - 1
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(cp), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.recb.setIcon(icon1)
            self.recb.setIconSize(QtCore.QSize(1280, 480))
            self.recb.setMaximumSize(1300, 500)

    def rightrecbaction(self):
        self.leftrecb.setEnabled(True)
        ci = self.c
        ll = self.fileList
        if ci == (len(self.fileList) - 1):
            self.rightrecb.setEnabled(False)
        else:
            cp = ll[ci + 1]
            self.c = ci + 1
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(cp), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.recb.setIcon(icon1)
            self.recb.setIconSize(QtCore.QSize(1280, 480))
            self.recb.setMaximumSize(1300, 500)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())