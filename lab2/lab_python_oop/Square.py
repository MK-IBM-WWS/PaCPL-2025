from lab2.lab_python_oop.Rectangle import Rectangle, Shape_Color

class Square(Rectangle):
    def __init__(self, side: float, color:Shape_Color.Color):
        super().__init__(side, side, color)
        self._name = "Квадрат"

    def __repr__(self):
        return f"{self._name} со стороной {self.width} цвета {str(self.color)}."
