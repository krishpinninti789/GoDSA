def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[min_index]>nums[j]:
                min_index = j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums

nums = list(map(int,input("Enter the numbers: ").split()))
print(selection_sort(nums))