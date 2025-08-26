def largest_element(arr):
    largest = float('-inf')
    for i in range(len(arr)):
        largest = max(largest,arr[i])
    return largest

arr = list(map(int,input("Enter the elements of the array: ").split()))
print(largest_element(arr))







