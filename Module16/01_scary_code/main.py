main = [1, 5, 3]
side_list_fi = [1, 5, 1, 5]
side_list_se = [1, 3, 1, 5, 3, 3]

main.extend(side_list_fi)
count_five = main.count(5)
print('Кол-во цифр 5 при первом объединении:', count_five)
for _ in range(count_five):
    main.remove(5)

main.extend(side_list_se)
count_three = main.count(3)
print('Кол-во цифр 3 при втором объединении:', count_three)

print('Результат работы программы:')
print("Кол-во цифр 5 при первом объединении:", count_five)
print('Кол-во цифр 3 при втором объединении:', count_three)
print('Итоговый список:', main)