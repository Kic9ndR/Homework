origin_dict = dict()
replay = 0


text = input('Введите текст: ')
for i in text:
    replay += 1
    if origin_dict.get(i) != None:
        replay += 1
    origin_dict[i] = replay
    replay = 0

print('Оригинальный словарь частот:')
for key, value in sorted(origin_dict.items()):
    print(f'{key} : {value}')