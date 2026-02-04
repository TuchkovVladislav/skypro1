from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, маскируя номер.
    """
    if not isinstance(info, str):
        raise ValueError("Аргумент должен быть строкой.")

    if info.startswith("Счет"):
        # Обработка для счета
        account_number = info.split(maxsplit=1)[1]
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    else:
        *card_name_list, card_number = info.rsplit(maxsplit=1)
        card_name = " ".join(card_name_list)  # Преобразуем список в строку
        masked_card = get_mask_card_number(card_number)
        return f"{card_name} {masked_card}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата "2025-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".
    """
    if not isinstance(date_string, str):
        raise ValueError("Дата должна быть строкой.")

    try:
        # Парсим строку в объект datetime
        date_obj = datetime.fromisoformat(date_string)
        # Форматируем в "ДД.ММ.ГГГГ"
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидается 'YYYY-MM-DDTHH:MM:SS.ssssss'")
