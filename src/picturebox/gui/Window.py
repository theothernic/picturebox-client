#! /usr/bin/env python

import os
from PyQt5 import QtWidgets, uic

class UiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiWindow, self).__init__()
        uic.loadUi(os.path.dirname(os.path.realpath(__file__)) + '/../resources/ui/MainWindow.ui', self)
        self.show()

