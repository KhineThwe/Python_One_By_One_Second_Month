#function annotation ---> attribute
#doc string ---> function body
#def myFun(a:<expression>,b:<expression>)

# def myFun(a:'annotation of a',b:'annotation of b')->'return a multiply b':
#     """This function'll return a*b"""
#     return a*b
# print(myFun.__annotations__)
# print(myFun.__doc__)

x = 3
y = 5
def myFun1(a:'some value from funCall',b:'some value from funCall')->'mutiply'+str(max(x,y)):
    """This function will return b+a*max(x,y) """
    return b+a*max(x,y)

data = myFun1(2,4)
print(data)
print(myFun1.__doc__)
print(myFun1.__annotations__)
