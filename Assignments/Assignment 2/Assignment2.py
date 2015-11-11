# file: Assingment2.py
"""
Python program for MECH2700, 2015, Semester 2.
Contains all the functions required to complete Assignment 2.

R. C. Mitchell
19 Oct 2015
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

def TransferFunction(w, Vin=5):
    """
    This function calculates the Transfer Function of the Chebyshev
    circuit. The Tranfer Function is an independant multiplication
    factor; regardless of what is selected for Vin, the result will
    be the same for the same frequency.
    w --> frequency in Hertz (limit from 10Hz to 10MHz)
    Vin --> Volatge in, in Volts
    """
    # Constants
    R1 = 378.0      # Ohms
    R2 = R1
    C1 = 532e-12    # 532pF
    C2 = 944e-12    # 944pF
    C3 = C2
    C4 = C1
    L1 = 91.3e-6    # 91.3uH
    L2 = 101e-6     # 101uH
    L3 = L1
    j = np.complex(1j)

    # Create [A - Matrix] and answer, [b = Array]
    A = np.array([[R1, (-j/(w*C1)), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, (-j/(w*C1)), -j*w*L1, (j/(w*C2)), 0.0, 0.0,
                   0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, (-j/(w*C2)), -j*w*L2, (j/(w*C3)),
                   0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, (-j/(w*C3)), -j*w*L3,
                   (j/(w*C4)), 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (-j/(w*C4)), -R2],
                  [1, -1, -1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 1, -1, -1, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 1, -1, -1, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, -1, -1]])
    b = np.array([Vin, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], float)
    # Checks:
    # print 'A = ', A, ' & Type(A) = ', type(A), ' & shape = ', A.shape
    # print 'b = ', b, ' & Type(b) = ', type(b), ' & shape = ', b.shape

    # Check for singularity in matrix.
    if np.linalg.det(A) == 0:
        # Check:
        # print np.absolute(np.linalg.det(A))   # Check det(A)
        print "Singular"
        return -1
    # If non-singular continue solving
    else:
        i = np.linalg.solve(A, b)
        # print 'i = ', i, ' & shape = ', i.shape   # double check format
        # print i[-1]                               # check last element

    # Checks to see the solution vector is correct
    # print 'check...'
    # print 'Ai = ', np.dot(A,i)

    Vout = R2 * np.absolute(i[-1])  # Vout = R2 * magnitude of last current

    return Vout/Vin

def Bode(start=10, end=10e7):
    """
    Makes use of TransferFunction to calculate the transfer function for
    a range of frequencies and plots the frequency response both linearly
    and on a semi-log (frequency axis).
    No values are required. The default range is 10Hz to 10MHz and cannot
    be extended but can be narrowed.
    """
    Magnitude = []      # Empty list for magnitude values
    freq = []           # Empty list for frequency values
    incrementer = 100   # Frequency interation incrementer size

    # For each incremental step in the range start -> stop, calculate the
    # transfer function
    for i in xrange(int(start), int(end), incrementer):
        freq.append(i)
        #print 'f = ', freq
        Magnitude.append(20*log(TransferFunction(i, 1), 10))
        #print 'Mag = ', Magnitude
        Gain = 20*log(TransferFunction(int(start), 1), 10)

        if i > int(start) + incrementer:
            if 0 < Magnitude[-1] - Magnitude[-2] and Magnitude[-1] - Magnitude[-2] < 1:
                cutOff = freq[-1]

    print 'The gain is {0:.2f}dB and the Cut-Off frequency is {1:.2f}Hz, '\
          '{2:.2f}kHz, {3:.2f}MHz'.format(Gain, cutOff, cutOff/1000, cutOff/1000000)


    # Plot the graphs of the trajectory and the physical environment
    # Only tried running 1 plot at a time. Comment out the other one.
    bode = plt.plot(freq, Magnitude, 'b', label='Frequency Response')
    #bode = plt.semilogx(freq, Magnitude, 'b', label='Frequency Response')
    plt.grid(b=True, which='both', color='k', linestyle='-')
    plt.suptitle('Bode Plot of Chebyshev Filter')   # Set the graph title
    plt.legend(loc='lower left')    # Set the legend location
    plt.ylabel('Magnitude (dB)')    # Set the y-axis label
    plt.xlabel('Frequency (Hz)')    # Set the x-axis label
    plt.show()                      # Make sure the graph appears

    return Gain, cutOff


print("Steady on there! Lets take it nice and slow...")

