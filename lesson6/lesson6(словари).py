'''
Синтаксис словарей
dictionary = {ключ1: значение1, ключ2: значение2}

альтернативный синтаксис
dictionary = {
    ключ1: значение1,
    ключ2: значение2,
}

КЛЮЧЕМ МОЖЕТ БЫТЬ ВСЕ, КРОМЕ СТРУКТУР ДАННЫХ
'''

dictionary = {
    8 : 'восемь',
    True: False,
    'hi' : 'hello',
    10 : [2,3,5],
    1 : { 1 : 'one'}
}

# Чтобы обратиться к словарю, надо написать его ключ. 1 - True
print(dictionary[8], dictionary[True])
# Можно работать с ключами словаря и его значениями
dictionary[8] = 'eight'
print(dictionary[8])

if 8 in dictionary:
    dictionary[8] += ' zero'
else:
    print('Ключ не найден')

print(dictionary[8])

# Для удаления надо писать del