import random

from utils import time_f


MATRIX_SIZE = 1000


# Generate matrix with random number
def generate_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for _ in range(size):
            matrix[i].append(random.randint(0, 10))
    return matrix


# Pretty print matrix as a table with columns and rows
def pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print()


# Give two matrices, return the result of matrix multiplication
def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix2[0])):
            result[i].append(0)
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


# Add matrices pairwise, return new matrix as a result.
def matrix_add(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[i])):
            result[i].append(matrix1[i][j] + matrix2[i][j])
    return result


# Apply threshold to matrix, if value is less than threshold, set it to value
# else set it to abs(1 - value). Return new matrix as a result.
def apply_threshold(matrix, threshold, value=1):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if matrix[i][j] < threshold:
                new_matrix[i].append(value)
            else:
                new_matrix[i].append(abs(1 - value))
    return new_matrix


@time_f
def main(matrix_size):
    A, B  = generate_matrix(matrix_size), generate_matrix(matrix_size)

    C = matrix_multiply(A, B)
    D = apply_threshold(C, 200, 0)
    E = apply_threshold(C, 200, 1)
    F = matrix_add(D, E)

if __name__ == "__main__":
    main(1000)
