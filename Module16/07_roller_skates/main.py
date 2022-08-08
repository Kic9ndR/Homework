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


count_skates = 0
for index in skates:
    count_skates += skates.count(index)
    if foot_size.count(index) > 0:
        count += 1
        foot_size.remove(index)
    for foot in foot_size:
        if index >= foot:
            if count_skates >= count:
                count += 1
                foot_size.remove(foot)
            else:
                break
    skates.remove(index)


print('Наибольшее кол-во людей, которые могут взять ролики:', count)