def remove_duplicates(nums):
    i=0
    j=i+1
    while j<len(nums):
        if nums[i]!=nums[j]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        
        
        j+=1
    return i+1

nums = list(map(int,input("Enter the numbers: ").split()))
print(remove_duplicates(nums))