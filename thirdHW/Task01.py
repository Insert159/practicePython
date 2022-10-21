# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random


def Create_Elemnt_List():
    count_X = int(input("Введите количество чисел в массиве: "))

    array = []
    for i in range(count_X):
        x = int(random.random()*10)
        array.append(x)

    return array


a = Create_Elemnt_List()
print(f"Наш рандомный массив {a}")


def sum_Element_List(array):
    sum_Elemnt = 0
    for i in range(len(array)):
        if i % 2 != 0:
            sum_Elemnt += array[i]
    return sum_Elemnt


print(f"Сумма нечетных элементов массива = {sum_Element_List(a)}")
