#1 задание

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]

common_elements = set(list1) & set(list2)
print("Общие элементы списков:", common_elements)

unique_to_list1 = set(list1) - set(list2)
print("Элементы, которые есть в первом списке, но нет во втором:", unique_to_list1)


#2 задание

def main():
    brand = input("Введите марку машины: ")
    model = input("Введите модель машины: ")
    year = input("Введите год выпуска: ")
    color = input("Введите цвет машины: ")

    car_info = {
        'Марка': brand,
        'Модель': model,
        'Год выпуска': year,
        'Цвет': color
    }

    print("Список ключей словаря:", list(car_info.keys()))

    print("Список значений словаря:", list(car_info.values()))

    print("Элементы словаря:")
    for key, value in car_info.items():
        print(f"{key} -> {value}")

if __name__ == "__main__":
    main()

