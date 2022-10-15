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











# Требуется найти наименьший натуральный делитель целого числа N, 
# отличный от 1.

# Пример:

# - Для n = 15:  Ответ: 3
# - Для n = 35:  Ответ: 5

# n = int(input())
# i = 1
# while i <= n:
#     i = i + 1
#     if n % i == 0:
#         print(i)
#         break











# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]


def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def Summa(x,y,z):
    l = range(-x,x+1)
    l = list(l)
    summ = l[y] * l[z]
    print(f'Список элементов:')
    print(l)
    print(f'Произведение цифр под индексами: ', y, 'и', z, 'равно', summ)
        
num = InputNum('Введите количество элементов (N): ')

pos1 = InputNum('Введите первое число: ')
while (((num*2) + 1) < pos1) or (pos1 < 1):
    print('Первое число находиться за пределами диапазона')
    pos1 = InputNum('Введите первое число: ')

pos2 = InputNum('Введите второе число: ')
while (((num*2) + 1) < pos2) or (pos1 < 1):        
    print('Второе число находиться за пределами диапазона')
    pos2 = InputNum('Введите второе число: ') 

Summa(num,pos1,pos2)








# Требуется посчитать сумму чётных чисел, расположенных 
# между числами 1 и N включительно.

# number = int(input('Введите число N: '))

# sum = 0
# for i in range(2, number + 1):
#     if  not i % 2:
#         sum += i
#         if i != 2:
#             print(' + ', end='')
#         print(i, end='')
# print(f' = {sum}')