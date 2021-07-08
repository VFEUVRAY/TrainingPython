from PyQt5 import QtCore, QtGui, QtWidgets

class pageSwitchingButton(QtWidgets.QPushButton):
    def __init__(self, parent, index):
        QtWidgets.QPushButton.__init__(self, parent)
        self.index = index