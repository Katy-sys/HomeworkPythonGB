# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))

list_one = input(f'Введите {n} целых чисел через пробел: ').split()
print(list_one)

if len(list_one) != n:
    print("Вы ввели неверное кол-во чисел. Запустите программу на выполнение снова.")
    print(len(list_one))
else:    
    list_two = list(input(f'Введите {m} целых чисел через пробел: ').split())
    print(list_two)
    if len(list_two) != m:
        print("Вы ввели неверное кол-во чисел. Запустите программу на выполнение снова.")
    else:
        list_one_unique = set(list_one)
        list_two_unique = set(list_two)
        print()
        print()
        print(list_one_unique)
        print(list_two_unique)
        i = list_one_unique.intersection(list_two_unique)
        print()
        print()
        print(sorted(i))