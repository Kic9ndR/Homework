goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for product_name, product_code in goods.items():
    total_cost = 0
    total_product = 0
    for products in store[product_code]:
        item_product = products['quantity']
        item_cost = products['price']
        total_product += item_product
        total_cost += item_product * item_cost
    print('{0} - {1} штук, стоимость {2} рубля'.format(product_name, total_product, total_cost))