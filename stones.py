def numJewelsInStones(jewels, stones):
    c = 0
        # jewels = set(jewels)
    for i in stones:
        if i in jewels:
            c+=1
    return c

j = input("Enter the jewels: ")
st = input("Enter the stones: ")
print(numJewelsInStones(j,st))

