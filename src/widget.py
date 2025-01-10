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


def get_date(info: str) -> str:
    """ Функция, которая приводит данные о дате в удобный формат """
    date_info_slice = info[:10].split("-")
    formatted_date = date_info_slice[-1:-4:-1]
    return ".".join(formatted_date)
