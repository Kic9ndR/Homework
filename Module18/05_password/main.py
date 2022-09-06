count_num = 0
count_upper = 0
len_pass = False


while True:
    password = input('Придумайте пароль: ')
    if len(password) >= 8:
        len_pass = True
        for i in password:
            if i.isupper() == True:
                count_upper += 1
            elif i.isdigit() == True:
                count_num += 1
    if count_num >= 3 and count_upper >= 1 and len_pass == True:
        print('Это надежный пароль!')
        break
    else:
        print('Это ненадежный пароль. Попробуйте еще раз.', end='\n')
        count_num = 0
        count_upper = 0
        len_pass = False


