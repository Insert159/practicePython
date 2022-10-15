# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


# def sumNumber():
#     try:
#         sum = 0
#         number = input(
#             "Введите любое число и получите сумму его цифр: ").replace(
#                 ".", "").replace("-", "")

#         for i in number:
#             sum += int(i)
#     except ValueError:
#         print("Вы ввели не число попробуйте еще раз")


#         sumNumber()
#     return sum


# print(f"Сумма введенного числа = {sumNumber()}")










# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def arrayMultip():
#     try:
#         array = []
#         sum = 1
#         number = int(input("Введите целое число от 1 до N: "))
#         for i in range(1, number+1):
#             sum *= i
#             array.append(sum)
#         if number < 0:
#             print("Вы ввели отрицательное число. Введите положительное целое! ")
#             arrayMultip()
#     except ValueError:
#         print("Вы ввели не то введите целое число")
#         arrayMultip()
#     return array


# print(*arrayMultip())












# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def arrayRezult():
#     try:
#         array = []
#         number = int(input("Введите  число : "))
#         for n in range(1, number+1):
#             sum = (1 + 1/n)**n
#             array.append(round(sum, 4))
#         if number < 0:
#             print("Вы ввели отрицательное число. Введите положительное целое! ")
#             arrayRezult()
#     except ValueError:
#         print("Вы ввели не то введите целое число")
#         arrayRezult()
#     return array


# a = arrayRezult()
# print(*a)


# def sumArray(array):
#     sum = 0
#     for i in array:
#         sum += i
#     return sum


# print(f"Сумма чисел = {sumArray(a)}")





# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def split(s):
    return [int(i) for i in s]


def readFile():
    file = open("text.txt", "rt", encoding="utf-8")
    array = file.read()
    b = split(array)
    file.close()
    return b


b = readFile()


def rezultArrayMulti(ar):
    try:
        array = []
        number = int(input("Введите  число N: "))
        multi = 1
        if number < 0:
            print("Введите целое положительное число!!!!")
            rezultArrayMulti(ar)
        for n in range(-number, number+1):
            array.append(n)
        print(f"Массив в фаиле = {ar}")
        print(f"Наш созданный массив от -N до N = {array}")
        for i in range(len(ar)):
            for j in range(len(array)):

                if ar[i] == j:
                    multi *= array[j]

    except ValueError:
        print("Вы ввели не то введите целое число")
        rezultArrayMulti(ar)
    return multi


print(f"Наш результат = {rezultArrayMulti(b)}")




# Реализуйте алгоритм перемешивания списка.


# def createList():
#     try:
#         array = []
#         number = int(input("Введите  размерность списка N: "))
#         if number < 0:
#             print("Введите целое положительное число!!!!")
#             createList()
#         for n in range(number+1):
#             array.append(n)

#     except ValueError:
#         print("Вы ввели не то введите целое число")
#         createList()
#     return array


# a = createList()
# print(f"Наш созданый массив = {a}")


# def mixArray(array):
#     newArray = []

#     for i in array:
#         if i % 2 == 0:
#             newArray.append(array[i])

#     for j in array:
#         if j % 2 != 0:
#             newArray.append(array[j])
#     b = newArray[::-1]

#     return b


# b = print(f"Перемешанный список = {mixArray(a)}")