# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv


import random


def generate_random_name():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        random_word1 = [random.choice(chars) for i in range(0, random.randint(1, 15))]
        random_word2 = [random.choice(chars) for i in range(0, random.randint(1, 15))]
        yield f"{''.join(random_word1)} {''.join(random_word2)}"


r = generate_random_name()

print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))


