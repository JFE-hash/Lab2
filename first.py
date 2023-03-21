print('Введите слова по порядку: ')
stroke = ''
word = ''
while word != 'stop':
    word = input()
    stroke += word
print('Получившаяся строка:', stroke)