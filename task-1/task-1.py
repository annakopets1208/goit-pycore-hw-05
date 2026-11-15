def caching_fibonacci():
    # Кеш для зберігання вже обчислених чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Якщо значення вже є в кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Обчислюємо рекурсивно, зберігаємо в кеш і повертаємо
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))
print(fib(15))