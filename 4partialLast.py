from functools import partial
def myFun(x,y,*args,x1,y1,**kwargs):
    print(x,y,*args,x1,y1,**kwargs)

newFun = partial(myFun,10,x1='test')
newFun(30,5,6,y1="testing")
