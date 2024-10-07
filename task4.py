from datetime import datetime, timedelta
import re
# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

def get_upcoming_birthdays(users: list) -> list:
    upcoming_week_birthdays = []

    for person in users:
        birthday_str = datetime.strptime(
            person.get('birthday'), '%Y.%m.%d')
        congratulation_date = birthday_str.replace(
            year=datetime.now().year).date()

        if congratulation_date.weekday() == 5:
            congratulation_date = congratulation_date.replace(
                day=congratulation_date.day+2)
        elif congratulation_date.weekday() == 6:
            congratulation_date = congratulation_date.replace(
                day=congratulation_date.day+1)
        else:
            congratulation_date = congratulation_date

        if congratulation_date >= datetime.now().date(
        ) and (datetime.now().isocalendar().week)+1 == congratulation_date.isocalendar().week:
            person_to_greet = {
                'name': person.get('name'),
                'congratulation_date': datetime.strftime(congratulation_date, '%Y.%m.%d')
            }
            upcoming_week_birthdays.append(person_to_greet)

    return upcoming_week_birthdays


# users = [
#     {"name": "John Doe", "birthday": "1985.10.13"},
#     {"name": "Jane Smith", "birthday": "1990.10.07"},
#     {"name": "Jane Smith", "birthday": "1990.10.20"},
#     {"name": "Jane Smith", "birthday": "1990.10.26"},
#     {"name": "Jane Smith", "birthday": "1990.10.12"},

# ]

# print(get_upcoming_birthdays(users))
