

#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

print('***Задача 2***')
from random import randint
сandies = 2021
m = 28
def game(Q, step):
    i = randint(1, 2)
    j = 2
    if i == j:
        j = 1
    while Q > 0:
        winner = ""
        if Q > 0 and Q <= step:
            user1 = Q
        else:
            user1 = randint(1, step)
        Q = Q - user1
        print(Q , i, end = ' ')
        if Q == 0:
            winner = "Выиграл игрок №" + str(i)
        if Q > 0 and Q <= step:
            user2 = Q
        else:
            user2 = randint(1, step)
        Q = Q - user2
        print(Q, j, end = ' ')
        if Q == 0:
            winner = "Выиграл игрок  №" + str(j)
    return winner
print(game(сandies, m))

#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

print('***Задача 3***')
def game2(Q, step):
    winner2 = ""
    i = randint(1, 2)
    print(i)
    while Q > 0:
        if i == 1:                     
            if Q <= step:
                human = Q
            else:
                human = randint(1, step)
            Q = Q - human
            print(Q, "человек", end = ' ')
            if Q == 0:
                winner2 = "Выиграл человек"                      
            bot = Q % (step + 1)
            if bot == 0:
                bot = randint(1, step)
            Q = Q - bot
            print(Q, end = ' ')
            if Q == 0:
                winner2 = "Выиграл bot"
        else:                        
            bot = Q % (step + 1)
            Q = Q - bot
            print(Q, end = ' ')
            if Q == 0:
                winner2 = "Выиграл bot"
            human = randint(1, step)
            Q = Q - human
            print(Q, end = ' ')
            if Q == 0:
                winner2 = "Выиграл человек"
    return winner2

print(game2(сandies, m))