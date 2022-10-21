#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

print("Задача 1")
from math import pi
d = int(input("Введите точность c которой хотите получить число Пи: "))
str1 = str(pi)
lst = []
for i in range(d + 2):
    lst.append(str1[i])
pi = "".join(lst)
print(f"Число Пи с заданной точностью {d} равно {pi}")

