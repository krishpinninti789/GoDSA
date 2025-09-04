def binary(arr,target,low,high):
    low = 0
    high = len(arr)-1
    if low>=high:
        return -1
    mid = (low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary(arr,target,mid+1,high)
    else:
        return binary(arr,target,low,mid-1)
    

nums = list(map(int,input("Enter the numbers: ").split()))
target = int(input("Enter a number: "))
print(binary(nums,target,0,len(nums)))