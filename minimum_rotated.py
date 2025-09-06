def findMin(nums):
    low=0
    high = len(nums)-1
    mini = float('inf')
    while low<=high:
        mid = (low+high)//2
        if nums[mid]<=nums[high]:
            mini = min(mini,nums[mid])
            high = mid-1
        else:
            mini = min(mini,nums[low])
            low=mid+1
    return mini

nums = list(map(int,input("Enter the numbers: ").split()))
print(findMin(nums))