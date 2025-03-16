from tests.conftest import transactions


def filter_by_currency(all_transactions: list[dict], name_of_the_currency="USD") -> list:
    usd_transactions = filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == name_of_the_currency, all_transactions)

    return list(usd_transactions)


usd_list = filter_by_currency(all_transactions=transactions(), name_of_the_currency="USD")


def iterating_transactions():
    for item in usd_list:
        yield dict(item)


one_transaction = iterating_transactions()

print(next(one_transaction))
