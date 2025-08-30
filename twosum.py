def two_sum(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(n):
        remaining = target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i
    
    
    
    
    
nums = list(map(int,input("Enter the nums: ").split(" ")))
target = int(input("Enter the target value: "))
print(two_sum(nums,target))