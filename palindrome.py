def fn(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return fn(s,l+1,r-1)

s = input("Enter a string: ")
print(fn(s,0,len(s)-1))