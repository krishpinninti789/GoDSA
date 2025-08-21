def hashing(n,m):
    hash_list = [0]*(len(n)+1)
    for num in n:
        hash_list[num]+=1
    for num in m:
        if num<0 or num>len(n)-1:
            print(0)
        else:
            print(hash_list[num])

print("Enter the numbers to the two lists: ")
n = list(map(int,input().split(" ")))
m = list(map(int,input().split(" ")))
hashing(n,m)