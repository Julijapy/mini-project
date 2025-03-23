from typing import Iterator, Any


def filter_by_currency(all_transactions: list[dict[str, Any]], name_of_the_currency="USD") -> Iterator[dict[[str, Any]]]:
    usd_transactions = filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == name_of_the_currency, all_transactions)
    for item in usd_transactions:
        yield item
