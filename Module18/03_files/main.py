import string

file = input('Название файла: ').lower()
extention = ('.txt', '.docx')
if file[0] in string.punctuation:
    print('Ошибка. Название начинается на один из специальных символов.')
elif not file.endswith(extention):
    print('Ошибка: Неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно')