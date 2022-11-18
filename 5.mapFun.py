#map function ----> reduce no of time to call fun
def fact(n):
    return 1 if n<2 else n*fact(n-1)
#map function ---> takes 2 parameter ---> fun,iterable
#return map obj
# result = map(fact,range(6))#5
# print(result)
# for i in result:
#     print(i)
if __name__ == "__main__":
    # result = fact(0)
    # result1 = fact(1)
    # result2 = fact(2)
    # result3 = fact(3)
    # result4 = fact(4)
    # result5 = fact(5)
    # print(result)
    # print(result1)
    # print(result2)
    # print(result3)
    # print(result4)
    # print(result5)

    # result = list(map(fact,range(6)))#5
    result = map(fact, range(6))  # 5
    print(result)
    for i in result:
       print(i)

    for x in result:
       print(x)
    #map function 2 time ---> return 1 time
    #map function ----> generator
    #normal fun ----> return ---> end
