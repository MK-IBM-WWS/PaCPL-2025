import unittest

from lab2.lab_python_oop import Rectangle, Color
import matplotlib.pyplot as plt


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(width=6.0, height=4.0, color=Color.RED)

    def test_rectangle_creation(self):
        self.assertEqual(self.rectangle.width, 6.0)
        self.assertEqual(self.rectangle.height, 4.0)
        self.assertEqual(str(self.rectangle.color), "red")

    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 24.0)

    def test_rectangle_negative_sides(self):
        with self.assertRaises(ValueError):
            Rectangle(width=-6.0, height=4.0, color=Color.RED)
        with self.assertRaises(ValueError):
            Rectangle(width=6.0, height=-4.0, color=Color.RED)

    def test_rectangle_draw(self):
        fig, ax = plt.subplots()
        try:
            self.rectangle.draw(ax)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Ошибка при отрисовке: {e}")
        finally:
            plt.close(fig)

    def test_rectangle_repr(self):
        expected_repr = "Прямоугольник со сторонами 6.0 и 4.0 цвета red. Площадь: 24.00"
        self.assertEqual(repr(self.rectangle), expected_repr)


if __name__ == '__main__':
    unittest.main()