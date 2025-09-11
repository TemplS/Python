import math


def S_square(a):
    return (a*a)


x = float(input("Сторона квадрата: "))
a = math.ceil(x)
print(f"Площадь треугольника равна: {S_square(a)}")
