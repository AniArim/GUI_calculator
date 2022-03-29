from PyQt5 import QtCore, QtWidgets, QtGui
from ErrorWindowUi import Ui_ErrorWindow
from pathlib import Path


class ErrorDialog(QtWidgets.QMainWindow, Ui_ErrorWindow):

    def __init__(self, parent=None, text=None, details=None):
        super(ErrorDialog, self).__init__(parent)
        self.text = text
        self.details = details
        self.setWindowIcon(QtGui.QIcon(f"{Path.cwd()/'images'/'icon.png'}"))

    def btn_clicked(self, name, obj):
        if name == "OK":
            obj.close()
        elif name == "Детали":
            obj.resize(560, 320)
            self.btn_details.setText("Скрыть")
            self.btn_details.setGeometry(QtCore.QRect(430, 280, 110, 30))
            self.btn_ok.setGeometry(QtCore.QRect(300, 280, 110, 30))
            self.plainTextEdit_details.setHidden(False)
        elif name == "Скрыть":
            obj.resize(560, 175)
            self.btn_details.setText("Детали")
            self.btn_details.setGeometry(QtCore.QRect(430, 130, 110, 30))
            self.btn_ok.setGeometry(QtCore.QRect(300, 130, 110, 30))
            self.plainTextEdit_details.setHidden(True)
