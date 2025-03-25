import pytest

from main import (description_transaction_info, get_card_number_info,
                  transaction_info)
from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency(transactions_list, filter_by_currency_result):
    """Тестирование функции при стандартных данных"""
    assert list(filter_by_currency(transactions_list)) == filter_by_currency_result


def test_transaction_info():
    """Тестирование функции transaction_info"""
    assert transaction_info() == {
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
    }
    assert transaction_info() == {
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
    }
    assert transaction_info() == {
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
    }
    assert transaction_info() == "Список транзакций пуст"


def test_transaction_descriptions(transactions_list, transaction_descriptions_result):
    """Тестирование функции при стандартных данных"""
    assert (
        list(transaction_descriptions(transactions_list))
        == transaction_descriptions_result
    )


def test_description_transaction_info():
    """Тестирование функции description_transaction_info"""
    assert description_transaction_info() == "Перевод организации"
    assert description_transaction_info() == "Перевод со счета на счет"
    assert description_transaction_info() == "Перевод со счета на счет"
    assert description_transaction_info() == "Перевод с карты на карту"
    assert description_transaction_info() == "Перевод организации"
    assert description_transaction_info() == "Список транзакций пуст"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            20,
            25,
            [
                "0000 0000 0000 0020",
                "0000 0000 0000 0021",
                "0000 0000 0000 0022",
                "0000 0000 0000 0023",
                "0000 0000 0000 0024",
                "0000 0000 0000 0025",
            ],
        ),
        (
            330,
            335,
            [
                "0000 0000 0000 0330",
                "0000 0000 0000 0331",
                "0000 0000 0000 0332",
                "0000 0000 0000 0333",
                "0000 0000 0000 0334",
                "0000 0000 0000 0335",
            ],
        ),
        (
            1234,
            1240,
            [
                "0000 0000 0000 1234",
                "0000 0000 0000 1235",
                "0000 0000 0000 1236",
                "0000 0000 0000 1237",
                "0000 0000 0000 1238",
                "0000 0000 0000 1239",
                "0000 0000 0000 1240",
            ],
        ),
        (
            9999999999999990,
            9999999999999999,
            [
                "9999 9999 9999 9990",
                "9999 9999 9999 9991",
                "9999 9999 9999 9992",
                "9999 9999 9999 9993",
                "9999 9999 9999 9994",
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    """Тестирование генератора card_number_generator"""
    assert list(card_number_generator(start, stop)) == expected


def test_get_card_number_info():
    """Тестирование функции get_card_number_info"""
    assert get_card_number_info() == "0000 0000 0000 0001"
    assert get_card_number_info() == "0000 0000 0000 0002"
    assert get_card_number_info() == "0000 0000 0000 0003"
    assert get_card_number_info() == "0000 0000 0000 0004"
    assert get_card_number_info() == "0000 0000 0000 0005"
    assert get_card_number_info() == "Список транзакций пуст"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (-1, -3, "Заданы некорректные значения"),
        (-1, 3, "Заданы некорректные значения"),
        (3, 0, "Заданы некорректные значения"),
        (9999999999999999, 10000000000000000, "Заданы некорректные значения"),
    ],
)
def test_card_number_generator_incorrect(start, stop, expected):
    """Тестирование генератора card_number_generator при некорректных вводных данных"""
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(start, stop))
    assert str(exc_info.value) == expected
