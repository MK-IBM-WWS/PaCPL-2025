from lab2.lab_python_oop import Circle, Rectangle, Square, Color

import matplotlib.pyplot as plt

def main():
    n = 9.0

    circle = Circle(radius=n, color=Color.GREEN)
    rectangle = Rectangle(width=n, height=n,color=Color.BLUE)
    square = Square(side=n,color=Color.RED)
    shapes = [circle,rectangle,square]

    for shape in shapes:
        fig, ax = plt.subplots(figsize=(10, 8))
        shape.draw(ax)
        print(shape)
        print(f"Площадь: {shape.area():.2f}")

        ax.set_aspect('equal')
        ax.set_xlim(-(n + 2), n + 2)
        ax.set_ylim(-(n + 2), n + 2)
        ax.set_title(shape.get_name())
        plt.savefig(f'./{shape.get_name()}.png')
        print(f"Изображение сохранено в '{shape.get_name()}.png'")
        print("-" * 40)

if __name__ == "__main__":
    main()







