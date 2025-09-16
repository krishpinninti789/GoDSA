def replaceNonCoprimes(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
         return a * b // gcd(a, b)
    stack = []
    for num in nums:
        stack.append(num)
        while len(stack) > 1:
            g = gcd(stack[-1], stack[-2])
            if g > 1: 
                a = stack.pop()
                b = stack.pop()
                stack.append(lcm(a, b))
            else:
                break
    return stack


nums = list(map(int,input("Enter the numbers: ").split()))
print(replaceNonCoprimes(nums))