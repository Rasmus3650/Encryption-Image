import sys
import os
import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import *
from key_gen import keyGen
from gui import Ui_MainWindow

class StartGui(QtGui.QMainWindow):
    def __init__(self, parent = None):
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartGui()
    myapp.show()
    sys.exit(app.exec_())
