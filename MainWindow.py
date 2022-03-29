
from Figure_2D import Rectangle
from MatplotlibWindow import PlotWindow
from EnumModule import *
from MainWindowUi import Ui_MainWindow
from ErrorWindow import ErrorDialog

from pathlib import Path
from PyQt5 import QtGui, QtWidgets


class RootWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(RootWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(f"{Path.cwd() / 'images' / 'icon.png'}"))

        self.html = ""

        # Словарь изображений для фигур
        self.png_data = {"Прямоугольник": "rectangle.png", "Параллелограмм": "parallelogram.png",
                         "Квадрат": "square.png",
                         "Ромб": "rhombus.png", "Трапеция равнобедренная": "trapezium1.png",
                         "Трапеция прямоугольная": "trapezium2.png",
                         "Треугольник": "triangle.png", "Шестиугольник": "6-polygon.png", "Окружность": "circle.png",
                         "Призма": "prism.png", "Параллелепипед": "cuboid.png", "Куб": "cube.png",
                         "Пирамида": "pyramid.png",
                         "Цилиндр круговой": "cylinder.png", "Конус круговой": "cone.png", "Шар, сфера": "sphere.png"}

        # Словарь плоских и объемных фигур
        self.figure_list = (
            ("Прямоугольник", "Параллелограмм", "Квадрат", "Ромб", "Трапеция равнобедренная", "Трапеция прямоугольная",
             "Треугольник", "Шестиугольник", "Окружность"),
            ("Призма", "Параллелепипед", "Куб", "Пирамида", "Цилиндр круговой", "Конус круговой", "Шар, сфера")
        )
        # Словарь что возможно вычислить для различных фигур
        self.whatsearch_variants = {
            "Прямоугольник": (
                "Что нужно найти?", "Стороны", "Диагональ", "Периметр", "Площадь", "Окружность описанная вокруг",
                "Угол между стороной и диагональю", "Угол между диагоналями")
        }

        # Словарь вводных данных для рассчетов
        self.input_data = {
            "Прямоугольник": ("Сторона", "Диаметр", "Диагональ", "Площадь", "Периметр", "Угол α", "Угол β")
        }

        # Словарь рассчетов для разных фигур
        self.output_data = {
            "Прямоугольник": ("Диагональ", "Сторона a", "Угол α", "Площадь", "Угол β", "Периметр",
                              "Сторона  b", "Радиус")
        }

        # Список Figure_2D_box.Items
        self.Figure_2D_box_items = ("figure_2D", "rectangle", "parallelogram", "square", "rhombus", "trapezoid_1",
                                    "trapezoid_2", "triangle", "hexagon", "circle")

        # Список Figure_3D_box.Items
        self.Figure_3D_box_items = ("figure_3D", "prism", "parallelepiped", "cube", "pyramid", "cylinder", "cone",
                                    "sphere")
    
    def add_functions(self):
        self.switch_left.clicked.connect(lambda: self.switched(self.switch_left.text()))
        self.switch_right.clicked.connect(lambda: self.switched(self.switch_right.text()))
        
        self.Figure_2D_box.currentIndexChanged.connect(lambda: self.updateQComboBoxFigure(self.Figure_2D_box, self.Figure_2D_box_items))
        self.Figure_3D_box.currentIndexChanged.connect(lambda: self.updateQComboBoxFigure(self.Figure_3D_box, self.Figure_3D_box_items))
        
        self.Box_whatsearch.currentIndexChanged.connect(self.box_whatsearch_clicked)
        
        self.lineEdit_page1_line1_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line1_input.text(), self.lineEdit_page1_line1_input))
        self.lineEdit_page1_line2_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line2_input.text(), self.lineEdit_page1_line2_input))
        self.lineEdit_page1_line3_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line3_input.text(), self.lineEdit_page1_line3_input))
        self.lineEdit_page1_line4_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line4_input.text(), self.lineEdit_page1_line4_input))
        self.lineEdit_page1_line5_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line5_input.text(), self.lineEdit_page1_line5_input))
        self.lineEdit_page1_line6_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line6_input.text(), self.lineEdit_page1_line6_input))
        self.lineEdit_page1_line7_input.textChanged.connect(lambda: self.lines_got_text(self.lineEdit_page1_line7_input.text(), self.lineEdit_page1_line7_input))
        self.Box_whatsearch.currentIndexChanged.connect(lambda: self.clear_lines(self.page2_lines))
        self.paint_figure.clicked.connect(lambda: self.show_matplotlib_window(self.figure))
        self.Calculate.clicked.connect(self.calculate_result)

    def add_html_text(self, name):
        """
        Метод считывает разметку и текст из файла name.txt и добавляет в self.text_descriptions
        
        :param name: название файла с разметкой HTML в директории text_HTML
        :return: None
        """
        path_file = Path.cwd()/'text_HTML'/f'{name}.txt'
        try:
            with open(f"{path_file}", "r", encoding="utf-8") as file:
                for line in file:
                    self.html += line
            self.text_descriptions.setHtml(self._translate("MainWindow", f"{self.html}"))

        except IOError:
            pass

    def switched(self, text):
        """
        Метод переключения страниц объекта self.stackedWidget_func
        
        :param text: символ 'влево' или 'вправо'
        :return: None
        """
        index = self.stackedWidget_func.currentIndex()
        if text == "◄":
            if index == 0:
                self.stackedWidget_func.setCurrentIndex(2)
            elif index == 1:
                self.stackedWidget_func.setCurrentIndex(0)
            elif index == 2:
                self.stackedWidget_func.setCurrentIndex(1)
        else:
            if index == 0:
                self.stackedWidget_func.setCurrentIndex(1)
            elif index == 1:
                self.stackedWidget_func.setCurrentIndex(2)
            elif index == 2:
                self.stackedWidget_func.setCurrentIndex(0)

    def clear_lines(self, args):
        """
        Рекурсивный метод очистки входных данных.
        
        :param args: кортеж или список с вложениями или без
        :return: None
        """
        for index in range(len(args)):
            if isinstance(args[index], (tuple, list)):
                self.clear_lines(args[index])
            else:
                for i in args:
                    i.setText(self._translate("MainWindow", ""))
    
    def box_whatsearch_clicked(self):
        """
        Обработка событий в поле "Что ищем?"
        :return:  None
        """

        if self.Box_whatsearch.currentIndex() == 0:  # Если "Что ищем?", тогда текст сбрасывается
            self.groupBox_pageInput.setEnabled(False)  # Выключаем кликабельность бокса для ввода параметров
            # Очищаем поля с параметрами поиска и ввода пользователя
            self.clear_lines(self.page1_lines)
            
        if self.figure == self.figure_list[0][0]:  # Прямоугольник
            if self.Box_whatsearch.currentIndex() != 0:
                self.clear_lines(self.page1_lines)
                self.groupBox_pageInput.setEnabled(True)  # включаем бокс для ввода данных
                for i in self.page1_lines[1]:  # кликабельность полей для ввода данных
                    i.setEnabled(True)
                
                j = 0
                for i in self.page1_lines[0]:  # установка стандартного текста для полей наименований параметров для поиска
                    i.setText(self._translate("MainWindow", self.input_data.get(self.figure)[j]))
                    j += 1
                # Изменение текста и видимости в полях в зависимости от того, что ищем
                if self.Box_whatsearch.currentIndex() == 2:
                    self.lineEdit_page1_line1.setText("Сторона a")
                    self.lineEdit_page1_line2.setText("Сторона b")
                    self.lineEdit_page1_line3.setText("Радиус")
                elif self.Box_whatsearch.currentIndex() == 3:
                    self.lineEdit_page1_line1.setText("Сторона a")
                    self.lineEdit_page1_line2.setText("Сторона b")
                    self.lineEdit_page1_line3.setText("Диагональ")
                    self.lineEdit_page1_line5.setText("Радиус")
                    self.lineEdit_page1_line6.setText("")
                    self.lineEdit_page1_line6_input.setEnabled(False)
                    self.lineEdit_page1_line7.setText("")
                    self.lineEdit_page1_line7_input.setEnabled(False)
                elif self.Box_whatsearch.currentIndex() == 4:
                    self.lineEdit_page1_line1.setText("Сторона a")
                    self.lineEdit_page1_line2.setText("Сторона b")
                    self.lineEdit_page1_line4.setText("Радиус")
                    self.lineEdit_page1_line6.setText("Угол β")
                    self.lineEdit_page1_line7.setText("")
                    self.lineEdit_page1_line7_input.setEnabled(False)
                elif self.Box_whatsearch.currentIndex() == 5:
                    self.lineEdit_page1_line1.setText("Сторона a")
                    self.lineEdit_page1_line2.setText("Сторона b")
                elif self.Box_whatsearch.currentIndex() == 6:
                    self.lineEdit_page1_line1.setText("Сторона a")
                    self.lineEdit_page1_line2.setText("Сторона b")
                    self.lineEdit_page1_line4.setText("Угол β")
                    self.lineEdit_page1_line5_input.setEnabled(False)
                    self.lineEdit_page1_line5.setText("")
                    self.lineEdit_page1_line6_input.setEnabled(False)
                    self.lineEdit_page1_line6.setText("")
                    self.lineEdit_page1_line7_input.setEnabled(False)
                    self.lineEdit_page1_line7.setText("")
                elif self.Box_whatsearch.currentIndex() == 7:
                    self.lineEdit_page1_line1.setText("Площадь")
                    self.lineEdit_page1_line2.setText("Диагональ")
                    self.lineEdit_page1_line3.setText("Угол α")
                    self.lineEdit_page1_line4_input.setEnabled(False)
                    self.lineEdit_page1_line4.setText("")
                    self.lineEdit_page1_line5_input.setEnabled(False)
                    self.lineEdit_page1_line5.setText("")
                    self.lineEdit_page1_line6_input.setEnabled(False)
                    self.lineEdit_page1_line6.setText("")
                    self.lineEdit_page1_line7_input.setEnabled(False)
                    self.lineEdit_page1_line7.setText("")
                    
    def updateQComboBoxFigure(self, box_object, tuple_of_box_items):
        """
        На странице Input и Output выводим значение фигуры, с которой будем работать, в зависимости от того, что выберет
        user.
        Если фигура не выбрана, виджет для ввода и вывода информации не кликабелен. Очищаем главное окно  с изображением.
        И устанавливаем gif.
        Если фигура выбрана, виджет для ввода, вывода и описания кликабелен. Не кликабельным остается поле для ввода
        данных до тех пор, пока пользователь не выберет, что именно нужно найти для выбранной фигуры. Создаем объект
        фигуры с которой будем работать. Очищаем переменную с данными о описании свойств фигуры. Добавляем описание
        свойств для нвыбранной фигуры.
        
        :return: None
        """
        self.plainTextEdit_figure_input.setPlainText(box_object.currentText())
        self.plainTextEdit_figure_output.setPlainText(box_object.currentText())
        
        if box_object.currentIndex() == 0:
            self.Box_formulas.setEnabled(False)
            self.Box_whatsearch.setCurrentText("Что нужно найти?")
            self.label_image.clear()
            self.label_image.setMovie(self.gif)
        else:
            self.Box_formulas.setEnabled(True)
            self.groupBox_pageInput.setEnabled(False)
            self.func_figure(box_object.currentText())
            self.update_image(self.plainTextEdit_figure_input.toPlainText())
            
            self.figure = self.plainTextEdit_figure_input.toPlainText()  # фигура с которой будем работать
            self.data_figure_values_input = {self.figure: {}}  # Создаем словарь в котором обновляем данные после ввода
            # пользователем в lines_got_text(self, text, line)
            
            self.html = ""
            self.add_html_text(tuple_of_box_items[box_object.currentIndex()])  # берем название файла
            # из списка Figure_2D_box_items по текущему индексу Figure_3D_box

    def func_figure(self, figure):
        if figure == self.figure_list[0][0]:
            # Отображаем варианты для поиска. для выбранной фигуры. figure == self.figure
            for i in range(8):
                self.Box_whatsearch.setItemText(i, self._translate("MainWindow", self.whatsearch_variants.get(figure)[i]))

    def lines_got_text(self, text, line):
        """
        Обновление словаря с входными данными в self.data_figure_values_input. Скрываем все поля для вывода на странице
        Output. очищаем поле для выввода информации о функции, которая была задействована для вычислений.
        Дополнительная валидация вводных данных. Запятая в тексте изменятся на точку. Точка в начале текста изменяется
        на ноль с точкой. Если поле очищается - пары ключ:значение удаляются из словаря.
        
        :param text: текс из любого поля для ввода
        :param line: объект этого поля для ввода
        :return: None
        """
        if text:
            try:
                self.data_figure_values_input.get(self.figure).update({line.objectName(): float(text)})
                self.clear_lines(self.page2_lines)
                self.hide_lineEdit_page2(1)
                self.hide_lineEdit_page2(2)
                self.plainTextEdit_page2_about_result.setPlainText("")
            except ValueError:
                if text == ".":
                    line.setText('0.')
                elif "," in text:
                    line.setText(text.replace(",", "."))
        else:
            try:
                self.data_figure_values_input.get(self.figure).pop(line.objectName())
            except KeyError:
                pass

    def calculate_result(self):
        if not self.groupBox_pageInput.isEnabled():
            pass
        else:
            self.make_calculations()

    def page2_line1_placement(self, functionVariant: enum.Enum):

        self.result = Rectangle(self.Box_whatsearch.currentIndex(),
                                self.data_figure_values_input.get(self.figure), functionVariant)
        if self.result.result():
            self.lineEdit_page2_line1_out.setText(f"{self.result.result()}")
            self.plainTextEdit_page2_about_result.setPlainText(functionVariant.name)
        else:
            return

    def page2_two_lines_placement(self, functionVariant: RectangleSidesFormulas):
        self.result = Rectangle(self.Box_whatsearch.currentIndex(),
                                self.data_figure_values_input.get(self.figure), functionVariant)
        if self.result.result():
            self.sideA, self.sideB = self.result.result()
            self.lineEdit_page2_line1.setText("Сторона a")
            self.lineEdit_page2_line2.setText("Сторона b")

            self.lineEdit_page2_line1_out.setText(f"{self.sideA}")
            self.lineEdit_page2_line2_out.setText(f"{self.sideB}")
            self.plainTextEdit_page2_about_result.setPlainText(functionVariant.name)
            return self.stackedWidget_func.setCurrentIndex(1), self.show_lineEdit_page2(1), \
                   self.show_lineEdit_page2(2)
        else:
            return

    def check_page1_input_for_line(self, lineIndex: int):
        return self.temp_values.get(f'lineEdit_page1_line{lineIndex}_input')

    def check_page1_inputs_for_lines(self, firstLineIndex: int, secondLineIndex: int):
        return self.temp_values.get(f'lineEdit_page1_line{firstLineIndex}_input') \
               and self.temp_values.get(f'lineEdit_page1_line{secondLineIndex}_input')

    def check_page1_inputs_for_line_or_line(self, firstLineIndex: int, secondLineIndex: int):
        return self.temp_values.get(f'lineEdit_page1_line{firstLineIndex}_input') \
               or self.temp_values.get(f'lineEdit_page1_line{secondLineIndex}_input')

    def make_calculations(self):
        """
        Если все поля пустые, то для любой фигуры выдаем ошибку, если нет, выполняется блок проверки для каждой
        фигуры, входных данных для поиска параметра для конкретной фигуры по ряду функций.  Если все данные введены корректно,
        создаем объект класса фигуры, наследуемый от Figure_2D. Получаем результат в зависимости от введенных
        данных (различные функции для каждого способа). Результат - self.result.<parameter>, где <parameter> - это
        название переменной, где хранится функция вычисления. Результат передаем на страницу вывода результатов
        :return:  self.show_lineEdit_page2(1) метод отображения полей для вывода результата,
        self.stackedWidget_func.setCurrentIndex(1) - переключаем страницу с Input на Output
        """

        if self.figure:
            self.temp_values = self.data_figure_values_input.get(self.figure)  # достаем список введенных данных

            if not self.temp_values:
                self.error_message_show(text="Пустые поля, что считать то будем?",
                                        details="Тут могли бы быть функции...")
            else:
                """Блок проверки """
                if self.figure == "Прямоугольник":
                    if self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.sides.value:
                        self.lineEdit_page2_line1.setText("Сторона")

                        if self.check_page1_inputs_for_lines(1, 3):
                            self.page2_line1_placement(RectangleSidesFormulas.diagonalAndSide)

                        elif self.check_page1_inputs_for_lines(1, 4):
                            self.page2_line1_placement(RectangleSidesFormulas.squareAndSide)

                        elif self.check_page1_inputs_for_lines(1, 5):
                            self.page2_line1_placement(RectangleSidesFormulas.perimeterAndSide)

                        elif self.check_page1_inputs_for_lines(2, 6) or self.check_page1_inputs_for_lines(3, 6):
                            return self.page2_two_lines_placement(RectangleSidesFormulas.diameterAndAngleA)
                            
                        elif self.check_page1_inputs_for_lines(2, 7) or self.check_page1_inputs_for_lines(3, 7):
                            return self.page2_two_lines_placement(RectangleSidesFormulas.diameterAndAngleB)
                            
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формулы стороны прямоугольника (длины и ширины прямоугольника) через:\n"
                                                             " 1.Диагональ и другую сторону\n"
                                                             "2. Площадь и другую сторону\n"
                                                             "3. Периметр и другую сторону\n"
                                                             "4-5. Через диаметр и угол α или угол β")
                            return
                            
                    elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.diagonal.value:
                        self.lineEdit_page2_line1.setText("Диагональ")
                        
                        if self.check_page1_inputs_for_lines(1, 2):
                            self.page2_line1_placement(RectangleDiagFormulas.pythagoras)

                        elif self.check_page1_input_for_line(4) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleDiagFormulas.squareAndSide)
                        
                        elif self.check_page1_input_for_line(5) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleDiagFormulas.perimeterAndSide)
                        
                        elif self.check_page1_input_for_line(3):
                            self.page2_line1_placement(RectangleDiagFormulas.radius)
                        
                        elif self.check_page1_inputs_for_lines(1, 6):
                            self.page2_line1_placement(RectangleDiagFormulas.angleAAndSideA)
                        
                        elif self.check_page1_inputs_for_lines(2, 6):
                            self.page2_line1_placement(RectangleDiagFormulas.angleAAndSideB)
                        
                        elif self.check_page1_inputs_for_lines(4, 7):
                            self.page2_line1_placement(RectangleDiagFormulas.angleBAndSquare)
                        
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формула диагонали прямоугольника через:\n"
                                                                " 1.Две стороны прямоугольника (через теорему Пифагора)\n"
                                                                "2. Площадь и любую сторону\n"
                                                                "3. Периметр и любую сторону\n"
                                                                "4. Радиус/диаметр описанной окружности\n"
                                                                "5. Синус угла, прилегающего к диагонали, и длину стороны противоположной этому углу\n"
                                                                "6. Косинус угла, прилегающего к диагонали, и длину стороны прилегающей к этому углу\n"
                                                                "7. Синус острого угла между диагоналями и площадью прямоугольника")
                            return
                        
                    elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.perimeter.value:  # Периметр
                        self.lineEdit_page2_line1.setText("Периметр")

                        if self.check_page1_inputs_for_lines(1, 2):
                            self.page2_line1_placement(RectanglePerimeterFormulas.sides)

                        elif self.check_page1_input_for_line(4) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectanglePerimeterFormulas.squareAndSide)
                            
                        elif self.check_page1_input_for_line(3) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectanglePerimeterFormulas.diagonalAndSide)
                            
                        elif self.check_page1_input_for_line(5) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectanglePerimeterFormulas.radiusAndSide)
                            
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формула периметра прямоугольника через:\n"
                                                            " 1.Две стороны прямоугольника\n"
                                                            "2. Площадь и любую сторону\n"
                                                            "3. Диагональ и любую сторону\n"
                                                            "4. Радиус/диаметр описанной окружности и любую сторону\n")
                            return
                        
                    elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.square.value:  # Площадь
                        self.lineEdit_page2_line1.setText("Площадь")

                        if self.check_page1_inputs_for_lines(1, 2):
                            self.page2_line1_placement(RectangleSquareFormulas.sides)
                            
                        elif self.check_page1_input_for_line(5) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleSquareFormulas.perimeterAndSide)
                            
                        elif self.check_page1_input_for_line(3) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleSquareFormulas.diagonalAndSide)
                            
                        elif self.check_page1_inputs_for_lines(3, 6):
                            self.page2_line1_placement(RectangleSquareFormulas.angleBAndDiagonal)

                        elif self.check_page1_input_for_line(4) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleSquareFormulas.radiusAndSide)
                            
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формула площади прямоугольника через:\n"
                                                                "1.Две стороны прямоугольника\n"
                                                                "2. Периметр и любую сторону\n"
                                                                "3. Диагональ и любую сторону\n"
                                                                "4. Диагональ и синус острого угла между диагоналями\n"
                                                                "5. Радиус/диаметр описанной окружности и любую сторону\n")
                            return
                            
                    elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.radius.value:  # Окружность описанная вокруг
                        self.lineEdit_page2_line1.setText("Радиус окружности")

                        if self.check_page1_inputs_for_lines(1, 2):
                            self.page2_line1_placement(RectangleRadiusFormulas.sides)
                            
                        elif self.check_page1_input_for_line(5) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleRadiusFormulas.perimeterAndSide)
                            
                        elif self.check_page1_input_for_line(4) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleRadiusFormulas.squareAndSide)
                            
                        elif self.check_page1_input_for_line(3):
                            self.page2_line1_placement(RectangleRadiusFormulas.diagonal)
                            
                        elif self.check_page1_inputs_for_lines(1, 6):
                            self.page2_line1_placement(RectangleRadiusFormulas.angleAAndSideA)
                            
                        elif self.check_page1_inputs_for_lines(2, 7):
                            self.page2_line1_placement(RectangleRadiusFormulas.angleBAndSideA)
                            
                        elif self.check_page1_inputs_for_lines(4, 7):
                            self.page2_line1_placement(RectangleRadiusFormulas.angleBAndSquare)
                            
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формула радиуса окружности описанной вокруг прямоугольника через:\n"
                                                                "1.Две стороны прямоугольника\n"
                                                                "2. Периметр и любую сторону\n"
                                                                "3. Площадь и любую сторону\n"
                                                                "4. Диагональ\n"
                                                                "5. Синус угла, прилегающего к диагонали, и длину стороны противоположной этому углу\n"
                                                                "6. Косинус угла, прилегающего к диагонали, и длину стороны прилегающей к этому углу\n"
                                                                "7. Синус острого угла между диагоналями и площадью прямоугольника\n")
                            return
                            
                    elif self.Box_whatsearch.currentIndex() == RectangleAngleAFormulas.value:  # Угол между стороной и диагональю прямоугольника
                        self.lineEdit_page2_line1.setText("Угол α")
                        
                        if self.check_page1_input_for_line(3) and self.check_page1_inputs_for_line_or_line(1, 2):
                            self.page2_line1_placement(RectangleAngleAFormulas.diagonalAndSide)
                            
                        elif self.check_page1_input_for_line(4):
                            self.page2_line1_placement(RectangleAngleAFormulas.angleB)
                            
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формула определения угла между стороной и диагональю прямоугольника через:\n"
                                                            "1.Диагональ и любую сторону\n"
                                                            "2. Угол между диагоналями\n")
                            return
                        
                    elif self.Box_whatsearch.currentIndex() == RectangleAngleBFormulas.value:  # угол между диагоналями прямоугольника
                        self.lineEdit_page2_line1.setText("Угол β")
                        
                        if self.check_page1_input_for_line(3):
                            self.page2_line1_placement(RectangleAngleBFormulas.angleA)
                        
                        elif self.check_page1_inputs_for_lines(1, 2):
                            self.page2_line1_placement(RectangleAngleBFormulas.squareAndDiagonal)
                            
                        else:
                            self.error_message_show(text="Неправильно введены данные! Смотри детали",
                                                    details="Формула определения угла между диагоналями прямоугольника через:\n"
                                                            "1.Угол между стороной и диагональю\n"
                                                            "2. Площадь и диагональ\n")
                            return

                    return self.show_lineEdit_page2(1), self.stackedWidget_func.setCurrentIndex(1)
    
    def show_lineEdit_page2(self, line: int):
        if line == 1:
            self.lineEdit_page2_line1.setHidden(False)
            self.lineEdit_page2_line1_out.setHidden(False)
        elif line == 2:
            self.lineEdit_page2_line2.setHidden(False)
            self.lineEdit_page2_line2_out.setHidden(False)
    
    def hide_lineEdit_page2(self, line: int):
        if line == 1:
            self.lineEdit_page2_line1.setHidden(True)
            self.lineEdit_page2_line1_out.setHidden(True)
        elif line == 2:
            self.lineEdit_page2_line2.setHidden(True)
            self.lineEdit_page2_line2_out.setHidden(True)
        
    @staticmethod
    def error_message_show(text="", details=""):
        #global ErrorDialog
    
        ui = ErrorDialog(text=text, details=details)
        print(ui)
        ui.setupUi(ui)
        ui.show()
        
        ui.btn_ok.clicked.connect(lambda: ui.btn_clicked(ui.btn_ok.text(), ui))
        ui.btn_details.clicked.connect(lambda: ui.btn_clicked(ui.btn_details.text(), ui))

    @staticmethod
    def show_matplotlib_window(fig):
        #global PlotWindow  # класс объявляем глобальным чтобы окно не закрывалось сразу после открытия
        # ToDo разобраться с фигурой по возможности уйти от глобал
        ui = PlotWindow(figure=fig)
        print(ui)
        ui.setupUi(ui)
        ui.show()

    def update_image(self, figure: str):
        """
        Очищаем виджет с изображением в левой части окна. Добавляет изображение для выбранной фигуры
        
        :param figure: текст из self.plainTextEdit_figure_input
        :return: None
        """
        path = Path.cwd()/'images'/'figures'/f'{self.png_data.get(figure)}'
        self.label_image.clear()
        self.label_image.setPixmap(QtGui.QPixmap(f"{path}"))
        


