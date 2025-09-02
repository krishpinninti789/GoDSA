def freq(s):
    hash_list = {}
    for ch in s:
        hash_list[ch] = hash_list.get(ch,0)+1
    return hash_list
    
    
s = input("Enter the string: ")
print(freq(s))