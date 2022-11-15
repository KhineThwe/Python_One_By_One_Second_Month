#higher order function
#function တစ်ခုကနေ တခြား function arg
#lambda parameter_list:expression
#myFun ---> higher order function
#Ass1. lambda mini console
def myFun(x,fn):
    return fn(x)

value = myFun(5,lambda y:y**2)#5 power2
print(value)

def myFun1(fn,*args,**kwargs):
    return fn(*args,**kwargs)
value1 = myFun1(lambda x,y:x**y,2,3)
print(value1)
