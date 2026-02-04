from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей с данными.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, где state == переданному значению.
    """
    return [item for item in data if item.get("state") == state]
