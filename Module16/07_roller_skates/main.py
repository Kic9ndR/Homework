skates = []
foot_size = []
count = 0

number = int(input('Кол-во коньков: '))
for i in range(number):
    query = 'Размер ' + str(i + 1) + ' пары: '
    size = int(input(query))
    skates.append(size)

number = int(input('\nКол-во людей: '))
for i in range(number):
    query = 'Размер ноги ' + str(i + 1) + ' человека: '
    size = int(input(query))
    foot_size.append(size)
print()


for foot in foot_size:
    if foot in skates:
        skates.remove(foot)
        count += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', count)