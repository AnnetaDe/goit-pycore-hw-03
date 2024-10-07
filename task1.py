from datetime import datetime
import re
from patterns import date_formats


#  Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python


def get_days_from_today(date: str) -> int:
    no_space_date = date.strip()
    for date_pattern in date_formats:
        if re.match(date_pattern[0], no_space_date):
            date = datetime.strptime(no_space_date, date_pattern[1])
            today = datetime.now()
            return (today - date).days
        return ValueError('Invalid date format')


user_input = input('Enter the date ')

# print(get_days_from_today(user_input))
