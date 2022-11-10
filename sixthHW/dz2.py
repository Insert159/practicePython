# Орел и решка. Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

list_text = open('file_text.txt', 'w')
list_text.write('ООРОРООРРРРООРРООРРОООРР')
list_text.close()

list_text = open('file_text.txt', 'r')
list_OP = list_text.readline()
list_text.close()

n = list(filter(lambda x: x == 'Р', [i for i in list_OP]))
print(len(n))