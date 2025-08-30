def max_ones(nums): 
    n = len(nums)
    count=0
    max_count=0
    
    for i in range(n):
        if nums[i]==1:
            count+=1
        else:
            max_count = max(count,max_count)
            count = 0
            
    return max(max_count,count)
    

nums = list(map(int,input("Enter the nums: ").split(" ")))
print("Max ones are : ",max_ones(nums))