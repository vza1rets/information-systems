from datetime import datetime, time, date


class Dish:
    def __init__(self, dish_name: str, price: float, cooking_time: time):
        self.dish_name = dish_name
        self.price = price
        self.cooking_time = cooking_time

    def __str__(self):
        return (f"Блюдо: {self.dish_name}, Цена: {self.price}, Время приготовления: {self.cooking_time.strftime('%H:%M')}")


class Menu:
    def __init__(self, menu_name: str, category: str, datee: date, is_seasonal: bool):
        self.menu_name = menu_name
        self.category = category
        self.datee = datee
        self.is_seasonal = is_seasonal

    def __str__(self):
        return (
            f"Меню: {self.menu_name}, Категория: {self.category}, Дата создания: {self.datee.strftime('%Y.%m.%d')}, Сезонное: {self.is_seasonal}")


class Order:
    def __init__(self, order_id: int, dish_name: str, quantity: int, order_time: time, total_price: float):
        self.order_id = order_id
        self.dish_name = dish_name
        self.quantity = quantity
        self.order_time = order_time
        self.total_price = total_price

    def __str__(self):
        return (
            f"Заказ №: {self.order_id}, Блюдо: {self.dish_name}, Количество: {self.quantity}, Время заказа: {self.order_time.strftime('%H:%M')}, Итого: {self.total_price}")


def trytoparse_dish(input_str):
    parts = input_str.split('"')
    dish_name = parts[1]

    rest = parts[2].split()
    price = float(rest[0])

    time_parts = rest[1].split('.')
    cooking_time = time(int(time_parts[0]), int(time_parts[1]))

    return Dish(dish_name, price, cooking_time)


def trytoparse_menu(input_str):
    parts = input_str.split('"')
    menu_name = parts[1]
    category = parts[3]

    rest = parts[4].split()
    date_str = rest[0]
    date_obj = datetime.strptime(date_str, "%Y.%m.%d").date()
    is_seasonal = rest[1] == 'True'

    return Menu(menu_name, category, date_obj, is_seasonal)


def trytoparse_order(input_str):
    parts = input_str.split('"')
    order_id = int(parts[0].strip())

    dish_name = parts[1]

    rest = parts[2].split()
    quantity = int(rest[0])

    time_parts = rest[1].split('.')
    order_time = time(int(time_parts[0]), int(time_parts[1]))

    total_price = float(rest[2])

    return Order(order_id, dish_name, quantity, order_time, total_price)


def get_input_data():
    print('file or string?')
    typee = input()
    strings = []

    if typee.lower() == 'file':
        path = input('Введите путь к файлу: ')
        try:
            with open(f'{path}', encoding='utf-8') as f:
                strings = f.readlines()
                strings = [line.rstrip() for line in strings]
        except Exception as e:
            print(f'Не удалось открыть файл: {e}')
    elif typee.lower() == 'string':
        print('Введите строку')
        strings.append(input())
    else:
        print('Ошибка ввода')

    return strings


def main():
    strings = get_input_data()

    objects_list = []

    print('Какой тип объектов? (dish/menu/order)')
    object_type = input().lower()

    for string in strings:
        if string.strip():
            try:
                if object_type == 'dish':
                    obj = trytoparse_dish(string)
                    objects_list.append(obj)
                elif object_type == 'menu':
                    obj = trytoparse_menu(string)
                    objects_list.append(obj)
                elif object_type == 'order':
                    obj = trytoparse_order(string)
                    objects_list.append(obj)
                else:
                    print(f"Неизвестный тип объекта: {object_type}")
                    return
            except Exception as e:
                print(f"Ошибка в строке '{string}': {e}")

    for i, obj in enumerate(objects_list, 1):
        print(f"{i}. {obj}")


if __name__ == "__main__":
    main()