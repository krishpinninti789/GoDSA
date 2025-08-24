def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        is_sorted = False
        for j in range(i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_sorted = True
        if is_sorted == False:
            return nums
        
    return nums

nums = list(map(int,input("Enter the numbers: ").split()))
print(bubble_sort(nums))