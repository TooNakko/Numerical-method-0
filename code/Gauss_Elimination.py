import numpy as np

def gauss_jordan_elimination(A, b):
    n = len(b)

    augmented_matrix = np.hstack((A, np.array(b).reshape(n, 1))).astype(float)

    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[max_row][i]):
                max_row = j
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        augmented_matrix[i] /= augmented_matrix[i][i]

        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    x = augmented_matrix[:, -1]

    return x


A = np.array([[6, 2, 8],
              [3, 5, 2],
              [0, 8, 2]])

b = np.array([26, 8, -7])

print("x =", gauss_jordan_elimination(A, b))