def reverse(str1):
    
    words = str1.split(' ') 
    return " ".join(words[::-1])
        
str1 = input("Enter a string :")
print(reverse(str1))