def getNoZeroIntegers(n):
    for i in range(n):
        j = n-i
        if not '0' in str(j) and not '0' in str(i):
            return [i,j]
        
        
n = int(input("Enter a number: "))
print(getNoZeroIntegers(n))