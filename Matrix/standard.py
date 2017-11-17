def multiplication(matrix_a, matrix_b):
    rows_amount_a, columns_amount_a = len(matrix_a), len(matrix_a[0])
    rows_amount_b, columns_amount_b = len(matrix_b), len(matrix_b[0])

    matrix_c = [[0 for i in range(columns_amount_b)] for j in range(rows_amount_a)]

    print(matrix_c)
    for i in range(rows_amount_a):
        for j in range(columns_amount_a):
            for k in range(rows_amount_b):
                matrix_c[i][k] += matrix_a[i][j] * matrix_b[j][k]

    return matrix_c

if __name__ == '__main__':
    A = [[1, -1], [2, 0], [3, 0]]
    B = [[1, 1], [2, 0]]

    print(multiplication(A, B))