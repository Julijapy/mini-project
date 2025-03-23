from src.generators import filter_by_currency, transaction_descriptions

from main import transaction_info, description_transaction_info


def test_filter_by_currency(transactions_list, filter_by_currency_result):
    """Тестирование функции при стандартных данных"""
    assert list(filter_by_currency(transactions_list)) == filter_by_currency_result


def test_transaction_info():
    assert transaction_info() == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert transaction_info() == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert transaction_info() == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }
    assert transaction_info() == "Список транзакций пуст"


def test_transaction_descriptions(transactions_list, transaction_descriptions_result):
    """Тестирование функции при стандартных данных"""
    assert list(transaction_descriptions(transactions_list)) == transaction_descriptions_result


def test_description_transaction_info():
    assert description_transaction_info() == "Перевод организации"
    assert description_transaction_info() == "Перевод со счета на счет"
    assert description_transaction_info() == "Перевод со счета на счет"
    assert description_transaction_info() == "Перевод с карты на карту"
    assert description_transaction_info() == "Перевод организации"
    assert description_transaction_info() == "Список транзакций пуст"
