def hashing(chars,list1):
    hash_list = [0]*27
    for ch in chars:
        ascii_value = ord(ch)
        index = ascii_value-97
        hash_list[index]+=1
    # print(hash_list)
    for ch in list1:
        asc = ord(ch)
        i = asc-97
        print(hash_list[i],end="-")
    
    pass

str1 = input("Enter the string: ").replace(" ", "")
print(str1)
ls = list(input("Enter the characters: ").split(' '))
hashing(str1,ls)