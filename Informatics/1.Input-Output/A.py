"""
Задача №2936. Гипотенуза
Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.

Входные данные
В двух строках вводятся два числа (числа целые,положительные, не превышают 1000).

Выходные данные
Выведите ответ на задачу.

Примеры:
Входные данные:
3
4
Выходные данные:
5.0
"""
import math
def f(a, b):
    c = a * a + b * b
    c = math.sqrt(c)
    return c
a = int(input())
b = int(input())
print(f(a, b))


"""
Another solution: 

import math
a = int(input())
b = int(input())
x = pow(a, 2)
y = pow(b, 2)
c = x + y
ans = math.sqrt(c)
print(ans)
"""