def setZeroes( matrix):
    c = len(matrix[0])
    r= len(matrix)
    row_track = [0 for _ in range(r)]
    col_track = [0 for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                row_track[i]=-1
                col_track[j]=-1
    for i in range(r):
        for j in range(c):
            if row_track[i]==-1 or col_track[j]==-1:
                matrix[i][j]=0
    return matrix

matrix = []
m = int(input("Enter the matrix row size: "))
n = int(input("Enter the matrix col size: "))
for i in range(m):
    row = list(map(int, input().split()))  # read a row
    matrix.append(row)
print(matrix)
print(setZeroes(matrix))