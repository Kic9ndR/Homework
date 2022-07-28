lst_one = []
lst_two = []

for i in range(3):
    query = 'Введите ' + str(i + 1) + ' число для первого списка: '
    number = int(input(query))
    lst_one.append(number)
print()

for i in range(7):
    query = 'Введите ' + str(i + 1) + ' число для второго списка: '
    number = int(input(query))
    lst_two.append(number)


print('\nПервый список:', lst_one)
print('Второй список:', lst_two)

lst_one.extend(lst_two)
for _ in range(len(lst_one)):
    for i in lst_one:
        if lst_one.count(i) > 1:
            lst_one.remove(i)

print("\nНовый первый список с уникальными элементами:", lst_one)