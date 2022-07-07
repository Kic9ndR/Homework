def number_back(n):
    parts = str(n).split('.')
    parts[0] = ''.join(reversed(list(str(parts[0]))))
    parts[1] = ''.join(reversed(list(str(parts[1]))))
    return float(parts[0] + '.' + parts[1])


first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))

first_back = number_back(first)
second_back = number_back(second)

print('Первое число наоборот:', first_back)
print('Второе число наоборот:', second_back)
print('Сумма:', first_back + second_back)