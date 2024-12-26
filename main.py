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

from src.widget import mask_account_card

# Пример с картами
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))

# Пример со счетом
print(mask_account_card("Счет 73654108430135874305"))

from src.widget import get_date

date_string = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_string)
print(formatted_date)
