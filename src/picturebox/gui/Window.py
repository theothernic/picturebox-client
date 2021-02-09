
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtGui
from picturebox.gui.widgets.MainWindow import Ui_MainWindow;
from picturebox.gui.widgets.SlideshowWindow import Ui_SlideshowWindow;
from picturebox.gui.widgets.SettingsWindow import Ui_SettingsWindow;

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.slideshow = None
        self.settings = None

        ui = Ui_MainWindow()
        ui.setupUi(self)

        self.init_window()


    def init_window(self):
        self.findChild(QPushButton, 'cmdStartSlideshow').clicked.connect(self.clicked_start_slideshow)
        self.findChild(QPushButton, 'cmdSettings').clicked.connect(self.clicked_settings)

    def clicked_start_slideshow(self):
        if self.slideshow is None:
            self.slideshow = SlideshowWindow(self)
            self.slideshow.showFullScreen()
        else:
            self.slideshow = None

        self.setWindowOpacity(0.)


    def clicked_settings(self):
        if self.settings is None:
            self.settings = SettingsWindow(self)
            self.settings.show()
        else:
            self.settings = None

class SlideshowWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        ui = Ui_SlideshowWindow()
        ui.setupUi(self)

        self.init_window()


    def init_window(self):
        self.findChild(QPushButton, 'cmdClose').clicked.connect(self.clicked_close)

    def clicked_close(self):
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent.setWindowOpacity(1.)


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        ui = Ui_SettingsWindow()
        ui.setupUi(self)

        self.init_window()

    def init_window(self):
        self.findChild(QPushButton, 'cmdSave').clicked.connect(self.clicked_save)
        self.findChild(QPushButton, 'cmdCancel').clicked.connect(self.clicked_cancel)

    def clicked_save(self):
        self.close()

    def clicked_cancel(self):
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent.setWindowOpacity(1.)