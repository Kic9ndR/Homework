import random

original_list = [random.randint(0, 9) for _ in range(10)]

print('Оригинальный список:', original_list)

# Вариант 1
buf_dict_1, buf_dict_2, result_2 = [], [], []

for i_index, i_value in enumerate(original_list):
    if i_index % 2 == 0:
        buf_dict_1.append(i_value)
    else:
        buf_dict_2.append(i_value)

result = zip(buf_dict_1, buf_dict_2)
for i in result:
    result_2.append(i)
print('Новый список:', result_2)

# Вариант 2
zip_list = zip(original_list[::2], original_list[1::2])
new_list = []
for i in zip_list:
    new_list.append(i)

print('Новый список:', new_list)

# Вариант 3
result_2 = [*map(tuple, zip(original_list[::2], original_list[1::2]))]
print('Новый список:', result_2)
