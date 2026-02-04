from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date


def main():
    # Пример маскировки банковского счета
    account_number = "1234567890123456"
    masked_account = get_mask_account(account_number)
    print(f"Маскированный номер счета: {masked_account}")

    # Пример маскировки банковской карты
    card_number = "1234567812345678"
    masked_card = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card}")

    # Вывод даты
    operations = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-03-11T02:26:18.671407",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-01-10T10:00:00.000000",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2024-05-01T12:00:00.000000",
        },
    ]

    # 1. Фильтрация
    filtered = filter_by_state(operations)
    print("После фильтрации:")
    print(filtered)

    # 2. Сортировка
    sorted_ops = sort_by_date(filtered)
    print("\nПосле сортировки:")
    print(sorted_ops)

if __name__ == "__main__":
    main()
