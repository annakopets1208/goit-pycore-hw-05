import re
from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    """Повертає генератор дійсних чисел, знайдених у тексті."""
    pattern = r"(?<!\S)\d+\.\d+(?!\S)"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """Підсумовує всі числа, які повертає генератор func для тексту."""
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")