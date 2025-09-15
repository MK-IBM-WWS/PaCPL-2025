import unittest

from lab2.lab_python_oop import Square, Color
import matplotlib.pyplot as plt


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(side=5.0, color=Color.BLUE)

    def test_square_creation(self):
        self.assertEqual(self.square.width, 5.0)
        self.assertEqual(self.square.height, 5.0)
        self.assertEqual(str(self.square.color), "blue")

    def test_square_area(self):
        self.assertEqual(self.square.area(), 25.0)

    def test_square_negative_side(self):
        with self.assertRaises(ValueError):
            Square(side=-5.0, color=Color.BLUE)

    def test_square_draw(self):
        fig, ax = plt.subplots()
        try:
            self.square.draw(ax)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Ошибка при отрисовке: {e}")
        finally:
            plt.close(fig)

    def test_square_repr(self):
        expected_repr = "Квадрат со стороной 5.0 цвета blue. Площадь: 25.00"
        self.assertEqual(repr(self.square), expected_repr)


if __name__ == '__main__':
    unittest.main()