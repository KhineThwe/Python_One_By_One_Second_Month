#parameter Default
def bShop(name,quantity,unit,tList=None):
   if not tList:
       tList = []
   tList.append('{0} {1} {2}'.format(name, quantity, unit))
   return tList
store1 = bShop('python',3,'book')
bShop('Java',1,'book',store1)
store2 = bShop('c++',3,'book')
print(store1)
print(store2)
if store1 is store2:
    print('They are same')
else:
    print('They are not same')
