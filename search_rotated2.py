def search(nums, target):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[mid]<=nums[high]:
            if nums[mid]<=target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low=mid+1
    return False


nums = list(map(int,input("Enter the numbers: ").split(" ")))
target = int(input("Enter the target element: "))
print(search(nums,target))