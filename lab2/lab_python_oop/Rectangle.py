from lab2.lab_python_oop import GeometricalShape, Shape_Color
from matplotlib.patches import Rectangle as MplRectangle

class Rectangle(GeometricalShape):
    def __init__(self, width:float, height:float, color:Shape_Color.Color):
        self._name="Прямоугольник"
        if width <= 0 or height <= 0:
            raise ValueError("Стороны должны быть положительными числами")
        self._width = width
        self._height = height
        self._center = (0, 0)
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
    def width(self)->float:
        return self._width

    @width.setter
    def width(self, width:float):
        self._width=width

    @property
    def height(self)->float:
        return self._height

    @height.setter
    def height(self, height:float):
        self._height=height

    def area(self):
        return self._width * self._height

    def draw(self, ax):
        rectangle = MplRectangle((-self._width/2.0,-self.height/2.0), width=self._width,height=self._height, fill=True, facecolor=str(self._color),
                           edgecolor='red', linewidth=2, label=f'{self._name}')
        ax.add_patch(rectangle)

    def __repr__(self):
        return f"{self._name} со сторонами {self._width} и {self._height} цвета {str(self._color)}."