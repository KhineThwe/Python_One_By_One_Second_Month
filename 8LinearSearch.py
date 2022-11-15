#Linear Search
#data array = 20 30 40 50 60 70 80
#key = 60
#Linear Search သည် ကျွန်တော်တို့ထိပ်ဆုံး ရှာ
def linear_search(array,n,x):
    for i in range(n):
        if array[i] == x:
            return i
    return -1
if __name__ == "__main__":
    nums = [2,5,10,11,15,16,17,19,25,30,40]
    find_no = int(input("Please enter a number to find: "))
    n = len(nums)
    result = linear_search(nums,n,find_no)
    if result == -1:
        print("Element not found!!")
    else:
        print("Elements found at index: ",result)
