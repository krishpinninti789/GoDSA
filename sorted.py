def is_sorted(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            return False
        
    return True

nums = list(map(int,input("Enter the numbers: ").split()))
print(is_sorted(nums))