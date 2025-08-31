def remove(nums):
    result = []
    item_counter = {}
    
    for item in nums:
        if item_counter.get(item,0)<2:
            result.append(item)
            item_counter[item]=item_counter.get(item,0)+1

    return result  
    
nums = list(map(int,input("Enter the numbers: ").split()))
print(remove(nums))