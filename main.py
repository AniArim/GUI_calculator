import sys
from pathlib import Path
from PyQt5 import QtGui, QtWidgets
from MainWindow import RootWindow

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


