violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def count_time_songs(songs):
    count_time = []
    summ = 0
    for new_songs in songs:
        for i in violator_songs:
            if i[0] == new_songs:
                count_time.append(i[1])
    for summ_minute in count_time:
        summ += summ_minute
    print('Общее время звучания песен:', round(summ, 2), 'минуты')


count_songs = int(input('Введите кол-во выбираемых песен: '))

songs = []
for i in range(count_songs):
    print('Название', str(i + 1) + '-й песни:', end=' ')
    name = input()
    songs.append(name)


print()
count_time_songs(songs)