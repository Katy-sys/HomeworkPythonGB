# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def count_vowels (poem: str) -> int:
    sum_vowels: int= 0
    vowels = 'аеёиоуэюя'

    for item in range(len(poem)):
        if poem[item] in vowels:
            sum_vowels += 1

    return sum_vowels

def is_poem(maybe_poem):
    stanza_poem: list = maybe_poem.replace('-', '').split()
    count = 0
    
    for index, item in enumerate(stanza_poem):
        n = count_vowels(item)
        if(index == 0):
            count = n
        else:
            if(n != count): 
                return False   
    return  True  


def print_res (res: bool):
    if res == True:
        print('Парам пам-пам ;-)')
    else:
        print('Пам парам %-|')

poem  = input('Введите стихотворение, разделяя фразы пробелами: ')

print_res(is_poem(poem))