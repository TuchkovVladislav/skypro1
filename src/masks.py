def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, показывая только последние 4 цифры.
    """
    if len(account_number) < 4:
        raise ValueError("Номер счета должен быть не менее 4 символов.")

    # Берем последние 4 цифры
    last_four_digits = account_number[-4:]

    # Возвращаем замаскированный номер
    return f"**{last_four_digits}"


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые 4, 2 символа в середине,
    и последние 4 цифры, форматируя блоками.
    """
    if len(card_number) < 16:
        raise ValueError("Номер карты должен быть не менее 16 символов.")

    # Разбиваем номер на части
    first_four = card_number[:4]
    fifth_and_sixth = card_number[4:6]
    last_four = card_number[-4:]

    # Возвращаем замаскированный номер в формате блоков
    return f"{first_four} {fifth_and_sixth}** **** {last_four}"
