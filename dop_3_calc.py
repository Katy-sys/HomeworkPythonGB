# Задача CALC необязательная. Напишите рекурсивную программу вычисления 
# арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
# Приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 


#     1+2*3 => 7; 

#     (1+2)*3 => 9;
# Тут может помочь библиотека re


import re
 
reg_exp_br = r"\((.+?)\)"
reg_exp_mul = r"(-?\d+(?:\.\d+)?)\s*(\*|\/)\s*(-?\d+(?:\.\d+)?)"
reg_exp_add = r"(-?\d+(?:\.\d+)?)\s*(\+|\-)\s*(-?\d+(?:\.\d+)?)"
 
 
 
def my_eval(expresion: str) -> str:
 
    while (match := re.search(reg_exp_br, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

    while (match := re.search(reg_exp_mul, expresion)):
        expresion: str = expresion.replace(match.group(0), calc(match.group(1),match.group(2),match.group(3)))

    while (match := re.search(reg_exp_add, expresion)):
        expresion: str = expresion.replace(match.group(0), calc(match.group(1),match.group(2),match.group(3)))
    
    return expresion
 
def calc(a: float, z: str, b: float) -> str:
    if(z == "+"):
        return str(float(a)+float(b))
    elif(z == "-"):
        return str(float(a)-float(b))
    elif(z == "*"):
        return str(float(a)*float(b))
    elif(z == "/"):
        return str(float(a)/float(b))
    
exp = ''.join(input('Введите выражение: ').split())
print(f'{exp} = {my_eval(exp)}')
