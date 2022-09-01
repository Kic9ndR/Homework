text = input('Доступное меню: ').replace('; ', ';').split(';')

print('\nНа данный момент в меню есть:', ', '.join(text))