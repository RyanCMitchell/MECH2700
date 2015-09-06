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

def guess(velocity, thetaDeg, timeStep=0.01):
    """
    Initial calcultaion / integration of the function using guessed
    initial conditions. The function will also be plotted to help
    visualise the scenario.
    velocity in meters per second, theta in degrees, timeStep in
    seconds. The smaller the timeStep the more accurate the function.
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
    while trajGuessY[-1] > 0:
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

    print 'The bread lands at: {0:.3f}, {1:.3f}'.format(
        trajGuessX[-1], trajGuessY[-1])
    return


def noDrag(velocity, thetaDeg, timeStep=0.001):
    """
    Initial calcultaion / integration of the function using guessed
    initial conditions. The function will also be plotted to help
    visualise the scenario. This function does not include any drag
    coefficients and as such is a simplified version of the 'guess'
    function.
    
    velocity in meters per second, theta in degrees and timeStep in
    seconds. The smaller the timeStep the more accurate the function.
    """
    # Calculate / fill all the variables
    theta = radians(thetaDeg)       # Change the input angle into radians
    trajNoDragX = []                # Create an empty list
    trajNoDragX.append(trajXY[0])   # Initialise the list
    trajNoDragY = []                # Create an empty list
    trajNoDragY.append(trajXY[1])   # Initialise the list
    accelX = 0                      # No drag in the x-direction
    accelY = grav                   # Assign gravity to y-acceleration
    velocityX = velocity*cos(theta) # Calculate the x-velocity component
    velocityY = velocity*sin(theta) # Calculate the y-velocity component

    # Execute the mathematics and build a list of the coordinates.
    # While the bread is in the air perform calculations.
    # As it steps through it updates the velocities and accelerations
    # so that the bread acceleration and velocity slows.
    # This function does not include any x-accelerations due to zero drag
    while trajNoDragY[-1] > 0:
        # New velocity equals old velocity minus the updated acceleration
        velocityY = velocityY - accelY*timeStep
        # Positions equal last position (in the list) + distance moved
        x = trajNoDragX[-1] + velocityX*timeStep
        y = trajNoDragY[-1] + velocityY*timeStep
        trajNoDragX.append(x)    # Append the x-coord to the list
        trajNoDragY.append(y)    # Append the y-coord to the list

    # Plot the graphs of the trajectory and the physical environment
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

    print 'The bread lands at: {0:.3f}, {1:.3f}'.format(
        trajNoDragX[-1], trajNoDragY[-1])
    
    return


def optimal(timeStep=0.1):
    """
    Opimisation calculation for the initial launch velocity and angle.
    The optimal solution will achieve the perfect trajectory angle for
    the smallest possible velocity. This is due to the physical strength
    limitations of the students' system. This solution includes drag.
    """
    # Calculate / fill all the variables
    trajOptimalX = []               # Create an empty list
    trajOptimalY = []               # Create an empty list

    # Nested for-loops that will cycle through every angle per 1m/s step
    # in velocity. This will allow the minimun velocity to be used and
    # find the first angle that will achieve this.
    for velocity in range(0,51):    # Loop through m/s values 0 - 50
        print 'Testing velocity {0:.0f}'.format(velocity)
        for thetaDeg in range(0,90):   # Loop through degree values 0 - 89
            #print 'Testing theta {0:.0f}'.format(thetaDeg)


            trajOptimalX[:] = []            # Empty list on each pass
            trajOptimalY[:] = []            # Empty list on each pass
            trajOptimalX.append(trajXY[0])  # Re-initialise the list
            trajOptimalY.append(trajXY[1])  # Re-initialise the list

            theta = radians(thetaDeg)       # Change the angle into radians
            accelX = ((rho*drag*pow((velocity*cos(theta)),2)*pi*pow(
                radius,2))/(2*mass))        # Calculate the x-accel
            accelY = grav                   # Assign gravity to y-accel
            velocityX = velocity*cos(theta) # Calculate the x-vel component
            velocityY = velocity*sin(theta) # Calculate the y-vel component

            # looking for clearance at (84,9)
    
            # Execute the mathematics and build a list of the coordinates.
            # While the bread is in the air perform calculations.
            # As it steps through it updates the velocities and
            # accelerations so that the bread acceleration and velocity
            # slows.
            while trajOptimalY[-1] > 0:

                # As soon as we find a solution finish off the
                # calculations, plot the graph and return
                if trajOptimalX[-1] > 84 and trajOptimalY[-1] > 9:
                    print 'Whithin firing range, finalising cordinates...'
                    while trajOptimalY[-1] >= 1:
                        # New velocity equals old velocity minus the
                        # updated acceleration
                        velocityX = velocityX - accelX*timeStep
                        # Change the acceleraion to use the last calculated
                        # velocity
                        accelX = ((rho*drag*pow(velocityX,2)*pi*
                                   pow(radius,2))/(2*mass))
                        # New velocity equals old velocity minus the
                        # updated acceleration
                        velocityY = velocityY - accelY*timeStep
                        # Positions equal last position (in the list) +
                        # distance moved
                        x = trajOptimalX[-1] + velocityX*timeStep
                        y = trajOptimalY[-1] + velocityY*timeStep
                        trajOptimalX.append(x)    # Append x-coord to list
                        trajOptimalY.append(y)    # Append y-coord to list
                    
                    # Plot the graphs of the trajectory and the physical
                    # environment
                    env = plt.plot(physEnvX, physEnvY, 'b',
                                   label='Environment')
                    traj = plt.plot(trajOptimalX, trajOptimalY,
                                    'r--', label='Trajectory')
                    plt.grid(b=True, which='major', color='k',
                             linestyle='-')
                    # Set the graph title
                    plt.suptitle('Bread Slingshot - Optimal')
                    plt.legend(loc='upper right')   # Set legend location
                    plt.ylabel('Height (m)')        # Set the y-axis label
                    plt.xlabel('Distance (m)')      # Set the x-axis label
                    plt.ylim([-5,50])               # Set the y-axis limits
                    plt.xlim([-5,120])              # Set the x-axis limits
                    plt.show()                      # Make the graph appear

                    print 'The bread lands at: {0:.3f}, {1:.3f}'.format(
                        trajOptimalX[-1], trajOptimalY[-1])
                    print 'The optimal shooting solution is {0:.0f}m/s '\
                          '({1:.2f}km/h) and {2:.0f} degrees'\
                          .format(velocity, velocity*3.6, degrees(theta))
                    return                   
                
                # New velocity equals old velocity minus the updated
                # acceleration
                velocityX = velocityX - accelX*timeStep
                # Change the acceleraion to use the last calculated
                # velocity
                accelX = ((rho*drag*pow(velocityX,2)*pi*pow(radius,2))
                           /(2*mass))
                # New velocity equals old velocity minus the updated
                # acceleration
                velocityY = velocityY - accelY*timeStep
                # Positions equal last position (in the list) + distance
                # moved
                x = trajOptimalX[-1] + velocityX*timeStep
                y = trajOptimalY[-1] + velocityY*timeStep
                trajOptimalX.append(x)    # Append the x-coord to the list
                trajOptimalY.append(y)    # Append the y-coord to the list

    print 'A solution was not found'    
    return


print("Functions locked, loaded and ready for firing!")














