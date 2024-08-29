def is_sparse_matrix(matrix):
    zero_count = sum(1 for row in matrix for element in row if element == 0)
    total_elements = len(matrix) * len(matrix[0])
    return zero_count > total_elements / 2

# Example usage:
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 2]
]
if is_sparse_matrix(matrix):
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")
