from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция, которая маскирует номер или счет карты"""
    card_details = user_card.split()
    card_type = []
    for item in card_details:
        if item.isalpha():
            card_type.append(item)
        elif item.isdigit():
            if  "Счет" in card_details and len(item) == 20:
                card_number = get_mask_account(item)
            elif  "Счет" in card_details and len(item) == 16:
                raise ValueError("Данные введены некорректно")
            elif len(item) == 16:
                card_number = get_mask_card_number(item)
            else:
                raise ValueError("Данные введены некорректно")
            card_type.append(card_number)
    if not card_details:
        raise ValueError("Данные введены некорректно")
    elif not card_details[-1].isdigit():
        raise ValueError("Данные введены некорректно")
    return " ".join(card_type)


def get_date(info: str) -> str:
    """Функция, которая приводит данные о дате в удобный формат"""
    date_info_slice = info[:10].split("-")
    formatted_date = date_info_slice[-1:-4:-1]
    return ".".join(formatted_date)
