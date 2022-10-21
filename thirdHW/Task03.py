# 3.Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

def Create_New_Array():
    try:
        b = []
        while 1:
            a = float(
                input("Введите число вещественное. Список будет заполнятся пока не введете 0: "))

            if a != 0.0:
                a = round((a % 1), 3)
                if a != 0.0:
                    b.append(a)
            else:
                break
    except ValueError:
        print("Вы ввели не число повторите")
        Create_New_Array()
    return b


ar = Create_New_Array()


def search_Differ_in_Array(array):
    array_Max = array[0]
    array_Min = array[0]

    for elem in array:
        if elem > array_Max:
            array_Max = elem
        if elem < array_Min:
            array_Min = elem
    c = array_Max - array_Min
    return c


ar1 = search_Differ_in_Array(ar)
print(ar1)
