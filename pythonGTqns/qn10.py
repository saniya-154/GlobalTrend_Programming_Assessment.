def transpose_matrix(matrix):

    if not matrix:
        return []

    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
