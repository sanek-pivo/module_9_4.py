# 1 задание. lambda - функция
print()
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda a, b: a == b, first, second))
print(result)
print()

# 2 задание. Замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write("%s\n" % item)

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3 задание. Метод __call__

import random
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        elem = random.choice(self.words)
        return elem


first_ball = MysticBall('Ковер', 'Самолет', 'Летим', 'Полетим', 'Пляшем')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())