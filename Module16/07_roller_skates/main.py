skates = []
foot_size = []
count = 0

number = int(input('Кол-во роликов: '))
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


for foot in sorted(foot_size):
    for suitable in sorted(skates):
        if suitable >= foot:
            count += 1
            skates.remove(suitable)
            break
    foot_size.remove(foot)

print('Наибольшее кол-во людей, которые могут взять ролики:', count)