def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
    
n= int(input("Enter a number: "))
print(factorial(n))