from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(info: str) -> str:
    if not isinstance(info, str):
        raise ValueError("Аргумент должен быть строкой.")

        # Определяем, является ли это картой или счетом
    if info.startswith("Счет"):
        # Извлекаем номер счета
        account_number = info.split(maxsplit=1)[1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        # Извлекаем номер карты
        *card_name, card_number = info.rsplit(maxsplit=1)
        masked_card = get_mask_card_number(card_number)
        return f"{' '.join(card_name)} {masked_card}"
from datetime import datetime

def get_date(date_string: str) -> str:
    if not isinstance(date_string, str):
        raise ValueError("Дата должна быть строкой.")

    try:
        # Парсим строку в объект datetime
        date_obj = datetime.fromisoformat(date_string)
        # Форматируем в "ДД.ММ.ГГГГ"
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидается 'YYYY-MM-DDTHH:MM:SS.ssssss'")