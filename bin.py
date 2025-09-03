def binary(n):
    bits = str(bin(n))
    return bits.count("1")
    
print(binary(13))