#my own reduce function
import functools
def mySum(x1,y1):
    return x1+y1

def myReduce(mySum,seq):
    first = seq[0]#3
    for i in seq[1:]:#3
        first = mySum(first,i)#mySum(1,2)#first = 3#mySum(3,3)
    return first

list = [1,2,3,4,5,6]
result = myReduce(mySum,list)
print(result)

print(functools.reduce(lambda a,b:a+b,list))
