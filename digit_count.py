def count_digits(num):
    count=0
    if num<0:
        num = -num
    while num>0:
        num = num//10
        count+=1
    return count

n = int(input("Enter the number: "))
print("Number of digits are: ",count_digits(n))