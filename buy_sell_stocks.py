def stocks(nums):
    
    max_profit = 0
    min_price = float('inf')
    for i in range(len(nums)):
        min_price = min(min_price,nums[i])
        max_profit = max(max_profit,nums[i]-min_price)
    return max_profit
     

nums = list(map(int,input("Enter the nums: ").split(" ")))
print(stocks(nums))