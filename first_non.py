from collections import Counter
def non_repeating(nums):
    c = Counter(nums)
    for key,value in c.items():
        if value==1:
            return key
      
nums = list(map(int,input("Enter the numbers: ").split()))
print(non_repeating(nums))