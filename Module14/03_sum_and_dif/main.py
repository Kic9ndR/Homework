def calc_number(n):
    s = list(str(n))
    s = list(map(int, s))
    return sum(s)


def len_number(n):
    return len(str(n))


number = int(input('Введите число: '))

calc_num = calc_number(number)          #Для удобства нахождения разности
len_num = len_number(number)

print('Сумма цифр:', calc_num)
print('Кол-во цифр в числе:', len_num)
print('Разность суммы и кол-ва цифр:', calc_num - len_num)