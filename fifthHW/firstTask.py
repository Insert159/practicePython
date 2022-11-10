#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print('***Задача 1***')
text = 'забвение ручка зимбабве кружка абвер'
print(text)
print(' '.join(list(filter(lambda word: not word.__contains__('абв'), text.split()))))




#Конец!