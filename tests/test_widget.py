import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_card, expected",
    [
        ("Visa Platinum 1111222233334444", "Visa Platinum 1111 22** **** 4444"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 11112222333344445555", "Счет **5555"),
        ("Счет 10002000300040005000", "Счет **5000"),
    ],
)
def test_mask_account_card(user_card, expected):
    """Тестирование функции при стандартных данных"""
    assert mask_account_card(user_card) == expected


@pytest.mark.parametrize(
    "user_card, expected",
    [
        ("Visa Platinum 111122223333444", "Данные введены некорректно"),
        ("Visa 11112222333344445", "Данные введены некорректно"),
        ("Maestro", "Данные введены некорректно"),
        ("abrakadabra simsalabim", "Данные введены некорректно"),
        ("", "Данные введены некорректно"),
        (" ", "Данные введены некорректно"),
        ("Счет 1111222233334444", "Данные введены некорректно"),
        ("Счет 11112222333344445", "Данные введены некорректно"),
        ("Счет 100020003000400050006000", "Данные введены некорректно"),
        ("Счет abab", "Данные введены некорректно"),
        ("Счет a1a1", "Данные введены некорректно"),
    ],
)
def test_mask_account_card_incorrect(user_card, expected):
    """Тестирование функции при некорректных данных"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(user_card)
    assert str(exc_info.value) == expected


@pytest.mark.parametrize(
    "date_info, expected",
    [
        ("2025.02.21", "21.02.2025"),
        ("2025/02/21", "21.02.2025"),
        ("2025-02-21", "21.02.2025"),
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024/03/11T02:26:18.671407", "11.03.2024"),
        ("2024.03.11T02/26/18/671407", "11.03.2024"),
    ],
)
def test_get_date_normal(date_info, expected):
    """Тестирование функции при стандартных данных"""
    assert get_date(date_info) == expected


@pytest.mark.parametrize(
    "date_info, expected",
    [
        ("", "Некорректная дата"),
        (" ", "Некорректная дата"),
        ("11111111", "Некорректная дата"),
        ("qwerty.123", "Некорректная дата"),
    ],
)
def test_get_date_incorrect(date_info, expected):
    """Тестирование функции при некорректных данных"""
    with pytest.raises(ValueError) as exc_info:
        get_date(date_info)
    assert str(exc_info.value) == expected
