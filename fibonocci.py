def fib(num):
    if num==0 or num==1:
        return num
    return fib(num-1)+fib(num-2)

n = int(input("Enter the nth fibbonaci you want: "))
print(fib(n))