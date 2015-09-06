# file: Assingment1.py
"""
Python program for MECH2700, 2015, Semester 2.
Contains all the functions required to complete Assignment 1.

R. C. Mitchell
2015-09-05
"""

#------------------------------------------------------------------
# Import appropriate modules
from math import *
import matplotlib.pylab as plt

#------------------------------------------------------------------
# Global definitions of the physical environment for plotting
# purposes to help visualise the scenario.
physEnvY = [1.8,0]          # Slingshot height
physEnvX = [0,0.5]          # Slingshot
for i in range(1,76,1):     # River
    physEnvX.append(i)
    physEnvY.append(0)
physEnvX.append(75)         # Left base of House
physEnvY.append(9)          # Left base of House height
for i in range(75,85,1):    # Roof of House
    physEnvX.append(i)
    physEnvY.append(9)
physEnvX.append(84)         # Right base of House
physEnvY.append(0)          # Right base of House height
for i in range(84,101,1):   # Continuation of ground
    physEnvX.append(i)
    physEnvY.append(0)

#plt.plot(physEnvX, physEnvY, 'b')
#plt.grid(b=True, which='major', color='k', linestyle='-')
#plt.show()


# Global definitions of the variables for ease of editing
trajX = [0]             # Initial x-coordinate in a list
trajY = [1.8]           # Initial y-coordinate in a list
drag = 0.55             # Dimensionless drag coefficient
diameter = 0.15         # Diameter of the loaf of bread in meters
radius = diameter / 2   # Radius of the loaf of bread in meters
mass = 0.7              # Mass of the loaf of bread in kg
rho = 1.2               # Density of the ambient air in kg/m^3
grav = 9.81             # Gravity in m/s^2

#------------------------------------------------------------------
# Start function definitions

def guess(velocity, thetaDeg, timeStep=1):
    """
    Initial calcultaion / integration of the function using guessed
    initial conditions. The function will also be plotted to help
    visualise the scenario.
    velocity in meters per second.
    theta in degrees.
    timeStep in seconds. The smaller the timeStep the more accurate
    the function.
    """
    
    # Clear all the variables
    theta = 0
    trajGuessX = []
    trajGuessY = []
    accelX = 0
    accelY = 0
    velocityX = 0
    velocityY = 0

    # Calculate / fill all the variables
    theta = radians(thetaDeg)
    trajGuessX = trajX
    trajGuessY = trajY
    #print trajGuessY
    accelX = ((rho*drag*pow((velocity*cos(theta)),2)*pi*pow(radius,2))
              /(2*mass))
    accelY = grav
    velocityX = velocity*cos(theta)
    velocityY = velocity*sin(theta)

    # Execute the mathematics and build a list of the coordinates
    while trajGuessY[-1] >= 0:
        velocityX = velocityX - accelX*timeStep
        accelX = ((rho*drag*pow(velocityX,2)*pi*pow(radius,2))
                   /(2*mass))
        velocityY = velocityY - accelY*timeStep
        x = trajGuessX[-1] + velocityX*timeStep
        y = trajGuessY[-1] + velocityY*timeStep
        trajGuessX.append(x)
        trajGuessY.append(y)

    #print trajGuessX[-1]

    # Plot the graphs of the trajectory and the physical environment
    env = plt.plot(physEnvX, physEnvY, 'b', label='Environment')
    traj = plt.plot(trajGuessX, trajGuessY, 'r--', label='Trajectory')
    plt.grid(b=True, which='major', color='k', linestyle='-')
    plt.suptitle('Bread Slingshot')
    plt.legend(loc='upper right')
    plt.ylabel('Height (m)')
    plt.xlabel('Distance (m)')
    plt.ylim([-5,50])
    plt.xlim([-5,120])
    plt.show()

    print trajY
    
    return

def noDrag():
    """
    Comments here
    """
    trajNoDragX = trajX          # Copy the lists for the guess
    trajNoDragY = trajY

    # Execute the mathematics and build a list of the coordinates
    #maths goes here

    # Plot the graphs of the trajectory and the physical environment
    #plt.plot(trajGuessX, trajGuessY, 'r--')
    #plt.hold()
    #plt.plot(physEnvX, physEnvY, 'b')
    #plt.grid(b=True, which='major', color='k', linestyle='-')
    #plt.show()
    
    return


def optimal():
    """
    Comments here
    """
    trajOptimalX = trajX          # Copy the lists for the guess
    trajOptimalY = trajY

    # Execute the mathematics and build a list of the coordinates
    #maths goes here

    # Plot the graphs of the trajectory and the physical environment
    #plt.plot(trajGuessX, trajGuessY, 'r--')
    #plt.hold()
    #plt.plot(physEnvX, physEnvY, 'b')
    #plt.grid(b=True, which='major', color='k', linestyle='-')
    #plt.show()
    
    return


#if __name__ == "__main__":
print("Ready for action! ;)")














