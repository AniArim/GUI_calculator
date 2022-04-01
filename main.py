"""
Copyright font Laptev_Brush.otf: Copyright (c) 2018 by Todor Georgiev. All rights reserved.
license for font: commercial and personal usage
"""

import sys
from pathlib import Path
from PyQt5 import QtGui, QtWidgets
from MainWindow import RootWindow
import source


try:
    from PyQt5.QtWinExtras import QtWin
    # для корректного изображения иконки в панели рабочего стола
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

app = QtWidgets.QApplication(sys.argv)
#id = QtGui.QFontDatabase.addApplicationFont(f"{Path.cwd()/'fonts'/'Laptev_Brush.otf'}")

app.setWindowIcon(QtGui.QIcon(f'{Path.cwd()/"images"/"icon.png"}'))

ui = RootWindow()
ui.setupUi(ui)

'''if id == 0:
    ui.fontName = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
    ui.font = QtGui.QFont(ui.fontName, 12)
    print(ui.font)
elif id == -1:
    raise FileNotFoundError("Шрифт 'Laptev_Brush.otf' не установлен")'''
ui.show()

sys.exit(app.exec_())


