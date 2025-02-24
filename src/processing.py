from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state='EXECUTED'
) -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_list = []
    for element in data:
        for key, value in element.items():
            if value == '':
                continue
            elif value == state:
                new_list.append(element)
    if not new_list:
        raise ValueError("Список пуст")
    return new_list


def sort_by_date(date: list[dict[str, Any]], reverse=True) -> list[dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    new_date = sorted(date, key=lambda x: x["date"], reverse=reverse)
    return new_date
