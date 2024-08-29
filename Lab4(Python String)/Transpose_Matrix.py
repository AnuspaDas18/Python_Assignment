def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose_matrix(matrix)
print("Transpose of matrix:")
for row in transposed_matrix:
    print(row)
