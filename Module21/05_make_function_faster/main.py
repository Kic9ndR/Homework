def calculating_math_func(data: int):
    if data == 0:
        return 1
    return calculating_math_func(data - 1) * data


dict_nums = {}


while True:         #Решил сделать бесконечный цикл, потому-что не хотелось стоп-слово придумывать :)
    number = int(input('Введите число: '))
    if number in dict_nums:
        print(dict_nums[number])
    else:
        result = (calculating_math_func(number) // number) ** 10
        print(result)
    dict_nums[number] = result
