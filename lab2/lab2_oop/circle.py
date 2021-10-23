from lab2_oop.figure import Figure
from lab2_oop.color import FigureColor
import math


class Circle(Figure):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.color = FigureColor()
        self.color.colorproperty = color_param

    def mesure(self):
        return math.pi*(self.r**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            self.color.colorproperty,
            Circle.get_figure_type(),
            self.r,
            self.mesure()
        )