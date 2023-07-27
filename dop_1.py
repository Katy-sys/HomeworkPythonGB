# задача 1 необязательная. Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции


# делим исходное число на 2 и записывам остаток от деления в список
def convert_to (n: int, nota: int) -> list:
    list_n = []
    while n_ten >= nota:
        list_n.append(n % nota)
        n = n//nota
    list_n.append(n % nota)
    return list_n



# переварачиваем список
def turn_over_list (list_n: list) -> list:
    a = []
    for _ in list_n:
        a = list_n[::-1]
    return a



# преобразуем список в строку
def to_st (li: list) -> str:
    st = ""
    for i in li:
        st += str(i) + " "
    return st


n_ten: int = int(input('Введите целое число: '))
notation: int = int(input('Выберите систему счисления для перевода (2 или 8) : '))

f = convert_to(n_ten, notation)
ff = turn_over_list(f)
fff = to_st(ff)
print(fff)

# проверка решения
# print(f"Двоичное число: {bin(n_ten)}")
# print("Восьмеричное число: %s"  %  oct(n_ten))