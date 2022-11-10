
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

print('***Задача 5***')
file1 = open("исходная строка.txt", "r")
lines = file1.readlines()
file1.close()
for line in lines:
    print(line.strip())
def encode(s):
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding
#print(encode(s))
for line in lines:
    print(encode(line.strip()))
text_file = open("полученная строка.txt", "w")
n = text_file.write(encode(line.strip()))
text_file.close()