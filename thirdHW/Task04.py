# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.


def conver_Ten_bin(number):
    num_ = number
    bin_num = ""
    while num_ > 0:
        bin_num = str(num_ % 2) + bin_num
        num_ //= 2
    return print(f"Число в дясятичной {number} = {bin_num} в двоийчной системе")


ten_number = int(input("ВВедите десятичное число: "))

conver_Ten_bin(ten_number)
