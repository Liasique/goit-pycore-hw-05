#TODO: find all REAL numbers in the text and calculate their sum

import re

from typing import Callable

#def generator_numbers(text: str)
"""повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті.
 Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків."""

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'  # Регулярний вираз для пошуку дійсних чисел
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)  # повертаємо як float, один за одним
    
#def sum_profit(text: str, func: Callable)
"""має використовувати генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку
 та приймати його як аргумент при виклику."""

def sum_profit(text, generator_numbers):
    return sum(generator_numbers(text))  


#Рекомендації для виконання:
"""Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, що числа 
чітко відокремлені пробілами.
Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа."""

#Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

#Очікуване виведення:
"""Загальний дохід: 1351.46"""