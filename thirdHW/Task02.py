# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Create_New_Array():

    b = []
    while 1:
        a = int(input("Введите число. Список будет заполнятся пока не введете 0: "))
        if a != 0:
            b.append(a)
        else:
            break
    return b


array_New = Create_New_Array()
print(f"Наш изначальный массив = {array_New}")


def Sum_Create_New_Array(array):
    sum_Creat = []
    for i in range(len(array)//2):
        x = array[i] * array[-1 - i]
        sum_Creat.append(x)
    if len(array) % 2:
        sum_Creat.append(array[(len(array)//2)]**2)

    return sum_Creat


print(Sum_Create_New_Array(array_New))
