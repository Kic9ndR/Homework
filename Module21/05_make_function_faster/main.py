
def calculating_math_func(data: int):
    if data == 0:
        return 1
    return calculating_math_func(data - 1) * data

number = int(input('Введите число: '))

result = (calculating_math_func(number) // number) ** 10
print(result)
