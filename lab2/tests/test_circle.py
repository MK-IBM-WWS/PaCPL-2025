import unittest

from lab2.lab_python_oop import Circle, Color
import matplotlib.pyplot as plt


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(radius=5.0, color=Color.GREEN)

    def test_circle_creation(self):
        self.assertEqual(self.circle.radius, 5.0)
        self.assertEqual(str(self.circle.color), "green")

    def test_circle_area(self):
        expected_area = 3.141592653589793 * 25
        self.assertAlmostEqual(self.circle.area(), expected_area, places=2)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(radius=-5.0, color=Color.GREEN)

    def test_circle_draw(self):
        fig, ax = plt.subplots()
        try:
            self.circle.draw(ax)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Ошибка при отрисовке: {e}")
        finally:
            plt.close(fig)

    def test_circle_repr(self):
        expected_repr = "Круг с радиусом 5.0 цвета green. Площадь: 78.54"
        self.assertEqual(repr(self.circle), expected_repr)


if __name__ == '__main__':
    unittest.main()