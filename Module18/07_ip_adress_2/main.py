IP = input('Введите IP: ').split('.')

for i in IP:
    if ',' in i:
        print('Адрес - это четыре числа, разделенные точками.')
        break
    elif i.isdigit() != True:
        print(i, '- это не целое число.')
        break
    elif int(i) > 255:
        print(i, 'превышает 255.')
        break
else:
    print('IP-адрес корректен.')