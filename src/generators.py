from typing import Any, Iterator


def filter_by_currency(
    all_transactions: list[dict[str, Any]], name_of_the_currency="USD"
) -> Iterator[dict[str, Any]]:
    """Функция фильтрует список транзакций и выдает транзакции, где валюта операции соответствует заданной"""
    usd_transactions = filter(
        lambda transaction: transaction["operationAmount"]["currency"]["code"]
        == name_of_the_currency,
        all_transactions,
    )
    for item in usd_transactions:
        yield item


def transaction_descriptions(
    all_transactions: list[dict[str, Any]]
) -> Iterator[dict[str, Any]]:
    """Функция обрабатывает список транзакций и поочередно выдает описание каждой операции"""
    description = map(lambda transaction: transaction["description"], all_transactions)
    for item in description:
        yield item


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт"""
    if 0 <= start < stop <= 9999999999999999:
        numbers = [num for num in range(start, stop + 1)]
        numbers_list = map(lambda a: f"{a:0>16}", numbers)
        card_numbers = map(
            lambda number: f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}",
            numbers_list,
        )
        for item in card_numbers:
            yield item
    else:
        raise ValueError("Заданы некорректные значения")
