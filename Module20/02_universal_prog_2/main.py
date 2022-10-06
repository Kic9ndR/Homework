def is_prime(text):
    crypto = []
    for i_num, meaning in enumerate(text):
        check = True
        if i_num == 0:
            check = False
        for i in range(2, (i_num // 2) + 1):
            if i_num % i == 0:
                check = False
                break
        if check == True:
            crypto += str(meaning)
    return crypto

print(is_prime('О Дивный Новый мир!'))