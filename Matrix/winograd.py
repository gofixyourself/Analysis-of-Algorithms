def multiplication(matrix_a, matrix_b):
    rows_amount_a, column_amount_a = len(matrix_a), len(matrix_a[0])
    rows_amount_b, column_amount_b = len(matrix_b), len(matrix_b[0])

    half = rows_amount_b // 2
    rows_factors = [0 for i in range(rows_amount_a)]
    columns_factors = [0 for i in range(column_amount_a)]

    for i in range(rows_amount_a):
        for j in range(half):
            rows_factors[i] += matrix_a[i][2 * j] * matrix_a[i][2 * j + 1]

    for i in range(column_amount_b):
        for j in range(half):
            columns_factors[i] += matrix_b[2 * j][i] * matrix_b[2 * j + 1][i]

    matrix_c = [[0 for i in range(column_amount_b)] for j in range(rows_amount_a)]

    for i in range(rows_amount_a):
        for j in range(column_amount_b):
            matrix_c[i][j] = - rows_factors[i] - columns_factors[j]
            for k in range(half):
                matrix_c[i][j] += ((matrix_a[i][2 * k] + matrix_b[2 * k + 1][j])
                                   * (matrix_a[i][2 * k + 1] + matrix_b[2 * k][j]))

    if rows_amount_b % 2:
        for i in range(rows_amount_a):
            for j in range(rows_amount_b):
                matrix_c[i][j] += matrix_a[i][rows_amount_b - 1] * matrix_b[rows_amount_b - 1][j]

    return matrix_c

if __name__ == '__main__':
    A = [[1, -1], [2, 0], [3, 0]]
    B = [[1, 1], [2, 0]]

    print(multiplication(A, B))
