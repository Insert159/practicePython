# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), применив лямбды, filter, map, zip, enumerate, списочные выражения.
# Seminar 2, Task 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input('Введите вещественное число: ')

from functools import reduce

sum = reduce(lambda x, y: x + y, [int(i) for i in n])
print(sum)