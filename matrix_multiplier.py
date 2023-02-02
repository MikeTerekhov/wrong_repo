import numpy as np


def matrix_multiplier(mat1, mat2):
    row1, col1 = np.shape(mat1)
    row2, col2 = np.shape(mat2)
    result = []

    # iterate through rows of mat1
    for i in range(len(mat1)):
        # iterate through cols of mat2
        for j in range(len(mat2[0])):
            # iterate through rows of mat2
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
