# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatplotlibWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QDoubleValidator


class Ui_MatplotlibWindow(object):
    def __init__(self, figure=""):
        self.figure = figure

    def setupUi(self, MatplotlibWindow):

        QLocale.setDefault(QLocale(QLocale(QLocale.English, QLocale.UnitedStates)))
        MatplotlibWindow.setObjectName("MatplotlibWindow")
        MatplotlibWindow.resize(740, 675)
        MatplotlibWindow.setStyleSheet(
"color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.647, fx:0.5, fy:0.5, stop:0.104478 rgba(40, 10, 10, 215), stop:0.880597 rgba(0, 0, 0, 255));\n"
)
        self.windowFrame = QtWidgets.QFrame(MatplotlibWindow)
        self.windowFrame.setGeometry(QtCore.QRect(0, 0, 740, 670))
        self.windowFrame.setStyleSheet(
            "QFrame {\n"
            "border-top: 3px solid rgb(126, 0, 0);\n"
            "border-left: 3px solid  rgb(126, 0, 0);\n"
            "border-right: 1px solid  rgb(214, 0, 0);\n"
            "border-bottom: 1px solid  rgb(214, 0, 0);\n"
            "border-radius: 10px;\n"
            "}\n"
            "QPushButton {\n"
            "background-color: qlineargradient(spread:reflect, x1:1, y1:0.522, x2:1, y2:0, stop:0.174129 rgba(15, 0, 0, 255), stop:0.890547 rgba(161, 100, 100, 218));\n"
            "color: rgb(209, 209, 209);\n"
            "font: 10pt \"Segoe Print\";\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: qlineargradient(spread:reflect, x1:1, y1:0.522, x2:1, y2:0, stop:0 rgba(102, 7, 0, 240), stop:0.80597 rgba(161, 100, 100, 218));\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: qlineargradient(spread:reflect, x1:1, y1:0.522, x2:1, y2:0, stop:0 rgba(58, 4, 0, 240), stop:0.80597 rgba(161, 100, 100, 218));\n"
            "padding-top: 2px;\n"
            "padding-left: 3px;\n"
            "}\n"
            "QLabel {\n"
            "background-color: qlineargradient(spread:reflect, x1:1, y1:0.522, x2:1, y2:0, stop:0.174129 rgba(15, 0, 0, 255), stop:0.890547 rgba(161, 100, 100, 218));\n"
            "font: 9pt \"Segoe Print\";\n"
            "color: rgb(209, 209, 209);\n"
            "padding: 0px 10px\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "background-color: qlineargradient(spread:reflect, x1:1, y1:0.522, x2:1, y2:0, stop:0.174129 rgba(15, 0, 0, 255), stop:0.890547 rgba(161, 100, 100, 218));\n"
            "font: 9pt \"Segoe Print\";\n"
            "color: rgb(209, 209, 209);\n"
            "padding: 0px 10px;\n"
            "border: 3px solid qlineargradient(spread:reflect, x1:1, y1:0.522, x2:1, y2:0, stop:0 rgba(102, 7, 0, 240), stop:0.80597 rgba(161, 100, 100, 218));\n"
            "}\n"
            "\n"
            ""
        )
        self.windowFrame.setObjectName("windowFrame")

        self.label_matplot_image = QtWidgets.QLabel(self.windowFrame)
        self.label_matplot_image.setGeometry(QtCore.QRect(10, 60, 720, 480))
        self.label_matplot_image.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_matplot_image.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_matplot_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_matplot_image.setText("")
        self.label_matplot_image.setObjectName("label_matplot_image")

        self.pushButton_go = QtWidgets.QPushButton(self.windowFrame)
        self.pushButton_go.setGeometry(QtCore.QRect(540, 550, 181, 28))
        self.pushButton_go.setObjectName("pushButton_go")

        self.pushButton_save = QtWidgets.QPushButton(self.windowFrame)
        self.pushButton_save.setGeometry(QtCore.QRect(540, 590, 181, 28))
        self.pushButton_save.setObjectName("pushButton_save")

        self.label_1 = QtWidgets.QLabel(self.windowFrame)
        self.label_1.setGeometry(QtCore.QRect(20, 550, 170, 30))
        self.label_1.setEnabled(False)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.windowFrame)
        self.label_2.setGeometry(QtCore.QRect(20, 590, 170, 30))
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.windowFrame)
        self.label_3.setGeometry(QtCore.QRect(20, 630, 170, 30))
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")

        self.matplot_widget = QtWidgets.QWidget(self.windowFrame)
        self.matplot_widget.setGeometry(QtCore.QRect(30, 80, 680, 440))
        self.matplot_widget.setStyleSheet("QWidget {\n"
"border-radius: 10px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0.96, y1:1, x2:1, y2:0, stop:0.323383 rgba(89, 79, 79, 198), stop:0.995025 rgba(255, 255, 255, 217));\n"
"border-top: 3px solid rgb(83, 0, 0); \n"
"border-left: 3px solid  rgb(83, 0, 0);\n"
"border-right: 1px solid  rgb(83, 0, 0);\n"
"border-bottom: 1px solid  rgb(83, 0, 0);\n"
"\n"
"}")
        self.matplot_widget.setObjectName("matplot_widget")

        self.plainTextEdit_result = QtWidgets.QPlainTextEdit(self.matplot_widget)
        self.plainTextEdit_result.setGeometry(QtCore.QRect(480, 10, 180, 410))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.plainTextEdit_result.setFont(font)
        self.plainTextEdit_result.setStyleSheet("padding: 5px 10px;\n"
"color: rgb(168, 0, 0);\n"
"selection-background-color: rgb(140, 140, 140);")
        self.plainTextEdit_result.setReadOnly(True)
        self.plainTextEdit_result.setObjectName("plainTextEdit_result")

        self.widget_plot = QtWidgets.QWidget(self.matplot_widget)
        self.widget_plot.setGeometry(QtCore.QRect(10, 10, 441, 411))
        self.widget_plot.setStyleSheet("padding: 20px 20px")
        self.widget_plot.setObjectName("widget_plot")

        self.label_2_input = QtWidgets.QLineEdit(self.windowFrame)
        self.label_2_input.setGeometry(QtCore.QRect(210, 590, 80, 30))
        self.label_2_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2_input.setReadOnly(False)
        self.label_2_input.setMaxLength(5)
        self.label_2_input.setObjectName("label_2_input")

        self.label_1_input = QtWidgets.QLineEdit(self.windowFrame)
        self.label_1_input.setGeometry(QtCore.QRect(210, 550, 80, 30))
        self.label_1_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_1_input.setReadOnly(False)
        self.label_1_input.setMaxLength(5)
        self.label_1_input.setObjectName("label_1_input")

        self.label_3_input = QtWidgets.QLineEdit(self.windowFrame)
        self.label_3_input.setGeometry(QtCore.QRect(210, 630, 80, 30))
        self.label_3_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3_input.setReadOnly(True)
        validator = QtGui.QRegularExpressionValidator(self.label_3_input)
        validator.setRegularExpression(QtCore.QRegularExpression("^[??-??][??-??]{0,6}$}"))
        self.label_3_input.setValidator(validator)
        self.label_3_input.setMaxLength(4)
        self.label_3_input.setObjectName("label_3_input")

        self.label_3.hide()
        self.label_3_input.hide()

        self.header_frame = QtWidgets.QFrame(self.windowFrame)
        self.header_frame.setGeometry(QtCore.QRect(10, 10, 721, 40))
        self.header_frame.setMouseTracking(True)
        self.header_frame.setTabletTracking(True)
        self.header_frame.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.647, fx:0.5, fy:0.5, stop:0.104478 rgba(40, 10, 10, 215), stop:0.880597 rgba(0, 0, 0, 255));")
        self.header_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_frame.setObjectName("header_frame")
        self.titleLabel = QtWidgets.QLabel(self.header_frame)
        self.titleLabel.setGeometry(QtCore.QRect(80, 5, 331, 31))
        self.titleLabel.setMouseTracking(True)
        self.titleLabel.setTabletTracking(True)
        self.titleLabel.setStyleSheet("border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 12pt \"Segoe Print\";\n"
"color: rgb(255, 8, 0);")
        self.titleLabel.setObjectName("titleLabel")
        self.windowButtonsFrame = QtWidgets.QFrame(self.header_frame)
        self.windowButtonsFrame.setGeometry(QtCore.QRect(620, 5, 91, 30))
        self.windowButtonsFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.windowButtonsFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.windowButtonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowButtonsFrame.setObjectName("windowButtonsFrame")

        self.minimizeWindowButton = QtWidgets.QPushButton(self.windowButtonsFrame)
        self.minimizeWindowButton.setGeometry(QtCore.QRect(0, 0, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Wingdings ")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.minimizeWindowButton.setFont(font)
        self.minimizeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeWindowButton.setMouseTracking(True)
        self.minimizeWindowButton.setTabletTracking(True)
        self.minimizeWindowButton.setStyleSheet("color: rgb(255, 8, 0);\n"
"font: 13pt \"Wingdings \";\n"
"")
        self.minimizeWindowButton.setObjectName("minimizeWindowButton")
        self.closeWindowButton = QtWidgets.QPushButton(self.windowButtonsFrame)
        self.closeWindowButton.setGeometry(QtCore.QRect(50, 0, 40, 30))
        self.closeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeWindowButton.setMouseTracking(True)
        self.closeWindowButton.setTabletTracking(True)
        self.closeWindowButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.closeWindowButton.setStyleSheet("color: rgb(255, 8, 0);\n"
"font: 21pt \"Wingdings\";\n"
"border: 1px\n"
"")
        self.closeWindowButton.setCheckable(False)
        self.closeWindowButton.setAutoDefault(False)
        self.closeWindowButton.setObjectName("closeWindowButton")
        self.icon_label = QtWidgets.QLabel(self.header_frame)
        self.icon_label.setGeometry(QtCore.QRect(10, 2, 60, 35))
        self.icon_label.setStyleSheet("border: 0px")
        self.icon_label.setText("")
        self.icon_label.setPixmap(QtGui.QPixmap("images/iconMin.png"))
        self.icon_label.setObjectName("icon_label")

        self.retranslateUi(MatplotlibWindow)
        QtCore.QMetaObject.connectSlotsByName(MatplotlibWindow)

        self.add_functions()

    def retranslateUi(self, MatplotlibWindow):
        _translate = QtCore.QCoreApplication.translate
        MatplotlibWindow.setWindowTitle(_translate("MatplotlibWindow", "Dialog"))
        self.pushButton_go.setText(_translate("MatplotlibWindow", "GO"))
        self.pushButton_save.setText(_translate("MatplotlibWindow", "?????????????????? png"))
        self.label_1.setText(_translate("MatplotlibWindow", "????????????"))
        self.label_2.setText(_translate("MatplotlibWindow", "????????????"))
        self.label_3.setText(_translate("MatplotlibWindow", "?????????????? ??????????????????"))
        self.label_3_input.setText(_translate("MatplotlibWindow", "????"))
        self.plainTextEdit_result.setPlainText(_translate("MatplotlibWindow", ""))
        self.titleLabel.setText(_translate("MatplotlibWindow", "???????????? ???? ??????????????"))
        self.minimizeWindowButton.setText(_translate("MatplotlibWindow", "??"))
        self.closeWindowButton.setText(_translate("MatplotlibWindow", "??"))

    def add_functions(self):
        pass


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MatplotlibWindow = QtWidgets.QDialog()
    ui = Ui_MatplotlibWindow()
    ui.setupUi(MatplotlibWindow)
    MatplotlibWindow.show()
    sys.exit(app.exec_())'''
