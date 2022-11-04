def myFun(a,b,*c):
    print(a)
    print(b)
    print(c)
myList = [1,2,4,5,8,9]
myFun(*myList)

def myFun2(x=10,y=20):
    print(x,y)
myFun2(5,3)

def myFun3(a,b,*c,d):
    print(a,b,c,d)
myList1 = [1,2,4,5,8,9]
myFun3(*myList1,d=6)

#end of positional args
def myFun(a,b,*,c):
    print(a,b,c)
myFun(1,2,c=20)#keyword only arg

#keyword argument ** key,value ---> dictionary
def myFunLast(**key):
    print(key)
myFunLast(a=10,b=20,c=4)

def kwargumentFun(a,b,*,koa,**kw):
    print(a,b,koa,kw)
kwargumentFun(a=10,b=20,c=30,koa=101)



