def transpose_matrix(matrix):
    if not matrix:
        return []

    # Get dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix for the transpose
    transpose = [[0] * rows for _ in range(cols)]

    # Fill the transpose matrix
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose
# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
