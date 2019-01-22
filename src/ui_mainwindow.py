# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui',
# licensing of 'ui/mainwindow.ui' applies.
#
# Created: Tue Dec 18 20:09:29 2018
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 549)
        MainWindow.setMinimumSize(QtCore.QSize(664, 548))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewFinder = QtWidgets.QLabel(self.centralwidget)
        self.viewFinder.setMinimumSize(QtCore.QSize(640, 480))
        self.viewFinder.setText("")
        self.viewFinder.setScaledContents(True)
        self.viewFinder.setAlignment(QtCore.Qt.AlignCenter)
        self.viewFinder.setObjectName("viewFinder")
        self.verticalLayout.addWidget(self.viewFinder)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))

