from math import *

def count_digits(num):
    # count=0
    # if num<0:
    #     num = -num
    # while num>0:
    #     num = num//10
    #     count+=1
    # return count
    
    
    #log approach
    
    return int(log10(num)+1)

n = int(input("Enter the number: "))
print("Number of digits are: ",count_digits(n))