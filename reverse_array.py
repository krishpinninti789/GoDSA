def reverse(nums,l,r):
    if l>=r:
        return nums
    
    nums[l],nums[r] = nums[r],nums[l]
    return reverse(nums,l+1,r-1)

n=[1,3,2,6,7,9]
print(reverse(n,0,len(n)-1))
    