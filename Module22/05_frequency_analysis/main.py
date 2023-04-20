from operator import itemgetter

def letter_dict(string):
    dict_letters = {}
    amount_letter = len(string)
    for i in string:
        counter = string.count(i)
        counter /= amount_letter
        dict_letters[i] = counter
    letter_ratio(dict_letters)
    return dict_letters

def letter_ratio(dict):
    analysis = open('analysis.txt', 'w', encoding='utf-8')
    sort_dict = sorted(dict.items(), key=itemgetter(1), reverse=True)
    for key, value in sort_dict:
        analysis.write(f'{key} {round(value, 3)}\n')
    analysis.close()


text = open('text.txt', 'r', encoding='utf-8')
pure_str = text.read().strip('.').replace(' ', '').lower()
text.close()
text = open('text.txt', 'r', encoding='utf-8')
print(f'Содержимое файла text.txt:\n{text.read()}\n')
text.close()

letter_dict(pure_str)
analysis = open('analysis.txt', 'r', encoding='utf-8')
print(f'Содержимое файла analysis.txt:\n{analysis.read()}')
analysis.close()
