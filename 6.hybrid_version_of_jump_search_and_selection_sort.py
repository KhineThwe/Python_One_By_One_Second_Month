import math
import random
def jump_search(new_nums,n,find_no):
    step = math.sqrt(n)

    prev = 0
    while new_nums[int(min(step,n)-1)] < find_no:
        prev = step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
    while new_nums[int(prev)] < find_no:
        prev+=1
        if prev == min(step,n):
            return -1

    if new_nums[int(prev)] == find_no:
        return prev
    return -1


def selectionSort(arrayList,n):
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arrayList[j] < arrayList[min_index]:
                min_index = j
        (arrayList[i],arrayList[min_index]) = (arrayList[min_index],arrayList[i])
    return arrayList

if __name__ == "__main__":
    no_of_elements = int(input("Please enter number of elements that you want to generate: "))
    i = 0
    arrayList = []
    while i<no_of_elements:
        # elements = int(input("Enter elements: "))
        account_no = random.randint(100,999)
        if account_no in arrayList:
            print("Dulplicate elements don't allow")
        else:
            arrayList.append(account_no)
            i += 1
    n = len(arrayList)
    new_nums = selectionSort(arrayList,n)
    print("Sorted array in ascending order: ",new_nums)
    find_no = int(input("Please enter a number to find: "))
    result = jump_search(new_nums,n,find_no)
    print(arrayList)
    if result == -1:
        print("Element not found: ")
    else:
        print("Number ",find_no,"is at index","%.0f" %result)
