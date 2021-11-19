"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
 Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(**kwargs):
    with open('orders.json') as f_n:
        data = json.load(f_n)
    data['orders'].append(kwargs)
    with open('orders.json', 'w') as file:
        json.dump(data, file, indent=4)


order = {'item': 'Notebook', 'quantity': 3, 'price': 10000, 'buyer': 'Ivanon', 'date': '19.11.2021'}

write_order_to_json(**order)

