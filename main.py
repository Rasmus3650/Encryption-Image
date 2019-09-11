import sys
import os
import base64
import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import *
from key_gen import keyGen
from gui import Ui_MainWindow


class StartGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.statusBar().setSizeGripEnabled(False)
        self.chooseFileButton.clicked.connect(self.openfile)
        self.imgString = ""
        self.imgPath = ""
        self.key = ""
        self.keyEdit.textChanged.connect(self.changetext)
        self.randomizeButton.clicked.connect(self.randomkey)
        self.encryptOwnButton.clicked.connect(self.encryptown)
        self.decryptOwnButton.clicked.connect(self.decryptown)
        self.encryptXorButton.clicked.connect(self.encryptxor)
        self.decryptXorButton.clicked.connect(self.decryptxor)

    def passd(self):
        pass

    def randomkey(self):
        self.keyEdit.setText(keyGen())

    def changetext(self):
        self.key = self.keyEdit.text()

    def openfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filepath, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;PNG Files (*.png);;JPG Files (*.jpg)",
                                                  options=options)
        if filepath:
            self.imgPath = filepath
            with open(filepath, "rb") as imageFile:
                strg = base64.b64encode(imageFile.read())
                self.imgString = strg.decode()
                imageFile.close()

    def encryptown(self):
        pass

    def decryptown(self):
        pass

    def encryptxor(self):
        pass

    def decryptxor(self):
        pass

    def savefile(self, encstring):
        filepath = self.imgPath.split(".")
        encstring = base64.b64decode(encstring)
        with open((filepath[0] + "_encoded.png"), "wb") as imageFile:
            imageFile.write(encstring)
            imageFile.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartGui()
    myapp.show()
    sys.exit(app.exec_())
