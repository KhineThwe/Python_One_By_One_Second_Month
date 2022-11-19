def myGen():
    data = 1
    while data<=10:
        square =data*data
        yield square
        data+=1

if __name__ == "__main__":
    results = myGen()
    for i in results:
        print(i)


