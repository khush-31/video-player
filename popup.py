from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(400, 220)
        Dialog.setModal(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 140, 95, 45))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 140, 95, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(Dialog.close)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 340, 80))
        self.label.setObjectName("label")
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Permission"))
        self.pushButton.setText(_translate("Dialog", "Block"))
        self.pushButton_2.setText(_translate("Dialog", "Allow"))
        self.label.setText(_translate("Dialog", "Allow this app to access your camera? \n\n  🎦 Integrated Webcam"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.exec_()
#     sys.exit(app.exec_())
#     Dialog.show()