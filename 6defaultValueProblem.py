#default value problem
#datetime
from datetime import datetime
# time = datetime.utcnow()
# print("Current Time",time)
# def myFun(msg,*,dt=datetime.utcnow()):
#     print("{0} : {1}".format(dt,msg))
# myFun("Testing")

#handle
def myFun(msg,*,dt=None):
    if not dt:#null
        dt = datetime.utcnow()
        print("{0} : {1}".format(dt, msg))
myFun("Testing")
