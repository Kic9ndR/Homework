def hanoi(amount, start, finish):
    if amount <= 0:
        return
    interim = 6 - start - finish
    hanoi(amount - 1, start, interim)
    print(f"Переложить диск {amount} со стержня {start} на стержень {finish}")
    hanoi(amount - 1, interim, finish)

count = int(input('Введите количество дисков: '))
first_rod = int(input("Введите стартовый стержень: "))
hanoi(count, first_rod, 3)
