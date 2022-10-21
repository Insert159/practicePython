

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

print("Задача 4")
import random
def рolynomial():
    try:
        k = int(input("Введите натуральную степень: "))
        a = int(random.randint(0, 100))
        b = int(random.randint(0, 100))
        c = int(random.randint(0, 100))
    except ValueError:
        print("Некорректный ввод")
        print()
        рolynomial()
    else:
        if a != 0:
            one = (str(a) + "x^" + str(k) + " + ")
        else:
            one = (str())

        if b != 0:
            two = (str(b) + "x" + " + ")
        else:
            two = (str())

        if c != 0:
            three = (str(c) + " = 0")
        else:
            three = (str())
        my_file = open("1.txt", "w+")
        my_file.write(f"{one}{two}{three}")
        my_file.close()
рolynomial()
print("Ответ в файле 1.txt")
