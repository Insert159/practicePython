# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности

arr = [int(i) for i in input('Введите числа через пробел:\n').split()]
print(arr)
new_arr = []
[new_arr.append(i) for i in arr if i not in new_arr]
print(new_arr)
