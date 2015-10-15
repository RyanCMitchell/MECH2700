# file: Assingment2.py
"""
Python program for MECH2700, 2015, Semester 2.
Contains all the functions required to complete Assignment 2.

R. C. Mitchell
2015 --> date
"""

#------------------------------------------------------------------
# Import appropriate modules
from math import *
import matplotlib.pylab as plt
import numpy as np

#------------------------------------------------------------------
# Global definitions of the variables for ease of editing


#------------------------------------------------------------------
# Start function definitions

def Filter(w, Vin=5):
    """
    Comments
    """
    # Constants
    R1 = 378.0        # Ohms
    R2 = R1     
    C1 = 532e-12    # 532pF  
    C2 = 944e-12    # 944pF
    C3 = C2
    C4 = C1
    L1 = 91.3e-6    # 91.3uH
    L2 = 101e-6     # 101uH
    L3 = L1
    j = np.complex(1j)
    # print 'j = ', j, ' & Type(j)', type(j)
    
    # Create A - Matrix and answer, b = Array, both as floats
    A = np.array([[R1, (-j/(w*C1)), 0, 0, 0, 0, 0, 0, 0],
                  [0, (-j/(w*C1)), -j*w*L1, (j/(w*C2)), 0, 0, 0, 0, 0],
                  [0, 0, 0, (-j/(w*C2)), -j*w*L2, (j/(w*C3)), 0, 0, 0],
                  [0, 0, 0, 0, 0, (-j/(w*C3)), -j*w*L3, (j/(w*C4)), 0],
                  [0, 0, 0, 0, 0, 0, 0, (-j/(w*C4)), -R2],
                  [1, -1, -1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, -1, -1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, -1, -1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, -1, -1]])
    b = np.array([Vin, 0, 0, 0, 0, 0, 0, 0, 0], float)
    # print 'A = ', A, ' & Type(A) = ', type(A), ' & shape = ', A.shape
    # print 'b = ', b, ' & Type(b) = ', type(b), ' & shape = ', b.shape

    # Check for singularity in matrix
    if np.linalg.det(A) == 0:
        print "Singular"
        return -1
    else:
        i = np.linalg.solve(A, b)
        #print 'i = ', i, ' & shape = ', i.shape

    # print 'check...'
    # print 'Ai = ', np.dot(A,i)

    print 'The bread lands at: {0:.3f}, {1:.3f}'.format(0, 1)
    return


print("Steady on there! Lets take it nice and slow...")









