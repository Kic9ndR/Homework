def check_len():
    global text, number_tuple
    result = 0
    len_range = len(text)
    len_turple = len(number_tuple)
    if len_range != len_turple:
        print('Данные имеют разную длину.')
        if len_range < len_turple:
            print('Кортеж будет урезан до длинны строки.')
            result = -1
        else:
            print('Строка будет урезана до длинны кортежа.')
            result = 1
            len_range = len_turple
    return result, len_range


def gen_pair():
    global text, number_tuple, pair
    len_data = check_len()
    for i in range(len_data[1]):
        tmp_pair = (text[i], number_tuple[i])
        pair.append(tmp_pair)
    print(pair)


pair = []
text = input('Строка: ')
number = input('Кортеж чисел: ').replace('(', '').replace(')', '').replace(' ', '').split(',')
number_tuple = tuple(int(num) for num in number)

gen_pair()
