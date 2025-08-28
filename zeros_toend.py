def zeros(nums):
    n = len(nums)
    ls = []
    c=0
    for i in range(n):
        if nums[i]==0:
            c+=1
        else:
            ls.append(nums[i])
    nums[:] = ls+[0]*c
    return nums
           
    
    

nums = list(map(int,input("Enter the numbers: ").split()))
print(zeros(nums))