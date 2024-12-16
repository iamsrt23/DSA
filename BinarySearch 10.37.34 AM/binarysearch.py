def binarysearch(nums,target):
    i = 0
    j = n-1
    while i <= j:
        mid  = i + (j-i) //2

        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            i = mid+1
        else:
            j = mid-1
    return -1

nums=[3,4,6,7,9,12,16,17]
target=12
n=len(nums)
result = binarysearch(nums,target)
print(result)
