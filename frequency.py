def frequeny(nums,ele):
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i],0)+1
    return hash_map.get(ele)
    

print("Enter the elements to the list: ")
nums = list(map(int,input().split(' ')))
ele = int(input("Enter the element you want the freqency: "))
print("The frequency is: ",frequeny(nums,ele))
