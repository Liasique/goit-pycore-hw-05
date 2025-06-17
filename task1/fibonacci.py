#TODO: Create function caching_fibonacci() that returns an inner function fibonacci(n) with caching 

#PSEUDOCODE:
"""
ФУНКЦІЯ caching_fibonacci
    Створити порожній словник cache

    ФУНКЦІЯ fibonacci(n)
        Якщо n <= 0, повернути 0
        Якщо n == 1, повернути 1
        Якщо n у cache, повернути cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Повернути cache[n]

    Повернути функцію fibonacci
КІНЕЦЬ ФУНКЦІЇ caching_fibonacci
"""

def caching_fibonacci():
    cache = {} #Створити порожній словник cache

    def fibonacci(n):
        if n <= 0:
            return 0  # Case: Fibonacci of 0 is 0
        elif n == 1:
            return 1 # Case: Fibonacci of 1 is 1
        if n in cache:
            return cache[n]  # If result is already in cache -> return it
        # If not in cache, calculate and save it in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n]

    return fibonacci  # Return the inner function

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(20))  # Виведе 6765