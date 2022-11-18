class myClass:
    def __init__(self,x=0):#x=default parameter
        print('from class')
        self.counter = x

    def __call__(self,x=1):
        print('updating value.............')
        self.counter +=x

obj = myClass()
inObj = myClass()
print(myClass.__init__(inObj,1))#className.methodName(obj name,value ka optional)
print(inObj.counter)
print(myClass.__call__(obj,10))#callable pyhit ag lote tr
print(obj.counter)
print(callable(obj))
