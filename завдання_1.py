import math

def expression (x, y):

    z = math.cos(x)**2 + math.sin(y)**2

    return z

def sum_of_squares (n):
    S = sum(i**2 for i in range(1, n+1))

    return S

x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

print("Значення виразу z = ", expression(x, y))

n = int(input("Введіть значення N: "))

print("Сума S  квадратів чисел від 1 до N = ", sum_of_squares (n))