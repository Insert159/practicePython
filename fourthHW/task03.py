
#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

print("Задача 3")
list1 = [1, 2, 2, 3, 3, 4, 5]
print("Список: ", list1)
unique = list(set(list1))
print("Список уникальных элементов списка: ", unique)