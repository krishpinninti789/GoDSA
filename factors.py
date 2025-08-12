from math import sqrt
def factors(num):
    # ls=[]
    # for i in range(1,num+1):
    #     if num%i==0:
    #         ls.append(i)
    # return ls
    
    #optimal solution
    ls = []
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            ls.append(i)
            if num//i!=i:
                ls.append(num//i)
    ls.sort()
    return ls


n = int(input("ENter the no: "))
ls = factors(n)
print("Factors are:")
for i in ls:
    print(i,end = " ")