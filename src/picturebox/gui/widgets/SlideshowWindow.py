# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './resources/ui/SlideshowWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SlideshowWindow(object):
    def setupUi(self, SlideshowWindow):
        SlideshowWindow.setObjectName("SlideshowWindow")
        SlideshowWindow.resize(400, 300)
        SlideshowWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(SlideshowWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(SlideshowWindow)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.ActionBarWidget = QtWidgets.QWidget(SlideshowWindow)
        self.ActionBarWidget.setMinimumSize(QtCore.QSize(0, 40))
        self.ActionBarWidget.setObjectName("ActionBarWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ActionBarWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmdClose = QtWidgets.QPushButton(self.ActionBarWidget)
        self.cmdClose.setMinimumSize(QtCore.QSize(0, 40))
        self.cmdClose.setText("")
        self.cmdClose.setObjectName("cmdClose")
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout.addWidget(self.ActionBarWidget, 0, QtCore.Qt.AlignRight)

        self.retranslateUi(SlideshowWindow)
        QtCore.QMetaObject.connectSlotsByName(SlideshowWindow)

    def retranslateUi(self, SlideshowWindow):
        _translate = QtCore.QCoreApplication.translate
        SlideshowWindow.setWindowTitle(_translate("SlideshowWindow", "Form"))
