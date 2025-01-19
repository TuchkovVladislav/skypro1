from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card
from src.widget import get_date

def main():
    # Маскировка банковского счета
    account_number = "1234567890"
    print(get_mask_account(account_number))  # Ожидаемый результат: **7890

    # Маскировка банковской карты
    card_number = "1234567890123456"
    print(get_mask_card_number(card_number))
    # Ожидаемый результат: 1234 56** **** 3456


if __name__ == "__main__":
    main()

# Пример с картами
print(mask_account_card("Visa Super Puper 1234567890123456"))
print(mask_account_card("Visa Super 1234567890123456"))

# Пример со счетом
print(mask_account_card("Счет 73654108430135874305"))

# Пример с датой
date_string = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_string)
print(formatted_date)
