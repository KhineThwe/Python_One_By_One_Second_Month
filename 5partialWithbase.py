from functools import partial
def pow(base,exponent):
    return base ** exponent
sq = partial(pow,exponent=2)
print(sq(4))

cu = partial(pow,exponent=3)
print(cu(4))

print("Testing for base with 5 and exponent 3:",cu(base=5))
