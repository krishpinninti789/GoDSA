def max_subarray(nums):
    
    max_sum = float('-inf')
    current_sum = 0
    
    for x in nums:
        current_sum = max(x,current_sum+x)
        max_sum = max(max_sum,current_sum)
    return max_sum
    

nums = list(map(int,input("Enter the nums: ").split(" ")))
print(max_subarray(nums))