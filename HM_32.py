# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint

def l_k (a, b, rsp) -> list:
    list_index: list = []
    for index, item in enumerate(rsp):
        if item >= a and item <= b:
            list_index.append(index)
    return(list_index)


rsp: list = list(randint(0, 200) for _ in range(10))
print(rsp)

a: int = int(input('Введите значение для нижней границы диапазона: '))
b: int = int(input('Введите значение для верхней границоы диапазна: '))

print(l_k(a, b, rsp))