import random
import string
import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5 import *
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
