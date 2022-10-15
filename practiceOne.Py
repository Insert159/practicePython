# Напишите программу, которая принимает на вход два числа и
# проверяет, является ли одно число квадратом другого.
# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


# Найти максимум из 5

# list = input().split()
# list.sort(key=int)
# print(list[len(list)-1])


lst = []
for i in range(5):
    lst.append(int(input('Введите число ')))
a = 0
for i in lst:
    if i > a:
        a = i
print(a)
