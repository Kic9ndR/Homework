import random

error = ['Я устал, я ухожу...',
         'Ой, скучно с тобой, пока!',
         'Упс, что-то пошло не так.']

summ = 0
with open('out_file.txt', 'w', encoding='utf-8') as num_file:
    while True:
        if 13 == random.randint(1, 13):
            raise ValueError(random.choice(error))
        num = int(input('Введите число: '))
        summ += num
        num_file.write(f'{num}\n')
        if summ >= 777:
            print('Тебе повезло, но это только в этот раз')
            break