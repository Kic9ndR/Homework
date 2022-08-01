def balance_of_debt_receipts():
    for c in range(count_promissory_notes):
        print()
        print(str(c + 1) + '-я расписка')
        to_whom = int(input('Кому: '))
        from_whom = int(input('От кого: '))
        count = int(input('Сколько: '))
        balance[to_whom - 1] -= count
        balance[from_whom - 1] += count
    num = 1
    print('\nБаланс друзей:')
    for f in balance:
        print(str(num) + ':', f)
        num += 1



count_friend = int(input('Кол-во друзей: '))
balance = []
for i in range(1, count_friend + 1):
    balance.append(0)


count_promissory_notes = int(input('Долговых расписок: '))


balance_of_debt_receipts()