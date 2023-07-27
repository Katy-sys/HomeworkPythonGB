# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

import random

number_bushes = int(input('Введите количество кустов черники (n > 0): '))
tipe_mod = 3
list_bush_berries = []

for _ in range(number_bushes):
    list_bush_berries.append(random.randint(1, 100))
print(list_bush_berries)    


list_summ = []


for picking_number in range(number_bushes):
    
    list_mod = list_bush_berries[:tipe_mod]

    summ_berries = 0
    for i in list_mod:
        summ_berries += i
        
    list_summ.append(summ_berries)
    list_bush_berries.insert(number_bushes, list_bush_berries[0])
    list_bush_berries.pop(0)
    # print(list_bush_berries)
    # print(list_summ)

max_summ = list_summ[0]
for i in list_summ:
    if i > max_summ:
        max_summ = i
print(max_summ)