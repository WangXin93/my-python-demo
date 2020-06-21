"""
jacobi method: https://www.youtube.com/watch?v=bR2SEe8W3Ig
Gauss-Seidel method: https://www.youtube.com/watch?v=F6J3ZmXkMj0
"""

import numpy as np
import numpy.linalg as la

def jacobi_iteration(A, x, b):
    x_new = np.zeros_like(x)
    for i in range(x.shape[0]):
        x_new[i] = b[i]
        for j in range(x.shape[0]):
            if i != j:
                x_new[i] = x_new[i] - A[i, j]*x[j]
        x_new[i] = x_new[i] / A[i, i]
    residual = la.norm((A @ x_new - b))
    print("x={}, residual={:4f}".format(x_new, residual))
    return x_new

def gauss_seidel_iteration(A, x, b):
    for i in range(x.shape[0]):
        x[i] = b[i]
        for j in range(x.shape[0]):
            if i != j:
                x[i] = x[i] - A[i, j]*x[j]
        x[i] = x[i] / A[i, i]
    residual = la.norm((A @ x - b))
    print("x={}, residual={:4f}".format(x, residual))
    return x


if __name__ == "__main__":
    A = np.array([
        [5, -1, 2],
        [3, 8, -2],
        [1, 1, 4]
    ])
    x = np.zeros(3)
    b = np.array([12, -25, 6])
    for _ in range(10):
        x = jacobi_iteration(A, x, b)

    A = np.array([
        [5, -1, 2],
        [3, 8, -2],
        [1, 1, 4]
    ])
    x = np.zeros(3)
    b = np.array([12, -25, 6])
    for _ in range(10):
        x = gauss_seidel_iteration(A, x, b)
