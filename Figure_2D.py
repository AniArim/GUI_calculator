
import math
import decimal
from decimal import Decimal
from ErrorWindow import ErrorDialog
from EnumModule import *


class Figure_2D:
    
    def __init__(self, whatsearch: enum.Enum, data_input: dict, variant: enum.Enum):
        self.data_input = data_input  # Словарь типа "lineEdit_page1_line1" : 56.2"
        self.whatsearch = whatsearch  # Индекс. по нему получаем список отображаемых полей
        self.variant = variant
        self.diameter = None
        self.radius = None
        self.square = None
        self.perimeter = None
        self.diagonal = None
        self.angleA = None
        self.angleB = None

    @staticmethod
    def error_show():

        ui = ErrorDialog(text="Угол не может быть больше 180 градусов!",
                         details="Угол равный 180 градусам - это прямая. Введите угол меньше 180 градусов.")
        ui.setupUi(ui)
        ui.show()

        ui.btn_ok.clicked.connect(lambda: ui.btn_clicked(ui.btn_ok.text(), ui))
        ui.btn_details.clicked.connect(lambda: ui.btn_clicked(ui.btn_details.text(), ui))


class Rectangle(Figure_2D):
    
    def __init__(self,  whatsearch: enum.Enum, data_input: dict, variant: enum.Enum):
        super().__init__(whatsearch, data_input, variant)

        self.sideA = self.get_value_from_data_input_line(1) or None
        self.sideB = self.get_value_from_data_input_line(2) or None
        self.side = self.sideA or self.sideB

    def get_value_from_data_input_line(self, lineIndex):
        return self.data_input.get(f"lineEdit_page1_line{lineIndex}_input")

    def result(self):
        """
        Метод рассчитывает результат в зависимости от входных данных (что ищем, введенных параметров, и функции).
        Проверяет углы на величину 180 градусов.
        
        :return: искомая величина, класс Decimal. Углы окгругляются до целого числа, другие параметры - до десятых.
        False - если вызвана ошибка
        """
        if self.whatsearch == RectangleWhatsearchVariant.sides.value:  # Стороны
            if self.variant == RectangleSidesFormulas.diagonalAndSide:
                self.diagonal = self.get_value_from_data_input_line(3)
                self.side_desired = math.sqrt(self.diagonal ** 2 - self.side ** 2)

            elif self.variant == RectangleSidesFormulas.squareAndSide:
                self.square = self.get_value_from_data_input_line(4)
                self.side_desired = self.square / self.side

            elif self.variant == RectangleSidesFormulas.perimeterAndSide:
                self.perimeter = self.get_value_from_data_input_line(5)
                self.side_desired = (self.perimeter - 2 * self.side) / 2

            elif self.variant == RectangleSidesFormulas.diameterAndAngleA:
                if self.get_value_from_data_input_line(3):
                    self.diameter = self.get_value_from_data_input_line(3)
                else:
                    self.diameter = self.get_value_from_data_input_line(2)

                if self.get_value_from_data_input_line(6) < 180:
                    self.angleA = self.get_value_from_data_input_line(6)
                    self.sideA = self.diameter * (math.sin(math.radians(self.angleA)))
                    self.sideB = self.diameter * (math.cos(math.radians(self.angleA)))
                    return Decimal(f"{self.sideA}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP), \
                        Decimal(f"{self.sideB}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
                else:
                    self.error_show()
                    return False

            elif self.variant == RectangleSidesFormulas.diameterAndAngleB:
                if self.get_value_from_data_input_line(3):
                    self.diameter = self.get_value_from_data_input_line(3)
                else:
                    self.diameter = self.get_value_from_data_input_line(2)

                if self.get_value_from_data_input_line(7) < 180:
                    self.angleB = self.get_value_from_data_input_line(7)
                    self.sideA = self.diameter * math.sin(math.radians(self.angleB / 2))
                    self.sideB = self.diameter * math.cos(math.radians(self.angleB / 2))
                    return Decimal(f"{self.sideA}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP), \
                        Decimal(f"{self.sideB}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
                else:
                    self.error_show()
                    return False

            return Decimal(f"{self.side_desired}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
        
        elif self.whatsearch == RectangleWhatsearchVariant.diagonal.value:  # Диагональ

            if self.variant == RectangleDiagFormulas.pythagoras:
                self.diagonal = math.sqrt(self.sideA ** 2 + self.sideB ** 2)

            elif self.variant == RectangleDiagFormulas.squareAndSide:
                self.square = self.get_value_from_data_input_line(4)
                self.diagonal = math.sqrt(self.square**2 + self.side ** 4) / self.side

            elif self.variant == RectangleDiagFormulas.perimeterAndSide:
                self.perimeter = self.get_value_from_data_input_line(5)
                self.diagonal = (math.sqrt(self.perimeter ** 2 - (4 * self.perimeter * self.side) + (8 * self.side ** 2))) / 2

            elif self.variant == RectangleDiagFormulas.radius:
                self.radius = self.get_value_from_data_input_line(3)
                self.diagonal = self.radius * 2

            elif self.variant == RectangleDiagFormulas.angleAAndSideA:
                if self.get_value_from_data_input_line(6) < 180:
                    self.angleA = self.get_value_from_data_input_line(6)
                    self.diagonal = self.sideA / (math.sin(math.radians(self.angleA)))
                else:
                    self.error_show()
                    return False

            elif self.variant == RectangleDiagFormulas.angleAAndSideB:
                if self.get_value_from_data_input_line(7) < 180:
                    self.angleB = self.get_value_from_data_input_line(7)
                    self.diagonal = self.sideB / (math.cos(math.radians(self.angleB)))
                else:
                    self.error_show()
                    return False

            elif self.variant == RectangleDiagFormulas.angleBAndSquare:
                if self.get_value_from_data_input_line(7) < 180:
                    self.square = self.get_value_from_data_input_line(4)
                    self.angleB = self.get_value_from_data_input_line(7)
                    self.diagonal = math.sqrt((2 * self.square) / (math.sin(math.radians(self.angleB))))
                else:
                    self.error_show()
                    return False

            return Decimal(f"{self.diagonal}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
        
        elif self.whatsearch == RectangleWhatsearchVariant.perimeter.value:  # Периметр

            if self.variant == RectanglePerimeterFormulas.sides:
                if self.sideA and self.sideB:
                    self.perimeter = 2 * (self.sideA + self.sideB)

            elif self.variant == RectanglePerimeterFormulas.squareAndSide:
                self.square = self.get_value_from_data_input_line(4)
                self.perimeter = (2 * self.square + 2 * self.side ** 2) / self.side

            elif self.variant == RectanglePerimeterFormulas.diagonalAndSide:
                self.diagonal = self.get_value_from_data_input_line(3)
                self.perimeter = (self.side + math.sqrt(self.diagonal ** 2 - self.side ** 2)) * 2

            elif self.variant == RectanglePerimeterFormulas.radiusAndSide:
                self.radius = self.get_value_from_data_input_line(5)
                self.perimeter = (self.side + math.sqrt(4 * self.radius ** 2 - self.side ** 2)) * 2

            return Decimal(f"{self.perimeter}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
        
        elif self.whatsearch == RectangleWhatsearchVariant.square.value:  # Площадь

            if self.variant == RectangleSquareFormulas.sides:
                self.square = self.sideA * self.sideB

            elif self.variant == RectangleSquareFormulas.perimeterAndSide:
                self.perimeter = self.get_value_from_data_input_line(5)
                self.square = ((self.perimeter * self.side) - (2 * self.side ** 2)) / 2

            elif self.variant == RectangleSquareFormulas.diagonalAndSide:
                self.diagonal = self.get_value_from_data_input_line(3)
                self.square = (self.side * math.sqrt(self.diagonal ** 2 - self.side ** 2))

            elif self.variant == RectangleSquareFormulas.angleBAndDiagonal:

                if self.get_value_from_data_input_line(6) < 180:
                    self.diagonal = self.get_value_from_data_input_line(3)
                    self.angleB = self.get_value_from_data_input_line(6)
                    self.square = (self.diagonal ** 2 * math.sin(math.radians(self.angleB))) / 2
                else:
                    self.error_show()
                    return False

            elif self.variant == RectangleSquareFormulas.radiusAndSide:
                self.radius = self.get_value_from_data_input_line(4)
                self.square = self.side * math.sqrt(4 * self.radius ** 2 - self.side ** 2)

            return Decimal(f"{self.square}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
        
        elif self.whatsearch == RectangleWhatsearchVariant.radius.value:  # Окружность описанная вокруг
            
            if self.variant == RectangleRadiusFormulas.sides:
                self.radius = (math.sqrt(self.sideA ** 2 + self.sideB ** 2)) / 2

            elif self.variant == RectangleRadiusFormulas.perimeterAndSide:
                self.perimeter = self.get_value_from_data_input_line(5)
                self.radius = (math.sqrt(self.perimeter ** 2 - (4 * self.perimeter * self.side) + (8 * self.side ** 2))) / 4

            elif self.variant == RectangleRadiusFormulas.squareAndSide:
                self.square = self.get_value_from_data_input_line(4)
                self.radius = ((math.sqrt(self.square ** 2 + self.side ** 4)) / self.side) / 2

            elif self.variant == RectangleRadiusFormulas.diagonal:
                self.diagonal = self.get_value_from_data_input_line(3)
                self.radius = self.diagonal / 2

            elif self.variant == RectangleRadiusFormulas.angleAAndSideA:
                if self.get_value_from_data_input_line(6) < 180:
                    self.angleA = self.get_value_from_data_input_line(6)
                    self.radius = self.sideA / (2 * math.sin(math.radians(self.angleA)))
                else:
                    return False

            elif self.variant == RectangleRadiusFormulas.angleBAndSideA:
                if self.get_value_from_data_input_line(7) < 180:
                    self.angleB = self.get_value_from_data_input_line(7)
                    self.radius = self.sideB / (2 * math.cos(math.radians(self.angleB)))
                else:
                    return False

            elif self.variant == RectangleRadiusFormulas.angleBAndSquare:
                if self.get_value_from_data_input_line(7) < 180:
                    self.angleB = self.get_value_from_data_input_line(7)
                    self.square = self.get_value_from_data_input_line(4)
                    self.radius = (math.sqrt((2 * self.square) / math.sin(math.radians(self.angleB)))) / 2
                else:
                    return False

            return Decimal(f"{self.radius}").quantize(Decimal('1.0'), decimal.ROUND_HALF_UP)
        
        elif self.whatsearch == RectangleWhatsearchVariant.angleA.value:  # Угол между стороной и диагональю прямоугольника

            if self.variant == RectangleAngleAFormulas.diagonalAndSide:
                self.diagonal = self.get_value_from_data_input_line(3)
                if self.sideA:
                    self.angleA = math.degrees((math.asin(self.sideA / self.diagonal)))
                elif self.sideB:
                    self.angleA = math.degrees((math.acos(self.sideB / self.diagonal)))

            elif self.variant == RectangleAngleAFormulas.angleB:
                if self.get_value_from_data_input_line(4) < 180:
                    self.angleB = self.get_value_from_data_input_line(4)
                    self.angleA = (self.angleB / 2)
                else:
                    self.error_show()
                    return False

            return Decimal(f"{self.angleA}").quantize(Decimal('1'), decimal.ROUND_HALF_UP)
        
        elif self.whatsearch == RectangleWhatsearchVariant.angleB.value:  # угол между диагоналями прямоугольника
            if self.variant == RectangleAngleBFormulas.angleA:
                if self.get_value_from_data_input_line(3) < 180:
                    self.angleA = self.get_value_from_data_input_line(3)
                    self.angleB = (2 * self.angleA)
                else:
                    self.error_show()
                    return False

            elif self.variant == RectangleAngleBFormulas.squareAndDiagonal:
                self.square = self.get_value_from_data_input_line(1)
                self.diagonal = self.get_value_from_data_input_line(2)
                self.angleB = math.degrees(math.asin((2 * self.square / (self.diagonal ** 2))))

            return Decimal(f"{self.angleB}").quantize(Decimal('1'), decimal.ROUND_HALF_UP)
    
    
        
        
