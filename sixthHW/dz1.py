# 1. Наибольший общий делитель. В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. 
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки. 

list = []
a = None

while a != '':
    a = input('Введите натуральное число: ')
    if a.isdigit():
        a = int(a)
        list.append(a)
 
import math
from functools import reduce
b = reduce(lambda x, y: math.gcd(x, y), list[1:])
print(b)