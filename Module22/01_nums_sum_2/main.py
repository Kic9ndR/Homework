count = 0
tmp_str = ''

with open('numbers.txt') as file:
    print('Содержимое файла numbers.txt')
    for row in file.readlines():
        print(row, end='')
        tmp_str = row.strip()
        if tmp_str != '':
            count += int(tmp_str)

f = open('answer.txt', 'w')
f.write(str(count))
print(f'\nСодержимое файла answer.txt\n{count}')
f.close()