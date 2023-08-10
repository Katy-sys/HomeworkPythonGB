# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def elements (a: int, d: int, n: int) -> list:
    list_res = []
    for i in range(1, n + 1):  
        an: int = a + (i-1) * d
        list_res.append(an)
    return list_res

a1: int = int(input('Введите первое число арифметической прогрессии: '))
difference: int = int(input('Введите разность: '))
n: int = int(input('Введите число значений: '))

print(elements(a1, difference, n))