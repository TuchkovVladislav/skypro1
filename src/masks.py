def get_mask_account(account_number: str, visible_digits: int = 4) -> str:
    """
    Маскирует номер банковского счета, показывая только последние несколько цифр.
    """
    if not isinstance(account_number, str):
        raise ValueError("Номер счета должен быть строкой.")
    if len(account_number) <= visible_digits:
        return account_number  # Если номер короче или равен видимым цифрам, возвращаем его полностью

    mask_length = len(account_number) - visible_digits
    masked_part = "*" * mask_length
    visible_part = account_number[-visible_digits:]
    return f"{masked_part}{visible_part}"


def get_mask_card_number(card_number: str, visible_digits: int = 4, block_size: int = 4) -> str:
    """
    Маскирует номер банковской карты, оставляя только последние цифры и форматируя блоками.
    """
    if not isinstance(card_number, str):
        raise ValueError("Номер карты должен быть строкой.")
    if len(card_number) <= visible_digits:
        return card_number  # Если номер короче или равен видимым цифрам, возвращаем его полностью

    mask_length = len(card_number) - visible_digits
    masked_part = "*" * mask_length
    visible_part = card_number[-visible_digits:]

    # Создаем маскированную строку
    masked_number = masked_part + visible_part

    # Форматируем в блоки
    formatted_number = " ".join(
        [
            masked_number[i: i + block_size]
            for i in range(0, len(masked_number), block_size)
        ]
    )

    return formatted_number
