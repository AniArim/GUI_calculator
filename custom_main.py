import sys
from pathlib import Path

from PyQt5 import QtGui, QtWidgets, Qt
from PyQt5.QtCore import QStringListModel

from CustomWindow import *


class StyleHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def getWindowStyleSheet():
        style = '''QtWidgets.QMainWindow {
           background-color: #454545;
           border: 1px solid black;
           border-top-right-radius: 10px;
           border-top-left-radius:  10px;
           }'''
        return style


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        self.ui.header_frame.setMouseTracking(True)
        self.ui.closeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.cursorPosition = self.cursor().pos()
        self.windowPosition = self.pos()

        self.ui.closeWindowButton.clicked.connect(self.closeWindow)
        self.ui.minimizeWindowButton.clicked.connect(self.minimizeWindow)

        self.show()

    def mousePressEvent(self, event):
        self.cursorPosition = event.pos()
        if event.button == QtCore.Qt.LeftButton:
            self.windowPosition = event.pos()
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.windowPosition = event.pos()

    def mouseMoveEvent(self, event):
        try:
            delta = event.pos() - self.cursorPosition
            self.move(self.pos() + delta)
        except TypeError:
            return

    def closeWindow(self):
        self.close()
        self.destroy()

    def minimizeWindow(self):
        self.showMinimized()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


