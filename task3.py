import re
from patterns import phone_pattern

# Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду(додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.


def normalize_phone(phone_number: str):
    phone_cleaned = re.sub(r'[^\d+]', '', phone_number)
    if match := re.match(
            phone_pattern, phone_cleaned):
        country_code = "+380"
        operator_code = match[2]
        part1 = match[3]
        part2 = match[4]
        part3 = match[5]
        return f"{country_code}{operator_code}{part1}{part2}{part3}"


# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]
# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
