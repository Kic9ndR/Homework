piople = int(input('Кол-во человек: '))
dropped = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', dropped, 'человек.')
piople_list = list(range(1, piople + 1))
out = 0

for _ in range(piople - 1):
    print('\nТекущий круг людей', piople_list)
    start_count = out % len(piople_list)
    out = (start_count + dropped - 1) % len(piople_list)
    print('Начало счёта с номера', piople_list[start_count])
    print('Выбывает человек под номером', piople_list[out])
    piople_list.remove(piople_list[out])

print('\nОстался человек под номером', piople_list)