#iterable fun ----> iterable obj ---> next()---> 1 time 1 element
#next ----> 1
list1 = [1,2,3,4,5]
iterable_var = iter(list1)
print(next(iterable_var))
print(next(iterable_var))
print(next(iterable_var))
print(next(iterable_var))
print(next(iterable_var))
