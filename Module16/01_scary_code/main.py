main = [1, 5, 3]
side_list_fi = [1, 5, 1, 5]
side_list_se = [1, 3, 1, 5, 3, 3]

main.extend(side_list_fi)

count_fives = 0
count_tiple = 0
for i in main:
    if i == 5:
        count_fives += 1
        main.remove(5)

main.extend(side_list_se)
for c in main:
    if c == 3:
        count_tiple += 1

print('Результат работы программы:')
print("Кол-во цифр 5 при первом объединении:", count_fives)
print('Кол-во цифр 3 при втором объединении:', count_tiple)
print('Итоговый список:', main)

#Закинуть в main второй список и посчитать кол-во 3-ек + вывести на экран ответ