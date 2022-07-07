def three_digits(y1, y2):
    for i in range(y1, y2 + 1):
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a == b == c or b == c == d or c == d == a or a == b == d:
            print(i)


years = int(input('Введите первый год: '))
years2 = int(input('Введите второй год: '))
print(f'Года от {years} до {years2} с тремя одинаковыми цифрами:')
three_digits(years, years2)