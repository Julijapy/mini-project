from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция, которая маскирует номер или счет карты"""
    card_details = user_card.split()
    details_list = []
    for item in card_details:
        if item.isalpha():
            details_list.append(item)
        else:
            if len(item) == 16:
                card_number = get_mask_card_number(card_details[-1])
            else:
                card_number = get_mask_account(card_details[-1])
            details_list.append(card_number)
    return " ".join(details_list)


def get_date(info: str) -> str:
    """Функция, которая приводит данные о дате в удобный формат"""
    date_info_slice = info[:10].split("-")
    formatted_date = date_info_slice[-1:-4:-1]
    return ".".join(formatted_date)
