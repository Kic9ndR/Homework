import random


count_sticks = int(input('Количество палок: '))
count_throw = int(input('Количество бросков: '))

result = ['I' for _ in range(count_sticks)]
downed_sticks = [random.randint(1, count_sticks) for _ in range(2)]
for i in range(count_throw):
    downed_sticks = [random.randint(1, count_sticks) for _ in range(2)]
    print('Бросок', str(i + 1) + '.', 'Сбиты палки с номерами', min(downed_sticks), 'по номер', max(downed_sticks))
    result[min(downed_sticks):max(downed_sticks)] = ['.' for _ in range(min(downed_sticks), max(downed_sticks))]

print('Результат:', result)