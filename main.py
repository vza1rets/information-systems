from datetime import datetime, time

inputDish_str = '"Плов узбекский" 350.75 01.30'
inputMenu_str = '"Летнее меню" "Основные блюда" 2024.06.01 True'
inputOrder_str = '1543 "Плов узбекский" 2 14.30 701.50'


def trytoparse_dish(input_str):
    parts = input_str.split('"')
    dish_name = parts[1]

    rest = parts[2].split()
    price = float(rest[0])

    time_parts = rest[1].split('.')
    cooking_time = time(int(time_parts[0]), int(time_parts[1]))

    result = f"Блюдо: {dish_name}, Цена: {price}, Время приготовления: {cooking_time.strftime('%H:%M')}"
    return result


def trytoparse_menu(input_str):
    parts = input_str.split('"')
    menu_name = parts[1]
    category = parts[3]

    rest = parts[4].split()
    date_str = rest[0]
    date = datetime.strptime(date_str, "%Y.%m.%d")
    is_seasonal = rest[1] == 'True'

    result = f"Меню: {menu_name}, Категория: {category}, Дата создания: {date.strftime('%Y.%m.%d')}, Сезонное: {is_seasonal}"
    return result


def trytoparse_order(input_str):
    parts = input_str.split('"')
    order_id = int(parts[0])
    dish_name = parts[1]

    rest = parts[2].split()
    quantity = int(rest[0])

    time_parts = rest[1].split('.')
    order_time = time(int(time_parts[0]), int(time_parts[1]))

    total_price = float(rest[2])

    result = f"Заказ №: {order_id}, Блюдо: {dish_name}, Количество: {quantity}, Время заказа: {order_time.strftime('%H:%M')}, Итого: {total_price}"
    return result


print(trytoparse_dish(inputDish_str))
print(trytoparse_menu(inputMenu_str))
print(trytoparse_order(inputOrder_str))