def get_mask_card_number(x: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_number = str(x)
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]
    return mask_card_number


def get_mask_account(x: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    account = str(x)
    mask_account = "**" + account[-4:]
    return mask_account
