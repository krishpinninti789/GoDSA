def recurrsion(i,n):
    if i==n:
        return
    else:
        print(i)
        recurrsion(i+1,n)

recurrsion(1,10)