#selection sort
def selection_sort(array,size):
    for step in range(size):
        min_index = step#0
        for i in range(step+1,size):#i=1
            if array[i] < array[min_index]:
                min_index = i

        (array[step],array[min_index]) = (array[min_index],array[step])

if __name__ == "__main__":
    data = [20,12,10,15,2]
    size = len(data)
    selection_sort(data,size)
    print("Sorted Array in Ascending Order: ",data)
