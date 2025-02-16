import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card


@pytest.mark.parametrize("card_number, expected", [("1000222233334444", "1000 22** **** 4444"),
                                                   ("2000202030304040", "2000 20** **** 4040"),
                                                   ("3000505060607070", "3000 50** **** 7070")])
def test_get_mask_card_number_normal_format(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, expected", [("1000222233skypro", "Данные введены некорректно"),
                                                   (" ", "Данные введены некорректно"),
                                                   ("3000    60607070", "Данные введены некорректно")])
def test_get_mask_card_number_not_numbers(card_number, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)

    assert str(exc_info.value) == expected


@pytest.mark.parametrize("card_number, expected", [("111122223333444", "Данные введены некорректно"),
                                                   ("11112222333344445", "Данные введены некорректно"),
                                                   ("", "Данные введены некорректно")])
def test_get_mask_card_number_incorrect_length(card_number, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)

    assert str(exc_info.value) == expected


@pytest.mark.parametrize("account_number, expected", [("11112222333344445555", "**5555"),
                                                      ("12345678901234567890", "**7890"),
                                                      ("12121212121212121212", "**1212")])
def test_get_mask_account_normal(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number, expected", [("111122223333444skypro", "Данные введены некорректно"),
                                                      ("1234 901234567890", "Данные введены некорректно"),
                                                      (" ", "Данные введены некорректно"),
                                                      ("123", "Данные введены некорректно"),
                                                      ("12121212121212121212121212", "Данные введены некорректно")])
def test_get_mask_account_incorrect(account_number, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)

    assert str(exc_info.value) == expected
