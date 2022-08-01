number = int(input('Кол-во чисел: '))
arr = []

for i in range(number):
    query = str(i + 1) + ' число: '
    arr.append(int(input('Число: ')))
print('\nПоследоваельность:', arr)

counter = 0
while arr != arr[::-1]:
    arr.insert(number, arr[counter])
    counter += 1


print('Нужно приписать чисел:', counter)
print('Сами числа:', arr[:counter][::-1])