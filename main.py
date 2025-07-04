from src.decorators import log
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

one_transaction = filter_by_currency(all_transactions=transactions)


def transaction_info():
    """Поочередная выдача списка транзакций, отфильтрованного по валюте"""
    try:
        return next(one_transaction)
    except StopIteration:
        return "Список транзакций пуст"


descriptions_data = transaction_descriptions(all_transactions=transactions)


def description_transaction_info():
    """Поочередная выдача информации описания транзакции"""
    try:
        return next(descriptions_data)
    except StopIteration:
        return "Список транзакций пуст"


card_number_info = card_number_generator(1, 5)


def get_card_number_info():
    """Поочередная выдача номеров банковских карт"""
    try:
        return next(card_number_info)
    except StopIteration:
        return "Список транзакций пуст"


@log(filename="logs/mylog.txt")
def func(x, y):
    """Проверка работоспособности функции при записи логов в файл"""
    return x + y


func(1, 2)
