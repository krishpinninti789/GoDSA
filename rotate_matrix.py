def rotate(matrix):
    result = []
    r= len(matrix)
    c = len(matrix[0])
    col_ind=0
    for _ in range(c):
        rotate_col =[]
        for j in range(c-1,-1,-1):
            rotate_col.append(matrix[j][col_ind])
        col_ind+=1
        result.append(rotate_col)
    for i in range(r):
        for j in range(c):
            matrix[i][j] = result[i][j]
    return matrix
            
    
matrix = []   
m = int(input("Enter the matrix row size: "))
n = int(input("Enter the matrix col size: "))
for i in range(m):
    row = list(map(int, input().split()))  # read a row
    matrix.append(row)
# print(matrix)
print(rotate(matrix))