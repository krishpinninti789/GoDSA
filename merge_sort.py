def merge_array(left,right):
    n = len(left)
    m = len(right)
    i,j=0,0
    result = []
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<n:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)


nums = list(map(int,input("Enter the numbers: ").split()))
print(merge_sort(nums))
    
    
    
        