import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from picturebox.gui.Window import UiWindow

def main():
    app = QApplication(sys.argv)

    win = UiWindow()
    win.show()

    sys.exit(app.exec_())

