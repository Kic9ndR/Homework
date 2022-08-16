import random

count_num = int(input('Кол-во чисел в списке: '))
num_list = [random.randint(0, 2) for _ in range(count_num)]

print('Список до сжатия:', num_list)

num_list = [i for i in num_list if i > 0]
print('Список после сжатия:', num_list)