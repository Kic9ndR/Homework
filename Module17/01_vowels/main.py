vowels_len = "аоуэыяёюеи"

text = input('Введите текст: ')

vowels_list = [vowels for vowels in text if vowels in vowels_len]

print('Список гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))