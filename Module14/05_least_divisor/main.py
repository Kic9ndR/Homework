def devider(num):
    for devider in range(2, num + 2):
        if num % devider == 0:
            print('Наименьший делитель, отличный от единицы:', devider)
            return


number = int(input('Введите число: '))
while number <= 0:
    print('Неверное значение! Повторите попытку')
    number = int(input('Введите число: '))

devider(number)