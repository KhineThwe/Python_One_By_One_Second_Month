#low=0  high=n-1
#main point ---> sorted order
#function to find the total no of times that the list is sorted
#pivot property ---> next,prev elements must be greater than pivot--->minimum element
def findRotationCount(nums,n):
    low = 0
    high = n-1
    while low<=high:
        #condition1:list is already sorted
        if nums[low]<=nums[high]:
            return low
        mid = (low+high)//2

        next = (mid+1) % n
        prev = (mid-1+n)%n
#15%11--> 4
        if nums[mid]<=nums[next] and nums[mid]<=nums[prev]:
            return mid
        elif nums[mid] <= nums[high]:
            high = mid - 1
        elif nums[mid]>=nums[low]:
            low = mid +1
    return -1

if __name__ == "__main__":
    nums = [8,9,10,11,1,2,3,4,5,6,7]#rotate ----> find ---> binary search
    # nums = [1,2,3,4,5]#this is for line 10
    n = len(nums)
    count = findRotationCount(nums,n)
    if count == 0:
        print(f'The list is already sorted')
    else:
        print(f'The list is rotated {count} times')



