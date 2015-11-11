# file: gjSolver.py
"""
Python script for MECH2700, 2015, Semester 2.
Contains a generic Gauss-Jordan matrix solver that reduces a matrix
until a Gauss-Jordan Matrix is achieved. This solver is equipped to
handle floats and complex numbers.
The functions in this program have been abstracted in order to
make use of them in other programs.

R. C. Mitchell
19 Oct 2015
"""

#---------------------------------------------------------------------
# Import appropriate modules
from math import *
import numpy as np

#---------------------------------------------------------------------
# Global definitions of the variables for ease of editing


#---------------------------------------------------------------------
# Start function definition

def GaussJordan(A, b):
    """
    Gauss-Jordan Matrix elimination solver with partial pivoting.

    Params:
        A: square (nxn) matrix of coefficients
        B: column vector of RHS values (nx1 matrix)

    Returns:
        x, which is the solution of Ax = b
    """
    rows, cols = A.shape
    c = np.hstack([A, b])
    z = np.complex(1j)
    # print 'z = ', j, ' & Type(z)', type(j)        # Check

    for j in range(0, rows):
        # Find pivot
        p = j
        for i in range(j + 1, rows):
            if abs(c[i, j]) > abs(c[p, j]): p = i

        # Test for singularity by comparison to a small number
        if abs(c[p, j]) < 1.0e-15:
            raise RuntimeError('Matrix may be singular')

        # Swap rows using the pivot & record the change
        c[p,:], c[j,:] = c[j,:].copy(), c[p,:].copy()

        # Perform the elimination
        c[j,:] = c[j,:] / c[j, j]
        for i in range(0,rows):
            if i != j:
                c[i,:] = c[i,:] - c[i, j]*c[j,:]
    I, x = c[:, 0:rows], c[:, -1]
        
    return x

def ConditionNumber(A):
    """
    Assuming that the matrix is non-singular, its condition number can be
    calculated as the scalar of
    ||A||.||A^(-1)||
    The actual value depends on which norm is used, but for this function
    the row-sum norm is used.

    Params:
        A: square (nxn) matrix of coefficients

    Returns:
        norm, as a float
    """
    # Test for singularity by comparison to a small number
    if abs(np.linalg.det(A)) < 1.0e-15:
        raise RuntimeError('Matrix may be singular')
    return float(np.linalg.norm(A, 1))

print 'Ready for use'

if __name__ == "__main__":

    # Check code is working with 2 smaller matrices
    '''A = np.array([[4.0, -2.0, 1.0],
                  [-3.0, -1.0, 4.0],
                  [1.0, -1.0, 3.0]])
    b = np.array([[15.0, 8.0, 13]]).transpose()
    print 'A = ', A
    print 'B = ', b
    x = GaussJordan(A, b)
    print 'x = ', x
    print 'Check RHS = ', np.dot(A, x)

    A = np.array([[0.0, 2.0, 0.0, 1.0],
                  [2.0, 2.0, 3.0, 2.0],
                  [4.0, -3.0, 0.0, 1.0],
                  [6.0, 1.0, -6.0, -5.0]])
    b = np.array([[0.0, -2.0, -7.0, 6.0]]).transpose()
    print 'A = ', A
    print 'B = ', b
    x = GaussJordan(A, b)
    print 'x = ', x
    print 'Check RHS = ', np.dot(A, x)'''
