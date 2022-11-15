#function introspection
def myFun(x,y):
    return x+y
print(dir(myFun))
myFun.__subject__ = 'bio'
myFun.__mark__ = 99
print(dir(myFun))
print(myFun.__subject__)
print(myFun.__mark__)
