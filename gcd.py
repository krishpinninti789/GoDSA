def gcd(n1,n2):
    max1 = max(n1,n2)
    while max1>=1:
        if n1%max1==0 and n2%max1==0:
            return max1
        max1-=1

print(gcd(48,18))