
from pathlib import Path

from PyQt5 import QtGui, QtWidgets

from EnumModule import *
from ErrorWindow import ErrorDialog
from Figure_2D import Rectangle
from MainWindowUi import Ui_MainWindow
from MatplotlibWindow import PlotWindow


class RootWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(RootWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(f"{Path.cwd() / 'images' / 'icon.png'}"))
        self.html = ""
        self.titles_for_parameters_in_lines_page1 = {
            FigureNames.rectangle.value: {
                RectangleWhatsearchVariant.whatsearch.value: "",
                RectangleWhatsearchVariant.sides.value: ("Сторона", "Диаметр", "Диагональ", "Площадь", "Периметр", "Угол α", "Угол β"),
                RectangleWhatsearchVariant.diagonal.value: ("Сторона a", "Сторона b", "Радиус", "Площадь", "Периметр", "Угол α", "Угол β"),
                RectangleWhatsearchVariant.perimeter.value: ("Сторона a", "Сторона b", "Диагональ", "Площадь", "Периметр", "Радиус"),
                RectangleWhatsearchVariant.square.value: ("Сторона a", "Сторона b", "Диагональ", "Радиус", "Периметр", "Угол β"),
                RectangleWhatsearchVariant.radius.value: ("Сторона a", "Сторона b", "Диагональ", "Площадь", "Периметр", "Угол α", "Угол β"),
                RectangleWhatsearchVariant.angleA.value: ("Сторона a", "Сторона b", "Диагональ", "Угол β"),
                RectangleWhatsearchVariant.angleB.value: ("Площадь", "Диагональ", "Угол α")
                            },
            FigureNames.parallelogram.value: {
                0: ""
                               },
            FigureNames.square.value: {
                0: ""
                        },
            FigureNames.rhombus.value: {
                0: ""
                    },
            FigureNames.trapezium1.value: {
                0: ""
                    },
            FigureNames.trapezium2.value: {
                0: ""
                    },
            FigureNames.triangle.value: {
                0: ""
                    },
            FigureNames.hexagon.value: {
                0: ""
                    },
            FigureNames.circle.value: {
                0: ""
                    },
            FigureNames.prism.value: {
                0: ""
                    },
            FigureNames.cuboid.value: {
                0: ""
                            },
            FigureNames.cube.value: {
                0: ""
                    },
            FigureNames.pyramid.value: {
                0: ""
                        },
            FigureNames.cylinder.value: {
                0: ""
                                },
            FigureNames.cone.value: {
                0: ""
                                },
            FigureNames.sphere.value: {
                0: ""
                            }
        }

    def add_functions(self):

        self.switch_left.clicked.connect(lambda: self.switched(self.switch_left.text()))
        self.switch_right.clicked.connect(lambda: self.switched(self.switch_right.text()))
        
        self.Figure_2D_box.currentIndexChanged.connect(lambda: self.updateQComboBoxFigure(self.Figure_2D_box))
        self.Figure_3D_box.currentIndexChanged.connect(lambda: self.updateQComboBoxFigure(self.Figure_3D_box))
        
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
        
        :param name: название файла без расширения с разметкой HTML в директории text_HTML
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

    def setText_setVisibility_to_page1_lines(self, enum_key: int):
        """
        TODO добавить описание
        :param enum_key:
        :return:
        """
        index = 0
        titles = self.titles_for_parameters_in_lines_page1.get(self.figure).get(enum_key)

        for title in titles:
            self.page1_lines[0][index].setText(title)
            index += 1

        for index, line in enumerate(self.page1_lines[0]):
            equal_line_input = self.page1_lines[1][index]

            if not line.text():
                line.setEnabled(False)
                line.setHidden(True)
                equal_line_input.setEnabled(False)
                equal_line_input.setHidden(True)
            else:
                line.setHidden(False)
                equal_line_input.setEnabled(True)
                equal_line_input.setHidden(False)

    def box_whatsearch_clicked(self):
        """
        Обработка событий в поле "Что ищем?"
        :return:  None
        """

        if self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.whatsearch.value:  # Если "Что ищем?", тогда текст сбрасывается
            self.groupBox_pageInput.setEnabled(False)  # Выключаем кликабельность бокса для ввода параметров
            self.clear_lines(self.page1_lines)  # Очищаем поля с параметрами поиска и ввода пользователя
            self.text_label_input.setText("Выберите параметр для поиска.")  # Устанавливаем дефолтное значение
            self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.whatsearch.value)
        else:
            self.text_label_input.setText("Вводные данные, которые известны:")
            self.clear_lines(self.page1_lines)
            self.groupBox_pageInput.setEnabled(True)  # включаем бокс для ввода данных
            
            if self.figure == FigureNames.rectangle.value:
                # Изменение текста в полях и видимости полей в зависимости от того, что ищем
                if self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.sides.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.sides.value)

                elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.diagonal.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.diagonal.value)

                elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.perimeter.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.perimeter.value)

                elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.square.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.square.value)

                elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.radius.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.radius.value)

                elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.angleA.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.angleA.value)

                elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.angleB.value:
                    self.setText_setVisibility_to_page1_lines(RectangleWhatsearchVariant.angleB.value)
            else:
                pass

    def updateQComboBoxFigure(self, box_object: QtWidgets.QComboBox):
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

        self.figure = self.plainTextEdit_figure_input.toPlainText() or None  # фигура с которой будем работать
        self.data_figure_values_input = {self.figure: {}}  # Создаем словарь в котором обновляем данные после ввода
        # пользователем в lines_got_text(self, text, line)
        self.html = ""
        self.text_descriptions.setHtml(self._translate("MainWindow", f"{self.html}"))
        
        if box_object.currentIndex() == 0:
            self.Box_formulas.setEnabled(False)
            self.Box_whatsearch.setCurrentText("Что нужно найти?")
            self.label_image.clear()
            self.label_image.setMovie(self.gif)

        else:
            self.Box_formulas.setEnabled(True)
            self.groupBox_pageInput.setEnabled(False)
            self.func_figure(box_object.currentText())
            self.update_image()

            file_name = FigureNames(FigureNames.keyForValue(self.figure)).name
            self.add_html_text(file_name)

    def func_figure(self, figure):
        """
        If figure >> object Box_whatsearch adding Item from self.whatsearch_variants.
        If not figure >> object Box_whatsearch clearing themself (delete all Items), adding title
        :param figure: self.figure
        :return: None
        """
        if figure == FigureNames.rectangle.value:

            for id, element in enumerate(RectangleWhatsearchVariant):
                addItem = repr(element._name_)
                self.Box_whatsearch.addItem(addItem)
                self.Box_whatsearch.setItemText(id, self._translate("MainWindow", element.name))

        else:
            self.Box_whatsearch.clear()
            self.Box_whatsearch.addItem(f"{RectangleWhatsearchVariant.whatsearch.name}")
            self.Box_whatsearch.setItemText(0, self._translate("MainWindow", RectangleWhatsearchVariant.whatsearch.name))

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
                if self.figure == FigureNames.rectangle.value:
                    if self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.sides.value:
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.sides.name)

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
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.diagonal.name)
                        
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
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.perimeter.name)

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
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.square.name)

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
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.radius.name)

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
                            
                    elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.angleA.value:  # Угол между стороной и диагональю прямоугольника
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.angleA.name)
                        
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
                        
                    elif self.Box_whatsearch.currentIndex() == RectangleWhatsearchVariant.angleB.value:  # угол между диагоналями прямоугольника
                        self.lineEdit_page2_line1.setText(RectangleWhatsearchVariant.angleB.name)
                        
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
    
        ui = ErrorDialog(text=text, details=details)
        print(ui)
        ui.setupUi(ui)
        ui.show()
        
        ui.btn_ok.clicked.connect(lambda: ui.btn_clicked(ui.btn_ok.text(), ui))
        ui.btn_details.clicked.connect(lambda: ui.btn_clicked(ui.btn_details.text(), ui))

    @staticmethod
    def show_matplotlib_window(fig):

        ui = PlotWindow(figure=fig)
        print(ui)
        ui.setupUi(ui)
        ui.show()

    def update_image(self):
        """
        Очищаем виджет с изображением в левой части окна. Добавляет изображение для выбранной фигуры

        """
        file_name = FigureNames(FigureNames.keyForValue(self.figure)).name
        path = Path.cwd()/'images'/'figures'/file_name
        self.label_image.clear()
        self.label_image.setPixmap(QtGui.QPixmap(f"{path}"))
        


