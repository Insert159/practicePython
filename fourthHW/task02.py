#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Задача 2")
n=int(input("Введите число: "))
print(f"Простые множетели введенного числа: ")
for i in range(1, n+1):
    if(n%i==0):
        print(i)