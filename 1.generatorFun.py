#generator fun
def myFun(x):
    return x

def myGen():
    data = 10
    yield data
    yield data+1
    yield data+2
    yield data+3

results = myGen()
print(results)
# print(next(results))
# print(next(results))
# print(next(results))
# print(next(results))
for i in results:
    print(i)

