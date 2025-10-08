from datetime import time

test1 = '"Плов узбекский" 350.75 01.30'
test2 = '"Суп"    250.50    00.45'
test3 = '"Борщ украинский"  280.00  01.15'


def trytoparse_dish(input_str):
    parts = input_str.split('"')
    dish_name = parts[1]

    rest = parts[2].split()

    price = float(rest[0])

    time_parts = rest[1].split('.')
    cooking_time = time(int(time_parts[0]), int(time_parts[1]))

    result = f"Блюдо: {dish_name}, Цена: {price}, Время приготовления: {cooking_time.strftime('%H:%M')}"
    return result


print(trytoparse_dish(test1))
print(trytoparse_dish(test2))
print(trytoparse_dish(test3))