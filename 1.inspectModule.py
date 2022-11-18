#inspect module
import math
import inspect
from inspect import ismethod,isfunction
def myFun(x,y,z=10,*,kw1,kw2=2):
	"""This is doc string"""
	return x*y

print(myFun.__name__)
print(myFun.__defaults__)#tuple ()
print(myFun.__kwdefaults__)#dictionary
print(myFun.__code__.co_varnames)#function var name ----> tuple
print(myFun.__code__.co_argcount)#return positional arg's count
print(inspect.getsource(myFun))
# print(inspect.getcomments(myFun))
print(inspect.getdoc(myFun))
print(inspect.getmodule(print))
print(inspect.getmodule(ismethod))
print(inspect.getmodule(math.sin))
