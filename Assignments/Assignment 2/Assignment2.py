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

def guess():
    """
    Comments
    """
    # Plot the graphs of the trajectory and the physical environment
    env = plt.plot(physEnvX, physEnvY, 'b', label='Environment')
    traj = plt.plot(trajXY[0], trajXY[1], 'r--', label='Trajectory')
    plt.grid(b=True, which='major', color='k', linestyle='-')
    plt.suptitle('title')           # Set the graph title
    plt.legend(loc='upper right')   # Set the legend location
    plt.ylabel('y-axis')            # Set the y-axis label
    plt.xlabel('x-axis')            # Set the x-axis label
    plt.ylim([-5,50])               # Set the y-axis limits
    plt.xlim([-5,120])              # Set the x-axis limits
    # Save the graph as ___ with a resolution of dpi
    plt.savefig('graph.png', dpi=400)
    plt.show()                      # Make sure the graph appears

    print 'The bread lands at: {0:.3f}, {1:.3f}'.format(0, 1)
    return


print("Steady on there! Lets take it nice and slow...")









