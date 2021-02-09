import sys

from PyQt5.QtWidgets import QApplication
from picturebox.gui.Window import MainWindow

def main():
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())

