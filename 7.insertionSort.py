#insertion sort in python
def insertionSort(array):
    n=len(array)
    for i in range(1,n):#i=0
        temp = array[i]#5
        j = i - 1#j=0 --->  9

        while j>=0 and temp<array[j]:
            array[j+1] = array[j]#
            #[9,9,1,4,3]
            j=j-1
        array[j+1] = temp
if __name__ == "__main__":
    data = [9,5,1,4,3]
    insertionSort(data)
    print('Sorted array in ascending order',data)
