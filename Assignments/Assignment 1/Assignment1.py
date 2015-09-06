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

# Global definitions of the variables for ease of editing
trajXY = (0, 1.8)       # Initial x-coordinate in a list
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
    # Calculate / fill all the variables
    theta = radians(thetaDeg)       # Change the input angle into radians
    trajGuessX = []                 # Create an empty list
    trajGuessX.append(trajXY[0])    # Initialise the list
    trajGuessY = []                 # Create an empty list
    trajGuessY.append(trajXY[1])    # Initialise the list
    accelX = ((rho*drag*pow((velocity*cos(theta)),2)*pi*pow(radius,2))
              /(2*mass))            # Calculate the x-acceleration
    accelY = grav                   # Assign gravity to y-acceleration
    velocityX = velocity*cos(theta) # Calculate the x-velocity component
    velocityY = velocity*sin(theta) # Calculate the y-velocity component

    # Execute the mathematics and build a list of the coordinates.
    # While the bread is in the air perform calculations.
    # As it steps through it updates the velocities and accelerations
    # so that the bread acceleration and velocity slows.
    while trajGuessY[-1] >= 0:
        # New velocity equals old velocity minus the updated acceleration
        velocityX = velocityX - accelX*timeStep
        # Change the acceleraion to use the last calculated velocity
        accelX = ((rho*drag*pow(velocityX,2)*pi*pow(radius,2))
                   /(2*mass))
        # New velocity equals old velocity minus the updated acceleration
        velocityY = velocityY - accelY*timeStep
        # Positions equal last position (in the list) + distance moved
        x = trajGuessX[-1] + velocityX*timeStep
        y = trajGuessY[-1] + velocityY*timeStep
        trajGuessX.append(x)    # Append the x-coord to the list
        trajGuessY.append(y)    # Append the y-coord to the list

    # Plot the graphs of the trajectory and the physical environment
    env = plt.plot(physEnvX, physEnvY, 'b', label='Environment')
    traj = plt.plot(trajGuessX, trajGuessY, 'r--', label='Trajectory')
    plt.grid(b=True, which='major', color='k', linestyle='-')
    plt.suptitle('Bread Slingshot') # Set the graph title
    plt.legend(loc='upper right')   # Set the legend location
    plt.ylabel('Height (m)')        # Set the y-axis label
    plt.xlabel('Distance (m)')      # Set the x-axis label
    plt.ylim([-5,50])               # Set the y-axis limits
    plt.xlim([-5,120])              # Set the x-axis limits
    plt.show()                      # Make sure the graph appears

    print 'The bread lands at: {0:.0f}, {1:.0f}'.format(
        trajGuessX[-1], trajGuessY[-1])
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














