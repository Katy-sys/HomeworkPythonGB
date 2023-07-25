# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

N = int (input("Введите число N > 1: "))

base = 2
degree = 0
result = 1

while result <= N:
    print (f" {base}^{degree} --> {result} ")
    degree += 1
    result = base ** degree
    
    