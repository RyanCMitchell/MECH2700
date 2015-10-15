# file: tutorial3.py
"""
Python program for MECH2700
All the functions required to complete tutorial 3.
Various iterative methods as well as some straight forward
math equations.
R. C. Mitchell
2015-09-10
"""

from math import *
import matplotlib.pylab as plt
from random import *

#------------------------------------------------------------------
# Global definitions



#------------------------------------------------------------------
# Functions

def epsilon():
    """
    Calculates the smallest possible value of machine precision achievable
    by the computer.
    """
    epsilon = 1.0       # define epsilon as 1 as per sheet
    eps = 2.0           # define ep1 and allow it to enter the while loop
    iterations = 0      # count the iterations to determine bit size 
    while eps > 1.0:
        epsilon = epsilon / 2.0
        eps = epsilon + 1.0
        iterations += 1
    epsilon = epsilon * 2.0
    return epsilon, iterations

def CubeRootDX(number):
    """
    Calculates the cube root of a number
    """
    root = 0.1
    dx = 0.1
    iterations = 0
    while dx > 1.0e-6:
        if pow(root, 3) < float(number):
            root = root + dx
        else:
            root = root - dx
            dx = dx / 10
        #print 'Number: {0:.3f} & root: {1:.3f} & iterations: {2:.0f}'\
        #.format(number, root, iterations)
        iterations += 1
    return root, iterations

def CubeRootNewton(number):
    """
    Calculates the cube root of a number using Newton's method
    """
    root = 1.0
    number = float(number)
    iterations = 0
    while abs(pow(root,3) - number) > 1.0e-6:
        root = root - ((pow(root,3)- number) / (3*pow(root,2)))
        #print 'Number: {0:.3f} & root: {1:.3f} & iterations: {2:.0f}'\
        #.format(number, root, iterations)
        iterations += 1
    return root, iterations


def thermo(Tc, tol=0.01, iterations=100):
    """
    Question 3:
    Calculates the temperature of the gas measured by the thermometer
    using the bisection method. Ts must be guessed first.
    """
    h = 8.3         # Convection heat transfer coefficient
    eps = 0.9       # Emissivity of the sensing element
    sig = 5.669e-8  # Stefan-Boltzmann constant
    Ts = 278        # Wall temperature
    Tg = 302        # Gas Temperature
    Tc = Tc         # Measured Temp -> what we're looking for
    a = -(h/(sig*eps))
    b = pow(Ts,4) + ((h*Tg)/(sig*eps))
    #print a+b

    # quick function for determining the sign of a number
    sign = lambda x: copysign(1, x)
    
    loopCount = 0
    while loopCount < iterations:
        c = (a+b)/2
        print c
        if Tc == a+b or (b-a)/2 < tol:   # Solution found
            return c
        elif a+b == sign(a):
            a = c
        else:
            b = c

        loopCount += 1
    return -1

def estimatePi(number=500000):
    """
    Question 4:
    Approximates the value of Pi/4 using a Monte Carlo simulation within
    a unit square. Results are plotted.
    """
    x = []
    y = []
    count = 0
    while count <= number:
        # coordinates for use
        xcoord = random()
        ycoord = random()

        # add coordinates to the list
        x.append(xcoord)
        y.append(ycoord)
        
        count += 1          # increment counter

    '''
    # Plot any graphs required
    env = plt.plot(physEnvX, physEnvY, 'b', label='Environment')
    traj = plt.plot(trajNoDragX, trajNoDragY, 'r--', label='Trajectory')
    plt.grid(b=True, which='major', color='k', linestyle='-')
    plt.suptitle('Bread Slingshot - No Drag')   # Set the graph title
    plt.legend(loc='upper right')               # Set the legend location
    plt.ylabel('Height (m)')                    # Set the y-axis label
    plt.xlabel('Distance (m)')                  # Set the x-axis label
    plt.ylim([-5,50])                           # Set the y-axis limits
    plt.xlim([-5,120])                          # Set the x-axis limits
    plt.show()                                 # Make the graph appear
    '''
    return x, y

print 'Ready for action'

'''
# Plot any graphs required
env = plt.plot(physEnvX, physEnvY, 'b', label='Environment')
traj = plt.plot(trajNoDragX, trajNoDragY, 'r--', label='Trajectory')
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.suptitle('Bread Slingshot - No Drag')   # Set the graph title
plt.legend(loc='upper right')               # Set the legend location
plt.ylabel('Height (m)')                    # Set the y-axis label
plt.xlabel('Distance (m)')                  # Set the x-axis label
plt.ylim([-5,50])                           # Set the y-axis limits
plt.xlim([-5,120])                          # Set the x-axis limits
plt.show()                                  # Make the graph appear




if __name__ == "__main__":

    print("Begin program...")
    text = input("Enter a value for the number of terms: ")
 

'''











