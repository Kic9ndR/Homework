def guest_come():
    name = input('Имя гостя: ')
    if len(guests) < 6:
        print('Привет,', name + '!')
        guests.append(name)
    else:
        print('Прости,', name + ', но мест нет.')

    return guests


def guest_left():
    name = input('Имя гостя: ')
    if guests.count(name) != 0:
        guests.remove(name)
        print('Пока,', name + '!')
    else:
        print('Такого человека нет на вечеринке')

    return guests


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    come_or_left = input('Гость пришел или ушел? ')
    if come_or_left == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    elif come_or_left == 'пришел':
        guest_come()
    elif come_or_left == 'ушел':
        guest_left()
    else:
        print('Неверно написано действие, попробуй еще раз')
    print()