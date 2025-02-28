from src.masks import get_mask_account, get_mask_card_number

from datetime import datetime


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
    date_format = ""
    formatted_date = ""
    for i in info:
        if i.isdigit():
            date_format += "*"
            formatted_date += i
        elif not i.isalnum():
            date_format += "."
            formatted_date += "."
        elif i == "T":
            date_format += i
            formatted_date += i
        else:
            raise ValueError("Некорректная дата")
    if date_format == "****.**.**T**.**.**.******":
        date_object = datetime.strptime(formatted_date, "%Y.%m.%dT%H.%M.%S.%f")
        date_str = date_object.strftime("%d.%m.%Y")
    elif date_format == "****.**.**":
        date_object = datetime.strptime(formatted_date, "%Y.%m.%d")
        date_str = date_object.strftime("%d.%m.%Y")
    else:
        raise ValueError("Некорректная дата")
    return date_str
