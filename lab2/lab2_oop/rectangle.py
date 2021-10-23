from lab2_oop.figure import Figure
from lab2_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.color = FigureColor()
        self.color.colorproperty = color_param

    def mesure(self):
        return self.width*self.height

    def __repr__(self):
        return '{} {} шириной {} и высотой {} площадью {}.'.format(
            self.color.colorproperty,
            Rectangle.get_figure_type(),
            self.width,
            self.height,
            self.mesure()
        )
