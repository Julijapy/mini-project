def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number.isdigit() and len(card_number) == 16:
        number_slice_1 = card_number[0:4]
        number_slice_2 = card_number[4:6]
        number_slice_3 = card_number[12:]
    else:
        raise ValueError("Данные введены некорректно")
    return "".join(number_slice_1) + " " + "".join(number_slice_2) + "** **** " + "".join(number_slice_3)


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if account_number.isdigit() and len(account_number) == 20:
        account_mask = "**" + account_number[-4:]
    else:
        raise ValueError("Данные введены некорректно")
    return account_mask
