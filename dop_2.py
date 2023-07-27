# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re

import re

def get_dictionary (li):

    dic = {}

    if li[0] != "-":
        li.insert(0, "+")
    
    for i in range(0, len(li), 2):
        
        k = i + 2
        s = ''.join(li[i:k])
        list_s = []

        for i in s:
            list_s += i
        
        x_in_list = list_s.count('x')
        equal_sign_in_list = list_s.count('=')

        if x_in_list > 0:
            position_x = 0
            for item in range(len(list_s)):
                if list_s[item] == "x":
                    position_x = item   
            # print(position_x)        

            k_dict = ''.join(list_s[position_x:])
            v_dict = ''.join(list_s[:position_x])
        elif equal_sign_in_list > 0:
            k_dict = '0'
            v_dict = ''.join(list_s[1:])
        else:
            k_dict = '1'
            v_dict = ''.join(list_s[:])
       
        dic[k_dict] = v_dict
        
    print(dic)
    return dic


# перевести значения в словаре в int
def dic_value_to_int (dic):
    re ={}
    for k in dic:
        re[k] = int(dic[k])
    return re

# сложить значения двух словарей
def fill_dic_res (dic, dic_res):
    
    for item in dic:
        try:
            dic_res[item] += dic[item]       # складываем значения
        except KeyError:                                    
            dic_res[item] = dic[item]        # если ключа еще нет - создаем
    return dic_res


mn = input("Введите многочлен (2x^2 + 4x + 5 = 0): ")
li_mn = list(mn.split())
dic_one = dic_value_to_int(get_dictionary(li_mn))   

jk = input("Введите многочлен (5x^3 - 3x^2 - 12 = 0): ")
li_jk = list(jk.split())
dic_two = dic_value_to_int(get_dictionary(li_jk))

dic_res = {}
fill_dic_res(dic_one, dic_res)
fill_dic_res(dic_two, dic_res)
sorted_dic_res = dict(reversed(sorted(dic_res.items())))


s = []
for key, item in sorted_dic_res.items():
    
    if key == '0':
        s.append("= {}".format(item))
    elif item == 0 and key != '1':
        s.append("".format(item, key))
    elif item == 0 and key == '1':
        s.append("".format(item, key))
    elif item < 0 and key != '1':
        s.append("{}{}".format(item, key))
    elif key == '1' and item > 0:
        s.append("+{}".format(item))
    elif key == '1' and item < 0:
        s.append("{}".format(item))
    else:
        s.append("+{}{}".format(item, key))


result = " ".join(s)
print(result)
       
