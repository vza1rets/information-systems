from datetime import datetime, time


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


def main():
    print('file or string?')
    typee = input()
    strings = []
    if typee.lower() == 'file':
        path = input('Введите путь к файлу: ')
        try:
            with open(f'{path}', encoding='utf-8') as f:
                strings = f.readlines()
                strings = [line.rstrip() for line in strings]
        except:
            print('Не удалось открыть файл')
    elif typee.lower() == 'string':
        print('Введите строку')
        strings.append(input())

    print('Какой тип объектов? (dish/menu/order)')
    object_type = input().lower()

    for string in strings:
        if string.strip():
            if object_type == 'dish':
                print(trytoparse_dish(string))
            elif object_type == 'menu':
                print(trytoparse_menu(string))
            elif object_type == 'order':
                print(trytoparse_order(string))
            else:
                print("Неизвестный тип объекта")


if __name__ == "__main__":
    main()