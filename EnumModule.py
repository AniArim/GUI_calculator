
import enum


class FigureNames(enum.Enum):

    rectangle = "Прямоугольник"
    parallelogram = "Параллелограмм"
    square = "Квадрат"
    rhombus = "Ромб"
    trapezium1 = "Трапеция равнобедренная"
    trapezium2 = "Трапеция прямоугольная"
    triangle = "Треугольник"
    hexagon = "Шестиугольник"
    circle = "Окружность"
    prism = "Призма"
    cuboid = "Параллелепипед"
    cube = "Куб"
    pyramid = "Пирамида"
    cylinder = "Цилиндр круговой"
    cone = "Конус круговой"
    sphere = "Шар, сфера"

    def __init__(self, *args):
        pass

    @classmethod
    def keyForValue(cls, figure: str) -> "FigureNames":
        data = tuple(cls)
        for object_ in data:
            if object_.value == figure:
                return object_


class RectangleWhatsearchVariant(enum.Enum):
    whatsearch = 0  # "Что нужно найти?"
    sides = 1  # "Стороны"
    diagonal = 2  # "Диагональ"
    perimeter = 3  # "Периметр"
    square = 4  # "Площадь"
    radius = 5  # "Окружность описанная вокруг"
    angleA = 6  # "Угол между стороной и диагональю 'a'"
    angleB = 7  # "Угол между диагоналями 'β'"

    def __init__(self, *args):
        pass

    @staticmethod
    def names() -> tuple:
        return (
            "Что нужно найти?",
            "Стороны",
            "Диагональ",
            "Периметр",
            "Площадь",
            "Окружность описанная вокруг",
            "Угол между стороной и диагональю 'a'",
            "Угол между диагоналями 'β'"
        )

    @property
    def text(self) -> str:
        return self.names()[self.value]


class RectangleParentFormulas(enum.Enum):

    def __init__(self, *args):
        pass

    @staticmethod
    def names() -> tuple:
        return ()

    @property
    def text(self) -> str:
        return self.names()[self.value]


class RectangleSidesFormulas(RectangleParentFormulas):

    diagonalAndSide = 0  # "Через диагональ и сторону"
    squareAndSide = 1   # "через площадь и другую сторону"
    perimeterAndSide = 2  # "через периметр и другую сторону"
    diameterAndAngleA = 3  # "через диаметр и угол α"
    diameterAndAngleB = 4  # "через диаметр и угол β"

    @staticmethod
    def names() -> tuple:
        return (
            "Через диагональ и сторону",
            "через площадь и другую сторону",
            "через периметр и другую сторону",
            "через диаметр и угол α",
            "через диаметр и угол β"
        )


class RectangleDiagFormulas(RectangleParentFormulas):

    pythagoras = 0  # "Через теорему Пифагора"
    squareAndSide = 1   # "через площадь и другую сторону"
    perimeterAndSide = 2  # "через периметр и другую сторону"
    radius = 3  # "Через радиус"
    angleAAndSideA = 4  # "Через синус угла 'a', прилегающего к диагонали, и длину стороны 'a' противоположной этому углу"
    angleAAndSideB = 5  # "Через косинус угла 'a', прилегающего к диагонали, и длину стороны 'b' прилегающей к этому углу"
    angleBAndSquare = 6  # "Через синус острого угла 'β' между диагоналями и площадью прямоугольника"

    @staticmethod
    def names() -> tuple:
        return (
            "Через теорему Пифагора",
            "Через площадь и другую сторону",
            "Через периметр и другую сторону",
            "Через радиус",
            "Через синус угла 'a', прилегающего к диагонали, и длину стороны 'a' противоположной этому углу",
            "Через косинус угла 'a', прилегающего к диагонали, и длину стороны 'b' прилегающей к этому углу",
            "Через синус острого угла 'β' между диагоналями и площадью прямоугольника"
        )


class RectanglePerimeterFormulas(RectangleParentFormulas):

    sides = 0  # "Через две стороны прямоугольника"
    squareAndSide = 1   # "Через площадь и другую сторону"
    diagonalAndSide = 2  # "Через диагональ и любую сторону"
    radiusAndSide = 3  # "Через радиус описанной окружности и любую сторону"

    @staticmethod
    def names() -> tuple:
        return (
            "Через две стороны прямоугольника",
            "Через площадь и другую сторону",
            "Через диагональ и любую сторону",
            "Через радиус описанной окружности и любую сторону",
        )


class RectangleSquareFormulas(RectangleParentFormulas):

    sides = 0  # "Через две стороны прямоугольника"
    perimeterAndSide = 1   # "Через периметр и любую сторону"
    diagonalAndSide = 2  # "Через диагональ и любую сторону"
    angleBAndDiagonal = 3  # "Через диагональ и синус острого угла 'β' между диагоналями"
    radiusAndSide = 4  # "Через радиус и любую сторону"

    @staticmethod
    def names() -> tuple:
        return (
            "Через две стороны прямоугольника",
            "Через периметр и любую сторону",
            "Через диагональ и любую сторону",
            "Через диагональ и синус острого угла 'β' между диагоналями",
            "Через радиус и любую сторону"
        )


class RectangleRadiusFormulas(RectangleParentFormulas):

    sides = 0  # "Через две стороны прямоугольника"
    perimeterAndSide = 1   # "Через периметр и любую сторону"
    squareAndSide = 2  # "Через площадь и любую сторону"
    diagonal = 3  # "Через диагональ"
    angleAAndSideA = 4  # "Через синус угла 'α', прилегающего к диагонали, и длину стороны 'a' противоположной этому углу"
    angleBAndSideA = 5  # "Через косинус угла 'α', прилегающего к диагонали, и длину стороны 'b' прилегающей к этому углу"
    angleBAndSquare = 6  # "Через синус острого угла между диагоналями 'β' и площадью прямоугольника"

    @staticmethod
    def names() -> tuple:
        return (
            "Через две стороны прямоугольника",
            "Через периметр и любую сторону",
            "Через площадь и любую сторону",
            "Через диагональ",
            "Через синус угла 'α', прилегающего к диагонали, и длину стороны 'a' противоположной этому углу",
            "Через косинус угла 'α', прилегающего к диагонали, и длину стороны 'b' прилегающей к этому углу",
            "Через синус острого угла между диагоналями 'β' и площадью прямоугольника"
        )


class RectangleAngleAFormulas(RectangleParentFormulas):

    diagonalAndSide = 0  # "через диагональ и любую сторону"
    angleB = 1   # "Через угол между диагоналями 'β'"

    @staticmethod
    def names() -> tuple:
        return (
            "Через диагональ и любую сторону",
            "Через угол между диагоналями 'β'",
            )


class RectangleAngleBFormulas(RectangleParentFormulas):

    angleA = 0   # "Через угол 'α' между стороной и диагональю"
    squareAndDiagonal = 1  # "через площадь и диагональ"

    @staticmethod
    def names() -> tuple:
        return (
            "Через угол 'α' между стороной и диагональю",
            "Через площадь и диагональ",
            )
