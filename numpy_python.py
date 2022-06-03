import numpy as np

from utils import time_f


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
def main(matrix_size: int):
    A, B = generate_matrix(matrix_size), generate_matrix(matrix_size)
    
    C = matrix_multiply(A, B)
    D = apply_threshold(C, 200, 0)
    E = apply_threshold(C, 200, 1)
    F = matrix_add(D, E)

if __name__ == '__main__':
    main(100)