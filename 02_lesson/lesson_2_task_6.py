lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for x in lst:
    if (x < 30):
        print(x)
print("Разделительная полоса между заданиями А и Б")
for x in lst:
    if (x % 3 == 0):
        print(x)
