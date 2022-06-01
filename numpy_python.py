import numpy as np

from utils import time_f


MATRIX_SIZE = 10000


# Generate matrix with random integers
def generate_matrix(size: int) -> np.ndarray:
    matrix = np.random.randint(0, 10, (size, size))
    return matrix


# Pretty print matrix
def pretty_print(matrix: np.ndarray):
    print(matrix, "\n")


# Give two matrices, return the result of matrix multiplication
def matrix_multiply(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    return np.matmul(matrix1, matrix2)


# Add matrices pairwise and return new matrix as a result
def matrix_add(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    return matrix1 + matrix2


# Apply threshold to matrix, if value is less than threshold, set it to value
# else set it to abs(1 - value). Return new matrix as a result.
def apply_threshold(matrix: np.ndarray, threshold: int, value: int = 1) -> np.ndarray:
    return np.where(matrix < threshold, value, abs(1 - value))


@time_f
def main():
    A, B = generate_matrix(MATRIX_SIZE), generate_matrix(MATRIX_SIZE)

    C = matrix_multiply(A, B)
    pretty_print(C)

    D = apply_threshold(C, 200, 0)
    pretty_print(D)

    E = apply_threshold(C, 200, 1)
    pretty_print(E)

    F = matrix_add(D, E)
    pretty_print(F)


if __name__ == '__main__':
    main()