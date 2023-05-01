count_sim = 0
broke_line = 0

with open('people.txt', 'r', encoding='utf-8') as people:
    for i in people:
        try:
            broke_line += 1
            len_name = len(i.strip('\n'))
            if len_name < 3:
                raise ValueError
            else:
                count_sim += len_name
        except ValueError:
            print(f'Ошибка возникла в {broke_line} строке: '
                  f'менее 3-х символов')

print('Общее количество символов:', count_sim)