def missing(nums):
    n = len(nums)
    return int(((n*(n+1))/2)-sum(nums))
    
    
    
    
nums = list(map(int,input("Enter the nums: ").split(" ")))
print("Missing number is : ",missing(nums))