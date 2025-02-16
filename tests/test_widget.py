import pytest

from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("user_card, expected", [("Visa Platinum 1111222233334444", "Visa Platinum 1111 22** **** 4444"),
                                                 ("Maestro 7000792289606361","Maestro 7000 79** **** 6361"),
                                                 ("11112222333344445555", "**5555")])
def test_mask_account_card(user_card, expected):
    assert mask_account_card(user_card) == expected