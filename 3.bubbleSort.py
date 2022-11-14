#bubble sort
def bubbleSort(array):
    for i in range(len(array)):# 0 7
        for j in range(0,len(array)-i-1):#j= 0 to 6(0,....5)
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data = [5, 3, 13, 2, 11, 4, 7]
bubbleSort(data)
print("Sorted array in ascending order")
print(data)
