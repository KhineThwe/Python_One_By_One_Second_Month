import functools
li = [1,2,3,4,5]
print("The sum of all elements from list: ",end="")
print((functools.reduce(lambda a,b:a*b,li)))
