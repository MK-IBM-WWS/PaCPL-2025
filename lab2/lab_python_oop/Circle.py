from lab2.lab_python_oop import GeometricalShape, Shape_Color

import math
from matplotlib.patches import Circle as MplCircle

class Circle(GeometricalShape):
    def __init__(self, radius:float, color:Shape_Color.Color):
        self._name = "Круг"
        if radius <= 0.0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = radius
        self._color = color

    def get_name(self)->str:
        return self._name

    @property
    def color(self)->str:
        return str(self._color)

    @color.setter
    def color(self, color_name:Shape_Color.Color):
        self._color=color_name

    @property
    def radius(self)->float:
        return self._radius

    @radius.setter
    def radius(self, radius:float):
        if radius <= 0.0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius=radius

    def area(self)->float:
        return math.pi * self._radius ** 2

    def draw(self, ax):
        circle = MplCircle((0,0), self._radius, fill=True, facecolor=str(self._color),
                           edgecolor='red', linewidth=2, label=f'Круг R={self._radius}')
        ax.add_patch(circle)

    def __repr__(self):
        return f"{self._name} с радиусом {self._radius} цвета {str(self._color)}."