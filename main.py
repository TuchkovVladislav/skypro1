from src.masks import get_mask_account, get_mask_card_number


def main():
    # Пример маскировки банковского счета
    account_number = "1234567890123456"
    masked_account = get_mask_account(account_number)
    print(f"Маскированный номер счета: {masked_account}")

    # Пример маскировки банковской карты
    card_number = "1234567812345678"
    masked_card = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card}")


if __name__ == "__main__":
    main()
