def cycle(num):
    if num <= 0:
        return 1
    else:
        cycle(num - 1)
        return print(num)

input_num = int(input('Введите число: '))

cycle(input_num)