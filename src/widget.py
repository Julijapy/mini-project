from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_card: str) -> str:
    """ Функция, которая маскирует номер или счет карты"""
    details = user_card.split()
    card_number = get_mask_card_number(details[-1])
    card_account = get_mask_account(details[-1])
    details_list = []
    for item in details:
        if item.isalpha():
            details_list.append(item)
    if len(details[-1]) == 16:
        details_list.append(card_number)
    else:
        details_list.append(card_account)
    return " ".join(details_list)
