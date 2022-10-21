# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input('Задайте натуральную степень k: '))
# k = randint(0, 10)
ratios = [randint(0, 100) for i in range(k + 1)]
if ratios[k] == 0:
    ratios[k] = randint(1, 100)
polynom = ''
if k != 0:
    for i in range(k + 1):
        if i > 1 and ratios[i] != 0:
            if ratios[i] > 1:
                polynom = f' + {ratios[i]}*x^{i}' + polynom
            else:
                polynom = f' + x^{i}' + polynom
        elif i == 1 and ratios[i] != 0:
            if ratios[i] > 1:
                polynom = f' + {ratios[i]}*x' + polynom
            else:
                polynom = ' + x' + polynom
        elif i < 1:
            if ratios[i] > 0:
                polynom += f' + {ratios[i]} = 0'
            else:
                polynom += ' = 0'
    print(polynom[3::])
else:
    print('0 = 0')
