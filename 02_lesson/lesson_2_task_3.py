import math


def S_square(x):
    return math.ceil(x*x)


x = float(input("Сторона квадрата: "))
print(f"Площадь треугольника равна: {S_square(x)}")
