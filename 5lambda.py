#lambda expression or anonymous function
x = lambda x,y:y*2+x
print(x(3,4))

y = lambda i,j=10:i*j
print(y(2,3))

#arbitary
z = lambda x,*args,y,**kwargs:(x,args,y,kwargs)
print(z(10,'a','b',y=10,i=10,j=20,k=30))
