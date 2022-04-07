

from PyQt5 import QtCore, QtWidgets
from ErrorWindowUi import Ui_ErrorWindow


class ErrorDialog(QtWidgets.QMainWindow, Ui_ErrorWindow):

    def __init__(self, parent=None, text=None, details=None):
        super(ErrorDialog, self).__init__(parent)

        self.text = text
        self.details = details
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.cursorPosition = self.cursor().pos()
        self.windowPosition = self.pos()

    def add_functions(self):
        self.btn_ok.clicked.connect(lambda: self.btn_clicked(self.btn_ok.text(), self))
        self.btn_details.clicked.connect(lambda: self.btn_clicked(self.btn_details.text(), self))

        self.closeWindowButton.clicked.connect(self.closeWindow)
        self.questionWindowButton.clicked.connect(lambda: self.btn_clicked(self.btn_details.text(), self))

    def btn_clicked(self, name: QtWidgets.QPushButton.text, obj: QtWidgets.QMainWindow):
        """
        Обработка событий кнопок "ОК" и "Детали". Изменения текста кнопки и расширение/сворачивание окна.

        :param name: QtWidgets.QPushButton.text
        :param obj: <ErrorWindow.ErrorDialog object>
        :return: None
        """

        if name == "ОК":  # rus
            obj.close()

        elif name == "Детали":
            obj.resize(715, 390)
            self.btn_details.setText("Скрыть")
            self.btn_details.setGeometry(QtCore.QRect(560, 340, 130, 30))
            self.btn_ok.setGeometry(QtCore.QRect(420, 340, 130, 30))
            self.plainTextEdit_details.setGeometry(QtCore.QRect(20, 180, 670, 140))

        elif name == "Скрыть":
            obj.resize(715, 224)
            self.btn_details.setText("Детали")
            self.btn_details.setGeometry(QtCore.QRect(550, 180, 130, 30))
            self.btn_ok.setGeometry(QtCore.QRect(410, 180, 130, 30))
            self.plainTextEdit_details.setGeometry(QtCore.QRect(20, 230, 671, 141))

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

