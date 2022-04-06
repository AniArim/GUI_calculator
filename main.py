"""
Copyright font Laptev_Brush.otf: Copyright (c) 2018 by Todor Georgiev. All rights reserved.
license for font: commercial and personal usage
"""

import sys
from pathlib import Path
from PyQt5 import QtGui, QtWidgets, QtCore
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

app.setWindowIcon(QtGui.QIcon(f'{Path.cwd()/"images"/"icon.png"}'))

ui = RootWindow()
ui.setupUi(ui)
ui.show()

sys.exit(app.exec_())


