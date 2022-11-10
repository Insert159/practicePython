def double_digit():
    nums = list(map(int, input('Введите числа через пробел:').split()))
    return ' '.join(map(str, filter(lambda i: 9 < abs(i) < 100, nums)))

print(f'[{double_digit()}]') # пример расходится с условием задачи, вывод организовал как в тексте: одной строкой через пробел.