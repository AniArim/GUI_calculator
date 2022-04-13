
import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from pathlib import Path
import numpy as np
import math

from Figure_2D import Rectangle as Rect
from EnumModule import *
from MatplotlibUi import Ui_MatplotlibWindow

from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.ticker import FixedLocator


class MatplotlibWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        pyplot.cla()  # чтобы не возникали ошибки накладывания осей при повторном вызове.
                        # Чтобы не было ошибки C/C++ с FigureCanvasQTAgg
        self.figure_draw = pyplot.gcf()
        self.figure_draw.clear()
        self.figure_draw.set_facecolor("#e3e3e3")
        self.canvas = FigureCanvasQTAgg(self.figure_draw)
        self.axes = self.figure_draw.add_subplot(111)
        self.layout_vertical = QtWidgets.QVBoxLayout(self)
        self.layout_vertical.addWidget(self.canvas)


class PlotWindow(QtWidgets.QDialog, Ui_MatplotlibWindow):

    def __init__(self, parent=None, figure=None):
        super(PlotWindow, self).__init__(parent)

        self.figure = figure
        self.data_input = {self.figure: {}}
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)  # устанавливаем флаг чтобы удалять окно после закрытия
        self.setWindowIcon(QtGui.QIcon(f"{Path.cwd()/'images'/'icon.png'}"))
        self.switch = False

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.cursorPosition = self.cursor().pos()
        self.windowPosition = self.pos()

    def add_functions(self):
        self.label_1_input.textChanged.connect(lambda: self.lines_got_text(self.label_1_input.text(), self.label_1_input))
        self.label_2_input.textChanged.connect(lambda: self.lines_got_text(self.label_2_input.text(), self.label_2_input))
        self.init_widget()
        self.pushButton_go.clicked.connect(self.plot_widget)
        self.pushButton_save.clicked.connect(self.save_image)

        self.closeWindowButton.clicked.connect(self.closeWindow)
        self.minimizeWindowButton.clicked.connect(self.minimizeWindow)

    def lines_got_text(self, text: str, line: QtWidgets.QLineEdit):
        """
        Метод дополнительной валидации всего вводимого текста, очистка полей для вывода результата.
        
        :param text: текс из любого поля для ввода
        :param line: объект этого поля для ввода
        :return: None
        """
        if text:
            try:
                self.data_input.get(self.figure).update({line.objectName(): float(text)})
            except ValueError:
                if text == ".":
                    line.setText('0.')
                elif "," in text:
                    line.setText(text.replace(",", "."))
        else:
            try:
                self.data_input.get(self.figure).pop(line.objectName())
            except KeyError:
                pass
    
    def init_widget(self):
        
        self.widget = MatplotlibWidget()
        self.layoutvertical = QtWidgets.QVBoxLayout(self.widget_plot)
        self.layoutvertical.addWidget(self.widget)

        
    def plot_rectangle(self):
        """
        Отрисовка прямоугольника и добавление его на axes.
        
        :return: None
        """
        self.widget.radius = self.diagonal/2
        i = ((-self.radius + self.heigth / 2) - (0.5 * self.scaling_)) / 2
        
        self.widget.figure_draw.suptitle(self.figure)  # Название фигуры
        self.widget.axes.axis("equal")  # чтобы круг был кругом, а не элипсом
        self.widget.axes.set(ylim=((-self.radius+self.heigth/2) - math.fabs(i), self.diagonal))  # граничные значения
        self.widget.axes.xaxis.set_major_locator(
            FixedLocator([0, self.weight, self.weight/2]))  # точки: ноль, ширина, центр круга х == радиус точка х
        self.widget.axes.yaxis.set_major_locator(
            FixedLocator([0, self.heigth, self.heigth/2, self.heigth/2+self.widget.radius]))  # точки: ноль, высота, центр круга у, радиус точка у
        
        self.widget.x = (0, self.weight, self.weight, 0, 0)
        self.widget.y = (0, 0, self.heigth, self.heigth, 0)
        self.widget.axes.plot(self.widget.x, self.widget.y, "-o", color="black")

        self.widget.diag_x = (0, self.weight, 0, self.weight)
        self.widget.diag_y = (0, self.heigth, self.heigth, 0)
        self.widget.axes.plot(self.widget.diag_x, self.widget.diag_y, "-o", color="black")

        # Представление окружности параметрическим уравнением
        self.widget.center_x, self.widget.center_y = (self.weight/2, self.heigth/2)
        theta = np.arange(0, 2 * np.pi, 0.01)
        x = self.widget.center_x + self.widget.radius * np.cos(theta)
        y = self.widget.center_y + self.widget.radius * np.sin(theta)
        self.widget.axes.plot(x, y, "black")

        # Отрисовка радиуса
        x = (self.widget.center_x, self.widget.center_x)
        y = (self.widget.center_y, self.widget.center_y + self.widget.radius)
        self.widget.axes.plot(x, y, "r-o")
        
        # расположение букв на рисунке
        self.widget.axes.text(i, 0, "A", fontsize=13, color="r")
        self.widget.axes.text(i, self.heigth, "B", fontsize=13, color="r")
        self.widget.axes.text(self.weight + math.fabs(i)/2, self.heigth, "C", fontsize=13, color="r")
        self.widget.axes.text(self.weight + math.fabs(i)/2, 0, "D", fontsize=13, color="r")
        self.widget.axes.text((self.weight/2), ((self.heigth/2+self.widget.radius) + math.fabs(i)/2), "R", fontsize=13, color="r")

        self.widget.axes.set_facecolor("#e3e3e3")
        self.widget.axes.grid()
        
    def scaling(self, number_x: (int, float), number_y: (int, float)):
        """
        Для корректного масштабирования осей и букв на рисунке  необходимо знать количество десятков во входных данных.
        Возвращаем максимальное значение - цифру для умножения при рассчете масштабирования.
        
        :param number_x: ширина из label_1_input
        :param number_y: высота из label_2_input
        :return: максимальное количество десятков во входных данных
        """
        len_x = len(str(number_x).partition(".")[0])
        len_y = len(str(number_y).partition(".")[0])
        i = max(len_x, len_y)
        self.scaling_ = 1 if i <= 1 else 10 ** (i - 1)
        return self.scaling_

    def plot_widget(self):
        """
        Метод очищает axes для добавления фигуры по новым параметрам.
        Производим рассчеты:  класса фигуры ( Rectangle для прямоугольника) из модуля Figure_2D.
        Добавляет в plainTextEdit_result рассчеты по входным данным.
        Вызывает метод отрисовки фигуры.
        
        :return: None
        """
        
        self.widget.axes.clear()  # очищаем оси для отрисовки фигуры с измененными параметрами в уже активном окне.
        
        if self.figure == FigureNames.rectangle.value:
            
            self.heigth = self.data_input.get(self.figure).get("label_1_input")
            self.weight = self.data_input.get(self.figure).get("label_2_input")
            
            if self.weight and self.heigth:

                self.scaling_ = self.scaling(self.weight, self.heigth)
                temp = {
                    "lineEdit_page1_line1_input": self.heigth,
                    "lineEdit_page1_line2_input": self.weight
                    }
                self.diag = Rect(RectangleWhatsearchVariant.diagonal.value, temp, RectangleDiagFormulas.pythagoras)
                self.perimeter = Rect(RectangleWhatsearchVariant.perimeter.value, temp, RectanglePerimeterFormulas.sides)
                self.square = Rect(RectangleWhatsearchVariant.square.value, temp, RectangleSquareFormulas.sides)

                self.diagonal = float(self.diag.result())
                self.radius = self.diagonal/2
                
                self.plainTextEdit_result.setPlainText(f"Радиус:\n R = {self.radius}\n"
                                                       f"Диагональ:\n AC = BD = 2R = {self.diag.result()}\n"
                                                       f"Площадь:\n S = {self.square.result()}\n"
                                                       f"Периметр:\n P = {self.perimeter.result()}")
                
                self.plot_rectangle()
                self.switch = True  # меняем значение False для корректной работы сохранения png
                self.widget.canvas.draw()
            else:
                pass
    
    def save_image(self):
        """
        Метод генерирует путь к рабочему столу, сохраняет отрисованное изображение, если холст не пустой.
        Изображение в формате png с прозрачным фоном и обрезаной рамкой.
        
        :return: None
        """
        if self.switch:
            self.filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget_plot,
                                    'Save File',
                                    f"{Path.home()/'Desktop'}",
                                    "Images (*.png)")
            
            self.widget.figure_draw.savefig(
                self.filename, dpi=1000, transparent=True, bbox_inches='tight')  # сохранение изображения в файл
        else:
            pass

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
    
