#Jump Search
#
import math
#x = 555
def jump_search(array,n,x):
    step = math.sqrt(n)#4.0

    prev = 0
    while array[int(min(step,n)-1)] < x:#3
        prev = step #8
        step+=math.sqrt(n)#12
        if prev>=n:
           return -1

    while array[int(prev)] <x:
        prev+=1
        if prev == min(step,n):
            return -1

    if array[int(prev)] == x:
        return prev
    return -1

if __name__ == "__main__":
    nums = [0, 1, 2, 3, 5, 8, 13, 21,
           34,35, 55, 89, 144, 233, 377, 610]#16
    n = len(nums)
    find_no = int(input("Please enter a number to find: "))
    result = jump_search(nums,n,find_no)
    if result == -1:
        print("Element not found")
    else:
        print("Number", find_no, "is at index", "%.0f" % result)
