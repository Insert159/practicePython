

#Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

print("Задача 5")
polynomial1 = f"{11}x^2 + {27}x + {34}"
print("Первый многочлен:", polynomial1)
polynomial2 = f"{32}x^2 + {16}x + {54}"
print("Второй многочлен:", polynomial2)

with open("f1.txt", "w") as data:
   data.write(polynomial1)
with open("f2.txt", "w") as data:
   data.write(polynomial2)

first_coef_polynomial_1 = int(polynomial1[0] + polynomial1[1])
second_coef_polinomial_1 = int(polynomial1[8] + polynomial1[9])
third_coef_polinomial_1 = int(polynomial1[14] + polynomial1[15])

first_coef_polynomial_2 = int(polynomial2[0] + polynomial2[1])
second_coef_polinomial_2 = int(polynomial2[8] + polynomial2[9])
third_coef_polinomial_2 = int(polynomial2[14] + polynomial2[15])

result1_coef = str(first_coef_polynomial_1 + first_coef_polynomial_2)
result2_coef = str(second_coef_polinomial_1 + second_coef_polinomial_2)
result3_coef = str(third_coef_polinomial_1 + third_coef_polinomial_2)

result = f"{result1_coef}x^2 + {result2_coef}x + {result3_coef}"
with open("result", "w") as data:
    data.write(result)
print("Сумма многочленов:", result)