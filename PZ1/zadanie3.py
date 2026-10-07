def remove_element(my_list, element):
    try:
        my_list.remove(element)
    except ValueError:
        print(f"Ошибка: Элемента '{element}' нет в списке.")
    else:
        print(f"Успех: Элемент '{element}' успешно удален из списка!")





shopping_list = ["молоко", "хлеб", "сыр", "яблоки"]
print("Исходный список:", shopping_list)
print("-" * 40)

# Пример 1: Успешное удаление
remove_element(shopping_list, "сыр")
print("Список после первого удаления:", shopping_list)
print("-" * 40)

# Пример 2: Попытка удаления несуществующего элемента
remove_element(shopping_list, "шоколад")
print("Финальный список:", shopping_list)
