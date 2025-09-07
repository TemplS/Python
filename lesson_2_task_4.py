def fizz_buzz(n):
    if n == 0:
        return
    fizz_buzz(n - 1)
    if n % 3 == 0:
        print("Fizz", end="")
    if n % 5 == 0:
        print("Buzz", end="")
    if n % 3 and n % 5:
        print(n, end="")
    print("")


n = int(input("Введите целое число: "))
fizz_buzz(n)