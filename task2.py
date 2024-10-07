from random import sample
# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.


def get_numbers_ticket(min_number, max_number, quantity):
    if min_number > 0 and max_number - min_number >= quantity > 0 and max_number <= 1000:
        return sorted(sample(range(min_number, max_number), quantity))
    else:
        return ValueError('Some of the numbers are out of range')


# print(get_numbers_ticket(-51, 1051, 5))
# print(get_numbers_ticket(1, 999, 300))
# print(get_numbers_ticket(996, 1000, 5))
# print(get_numbers_ticket(990, 1000, 13))
# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)
