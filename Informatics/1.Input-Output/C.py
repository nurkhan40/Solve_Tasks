"""
Задача №2938. Дележ яблок - 1
N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?

Входные данные
Программа получает на вход числа N и K.

Выходные данные
Программа должна вывести искомое количество яблок.
"""

def f(a, b):
    c = b // a
    return c

a = int(input())
b = int(input())
print(f(a, b))