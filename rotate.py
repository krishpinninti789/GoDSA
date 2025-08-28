def rotate(nums,k):
    n = len(nums)
    nums[:] = nums[n-k:]+nums[:n-k]
    return nums
    
    
    
nums = list(map(int,input("Enter the numbers: ").split()))
k = int(input("Enter the k rotations: "))
print(rotate(nums,k))