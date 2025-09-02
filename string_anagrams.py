
def anagrams(s1,s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())
    
     
s1 = input("Enter the string: ")
s2 = input("Enter the string: ")
print(anagrams(s1,s2))