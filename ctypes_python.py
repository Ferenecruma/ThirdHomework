import os
import ctypes

import numpy as np
from numpy.ctypeslib import ndpointer


root_path = os.path.dirname(os.path.abspath(__file__))
library_path = root_path + "/matrix_operations.so"
fast_lib = ctypes.cdll.LoadLibrary(library_path)

_doublepp = ndpointer(dtype=np.uintp, ndim=1, flags="C")

matrix_mul = fast_lib.matrix_multiply
matrix_mul.argtypes = [_doublepp, _doublepp, _doublepp, ctypes.c_int]
matrix_mul.restype = _doublepp


def matrix_mul_wrapper(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    res = np.zeros_like(matrix1)
    size = ctypes.c_int(matrix1.shape[0])

    xpp = (matrix1.ctypes.data + np.arange(matrix1.shape[0]) * matrix1.strides[0]).astype(np.uintp)
    ypp = (matrix2.ctypes.data + np.arange(matrix2.shape[0]) * matrix2.strides[0]).astype(np.uintp)
    zpp = (res.ctypes.data + np.arange(res.shape[0]) * res.strides[0]).astype(np.uintp)

    matrix_mul(xpp, ypp, zpp, size)
    return res


if __name__ == '__main__':
    a = np.random.randint(0, 10, (10, 10))
    b = np.random.randint(0, 10, (10, 10))
    print(a)
    print(b)
    c = matrix_mul_wrapper(a, b)
    print(c)

# Pass a matrix argument to the c dynamic library function using ctypes.
# The c dynamic library function returns a matrix as a result.

