from typing import Any

from datetime import datetime


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
    if not date:
        raise ValueError("Список пуст")
    date_list = []
    for date_dict in date:
        date_value = date_dict.get("date")
        if date_value is None:
            continue
        try:
            datetime.fromisoformat(date_value)
        except ValueError:
            continue
        else:
            date_list.append(date_dict)
    if not date_list:
        raise ValueError("Список пуст")
    date_sorted = sorted(date_list, key=lambda x: x["date"], reverse=reverse)
    return date_sorted
