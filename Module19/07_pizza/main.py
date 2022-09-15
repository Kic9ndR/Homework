count_order = int(input('Введите кол-во заказов: '))
orders_date = dict()


for i in range(1, count_order + 1):
    surname, pizza, amount = input(f'{i} заказ: ').rsplit(maxsplit=3)
    amount = int(amount)
    if surname not in orders_date:
        orders_date[surname] = {pizza: amount}
    else:
        if pizza not in orders_date[surname]:
            orders_date[surname][pizza] = amount
        else:
            orders_date[surname][pizza] += amount

for client in orders_date:
    print(f"{client}:")
    for all_pizza in orders_date[client]:
        print('       ', all_pizza, orders_date[client][all_pizza])