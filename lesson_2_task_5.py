def month_to_season(x):
    if x in range(1, 3) or x == 12:
        print("Зима")
    if x in range(3, 6):
        print("Весна")
    if x in range(6, 9):
        print("Лето")
    if x in range(9, 12):
        print("Осень")
    if x < 1 or x > 12:
        print("Выберите число от 1 до 12")


x = int(input("Введите номер месяца: "))
month_to_season(x)
