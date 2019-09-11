# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(259, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(100, 10, 71, 17))
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 261, 101))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.OWNtab = QtWidgets.QWidget()
        self.OWNtab.setObjectName("OWNtab")
        self.encryptOwnButton = QtWidgets.QPushButton(self.OWNtab)
        self.encryptOwnButton.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.encryptOwnButton.setCheckable(False)
        self.encryptOwnButton.setObjectName("encryptOwnButton")
        self.decryptOwnButton = QtWidgets.QPushButton(self.OWNtab)
        self.decryptOwnButton.setGeometry(QtCore.QRect(170, 30, 81, 21))
        self.decryptOwnButton.setObjectName("decryptOwnButton")
        self.tabWidget.addTab(self.OWNtab, "")
        self.XORtab = QtWidgets.QWidget()
        self.XORtab.setObjectName("XORtab")
        self.encryptXorButton = QtWidgets.QPushButton(self.XORtab)
        self.encryptXorButton.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.encryptXorButton.setCheckable(False)
        self.encryptXorButton.setObjectName("encryptXorButton")
        self.decryptXorButton = QtWidgets.QPushButton(self.XORtab)
        self.decryptXorButton.setGeometry(QtCore.QRect(170, 30, 81, 21))
        self.decryptXorButton.setObjectName("decryptXorButton")
        self.tabWidget.addTab(self.XORtab, "")
        self.randomizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomizeButton.setGeometry(QtCore.QRect(100, 50, 71, 17))
        self.randomizeButton.setObjectName("randomizeButton")
        self.keyEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.keyEdit.setGeometry(QtCore.QRect(40, 70, 211, 20))
        self.keyEdit.setObjectName("keyEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 47, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Encryption"))
        self.chooseFileButton.setText(_translate("MainWindow", "Choose file"))
        self.encryptOwnButton.setText(_translate("MainWindow", "Encrypt image"))
        self.decryptOwnButton.setText(_translate("MainWindow", "Decrypt Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OWNtab), _translate("MainWindow", "OWN"))
        self.encryptXorButton.setText(_translate("MainWindow", "Encrypt image"))
        self.decryptXorButton.setText(_translate("MainWindow", "Decrypt Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.XORtab), _translate("MainWindow", "XOR"))
        self.randomizeButton.setText(_translate("MainWindow", "Randomize"))
        self.label.setText(_translate("MainWindow", "Key:"))
