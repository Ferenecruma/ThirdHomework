import os
import ctypes

import numpy as np
from numpy.ctypeslib import ndpointer

from utils import time_f


root_path = os.path.dirname(os.path.abspath(__file__))
library_path = root_path + "/matrix_operations.so"
fast_lib = ctypes.cdll.LoadLibrary(library_path)

_intpp_in = ndpointer(dtype=np.uintp, ndim=1, flags="C")
_intpp_out = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))

# Function definitions for the C library
matrix_mul = fast_lib.matrix_multiply
matrix_mul.argtypes = [_intpp_in, _intpp_in, ctypes.c_int]
matrix_mul.restype = _intpp_out

matrix_add = fast_lib.matrix_add
matrix_add.argtypes = [_intpp_in, _intpp_in, ctypes.c_int]
matrix_add.restype = _intpp_out

apply_threshold = fast_lib.apply_threshold
apply_threshold.argtypes = [_intpp_in, ctypes.c_int, ctypes.c_int, ctypes.c_int]
apply_threshold.restype = _intpp_out


def to_numpy(xpp, size: int) -> np.ndarray:
    return np.array(
        [[xpp[i][j] for j in range(size)] for i in range(size)],
    )

def get_ctype_pointer(matrix: np.ndarray):
    return (
        matrix.ctypes.data + np.arange(matrix.shape[0]) * matrix.strides[0]
    ).astype(np.uintp)


def matrix_mul_wrapper(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    xpp = get_ctype_pointer(matrix1)
    ypp = get_ctype_pointer(matrix2)
    size = ctypes.c_int(matrix1.shape[0])
    res = matrix_mul(xpp, ypp, size)
    return to_numpy(res, matrix1.shape[0])


def matrix_add_wrapper(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    xpp = get_ctype_pointer(matrix1)
    ypp = get_ctype_pointer(matrix2)
    size = ctypes.c_int(matrix1.shape[0])
    res = matrix_add(xpp, ypp, size)
    return to_numpy(res, matrix1.shape[0])


def apply_threshold_wrapper(matrix: np.ndarray, threshold: int, value: int) -> np.ndarray:
    xpp = get_ctype_pointer(matrix)
    size = ctypes.c_int(matrix.shape[0])
    res = apply_threshold(xpp, size, threshold, value)
    return to_numpy(res, matrix.shape[0])


def generate_matrix(size: int) -> np.ndarray:
    matrix = np.random.randint(0, 10, (size, size), dtype=np.int32)
    return matrix


@time_f
def main(matrix_size: int):
    A, B  = generate_matrix(matrix_size), generate_matrix(matrix_size)
    C = matrix_mul_wrapper(A, B)
    D = apply_threshold_wrapper(C, 200, 0)
    E = apply_threshold_wrapper(C, 200, 1)
    F = matrix_mul_wrapper(D, E)


if __name__ == "__main__":
    main(matrix_size=1000)