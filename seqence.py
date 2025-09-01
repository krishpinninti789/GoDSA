def sequence(nums):
    
    my_set = set(nums)
    max_count=0
    for i in nums:
        my_set.add(i)
    for i in my_set:
        if i-1 not in my_set:
            count=1
            u=i
            while u+1 in my_set:
                count+=1
                u+=1
            max_count=max(count,max_count)
    return max_count
    
    
nums = list(map(int,input("Enter the numbers: ").split()))
print(sequence(nums))