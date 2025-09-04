def threeSum(nums):

    result=set()
    n = len(nums)
    for i in range(n):
        my_set= set()
        for j in range(i+1,n):
            third = -(nums[i]+nums[j])
            if third in my_set:
                temp = [nums[i],nums[j],third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
    return [list(i) for i in result]


nums = list(map(int,input("Enter the numbers: ").split()))
print(threeSum(nums))