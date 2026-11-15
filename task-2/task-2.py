import decimal
from decimal import Decimal

number = Decimal("1.45")

print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))
print("Округлення до трьох десяткових знаків:", Decimal("3.14159"). quantize(Decimal("0.000")))