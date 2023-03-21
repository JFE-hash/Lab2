from random import randint


range = [i for i in range(1, 1001)]
mistakes = 0
goods = 0
while mistakes < 3:
    n1 = randint(1, len(range))
    n2 = randint(1, len(range))
    answer = int(input(f'{n1} + {n2} = '))
    if answer != n1 + n2:
        mistakes += 1
        print('Ответ неверный :(')
    else:
        goods += 1
        print('Правильно!')
print(f'Игра окончена! Правильных ответов: {goods}')
