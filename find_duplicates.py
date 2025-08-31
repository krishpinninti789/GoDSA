from collections import Counter
def find_duplicates(nums):
    result = []
    c= Counter(nums)
    for key,value in c.items():
        if value>1:
            result.append(key)
    return result    
    
nums = list(map(int,input("Enter the numbers: ").split()))
print(find_duplicates(nums))