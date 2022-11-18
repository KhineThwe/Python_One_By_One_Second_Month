#callable
from decimal import Decimal
print(callable(print))
print(callable('xyz'.upper))
print(callable(callable))
print(callable(Decimal))
a = Decimal('10.10')
print(type(a))
print(callable(a))

