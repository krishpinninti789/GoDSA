def search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1


    
nums = list(map(int,input("Enter the numbers: ").split()))
k = int(input("Enter the target element: "))
print(search(nums,k))