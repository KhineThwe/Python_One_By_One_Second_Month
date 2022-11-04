import time
def myFun(fn,*args,rep=1,**kwargs):
    start = time.perf_counter()#start
    print("Starting Time",start)
    for i in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()#end time
    print("Ending Time", end)
    avgTime = (end-start)/rep
    fn(avgTime)
myFun(print,1,2,3,rep=5,sep='-',end='***\n')
