import pprint

data_list = [
    {"name": "Бананы", "price": 120, "category": "фрукты", "quantity": 50},
    {"name": "Яблоки", "price": 95, "category": "фрукты", "quantity": 35},
    {"name": "Морковь", "price": 30, "category": "овощи", "quantity": 47},
    {"name": "Эклеры", "price": 250, "category": "кулинария", "quantity": 0},
]


def sort_list(data: list[dict], item: str = None) -> list[dict]:
    """
    Возвращает список словарей, отсортированных по убыванию стоимости продукта,
    но только для продуктов из заданной категории.
    Если категория не задана, то сортировка производится для всех продуктов.

    :param data: Список словарей с данными о продуктах
    :param item:Категория продуктов, по которой хотим получить статистику.
    :return:Сортированный по убыванию стоимости список словарей.
    """
    if item:
        new_list = [product for product in data if product["category"] == item]
        return sorted(new_list, key=lambda x: x["price"], reverse=True)
    else:
        return sorted(data, key=lambda x: x["price"], reverse=True)


pprint.pprint(sort_list(data_list, "фрукты"))
