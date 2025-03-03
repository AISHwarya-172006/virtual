def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    return transpose
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
result = transpose_matrix(matrix)
for row in result:
    print(row)
