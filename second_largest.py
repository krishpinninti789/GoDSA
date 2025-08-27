def second_largest(nums):
    max1 = max(nums)
    s_largest = float('-inf')
    for i in range(len(nums)):
        if nums[i]>s_largest and nums[i]!=max1:
            s_largest = nums[i]
    return s_largest

nums = list(map(int,input("Enter the numbers: ").split()))
print(second_largest(nums))