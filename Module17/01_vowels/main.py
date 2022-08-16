vowels_len = ["а", "о", "у", "э", "ы", "я", "ё", "ю", "е", "и"]
vowels_list = []


text = input('Введите текст: ')

for i in text:
    for vowels in vowels_len:
        if vowels == i:
            vowels_list.append(vowels)

print('Список гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))