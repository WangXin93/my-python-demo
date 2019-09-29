import numpy as np
from numpy.linalg import qr

np.random.seed(2033)
a = np.random.randn(9, 6)
q, r = qr(a)
print(np.allclose(a, np.dot(q, r)))

def my_norm(v):
    """L2 norm
    """
    return np.sqrt(np.square(v).sum())

def my_qr(a):
    """QR factorization
    The orthonormal matrix Q can be computed with Gram-Schmidt algorithm.
        for i = 1, ..., k,
            1. Orthogonalization. q_tilde = a_i - (q_1^T a_i)q_1 - ... - (q_{i-1}^T a_i)q_{i-1}
            2. Test for linear dependence. if q_tilde = 0, quit
            3. Normalization. q_i = q_tilde/||q_tilde||
    
    The R can be computed by:
         if i <= j, R_{ij} = q_i^Ta_j
         if i > j, R_{ij} = 0

    Reference:
        Introduction to Applied Linear Algebra Vector, matrix, least square -- Stephen Boyd
    """
    row, col = a.shape
    
    q_list = [a[:, 0] / my_norm(a[:, 0])]
    for c in range(1, col):
        q_tilde = a[:, c]
        for i in range(c):
            q_tilde -= np.dot(q_list[i], a[:, c]) * q_list[i]
        if np.all(q_tilde == 0):
            continue
        else:
            q_list.append(q_tilde / my_norm(q_tilde))
    q = np.stack(q_list, axis=1)

    r = np.zeros((q.shape[1], col))
    for r_row in range(q.shape[1]):
        for r_col in range(col):
            if r_row > r_col:
                continue
            else:
                r[r_row, r_col] = np.dot(q[:, r_row], a[:, r_col])

    return q, r

my_q, my_r = my_qr(a)
print(np.allclose(a, np.dot(my_q, my_r)))


def my_inv(a):
    """ matrix inverse with QR factorization
    A = QR
    A^{-1} = (QR)^{-1} = R^{-1} Q^{-1} = R^{-1} Q.T

    1. QR factorization. A = QR
    2. For i = 1, ..., n
        solve the triangular equation R b_i = q_tilde using back substitution
    """
    q, r = my_qr(a)
    q_inv = q.T

    b_list = []
    for q_col in range(q_inv.shape[1]):
        q_tilde = q_inv[:, q_col]
        b = solve_upper_tri(r, q_tilde)
        b_list.append(b)
    
    inv = np.stack(b_list, axis=1)
    return inv

def solve_upper_tri(r, b):
    """ Solve upper triangle linear equation with back subsitution
    """
    x_list = []
    for n in range(b.shape[0]-1, -1, -1):
        x_left = b[n]
        for i in range(len(x_list)):
            x_left -= x_list[i] * r[n, b.shape[0]-1-i]
        x = x_left / r[n, n]
        x_list.append(x)
    x_list = x_list[::-1]
    x = np.array(x_list)
    return x

inv = my_inv(a)
print(np.allclose(np.linalg.pinv(a), inv))