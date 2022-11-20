#own partial function
#to make arg less
from functools import partial
def myFun(x,y,z):
    x = x + 11
    y = y + 11
    z = z + 11
    print(x, y, z)

#partial fun
def pFun(yy,zz):
    return myFun(10,yy,zz)
#default value ---> preset value

pFun(100,200)
#own partial fun

#built-in partial fun
def myFun1(x,y,z):
    x=x+11
    y=y+11
    z=z+11
    print(x,y,z)
newFun = partial(myFun1,10)#10 preset value go into first arg x
newFun(100,200)

