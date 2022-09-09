violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_time = 0
count_songs = int(input('Сколько песен выбрать: '))
for i in range(count_songs):
    name_songs = input("Название {0}-й песни: ".format(i + 1))
    count_time += violator_songs[name_songs]


print(f'Общее время звучания: {round(count_time, 2)} минут')