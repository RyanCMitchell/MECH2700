# file: tutorial2.py
"""
Python program for MECH2700
All the functions required to complete tutorial 2.
Various iterative methods as well as some straight forward
math equations.
R. C. Mitchell
2015-08-16
"""

from math import *
from pylab import *

#------------------------------------------------------------------

def cube(N):
    g = 1.0
    N = float(N)
    c = 0
    while abs(g*g*g - N) >= 0.01:
        g = ((N/(g*g)) +2*g)/3
        print("N: ",N, " & g: ", g)
        c += 1
    return c

def Rcube(N):
    g = 1.0
    N = float(N)
    c = 0
    while abs(g - N) >= 0.01:
        g = ((N/g*g) +2*g)/3
        print("N: ",N, " & g: ", g)
        c += 1
    return c

def Newton_cube(N):
    g = 1.0
    N = float(N)
    c = 0
    while abs(g*g*g - N) > 0.01:
        g = g - ((g*g*g - N) / (3*g*g))
        print("N: ",N, " & g: ", g)
        c += 1
    return c

def parallax_dist(alpha, beta, c):
    alpha = float(alpha)
    beta = float(beta)
    c = float (c)
    h = c * (sin(radians(alpha)) * sin(radians(beta))) / (
        sin(radians(alpha + beta)))
    #print float("%.4f" %h)
    return h

#------------------------------------------------------------------

# Matplotlib section
x_vals = [] # empty list for x values
y_vals = [] # empty list for y values
y_error = [] # empty list for y-error values

def atan_series(x, n):
    """Computes atan(x) with a truncated series expansion of n terms.
    Runs in the background allowing the machin function to execute."""
    xpower = x
    my_sum = x
    sign = 1
    
    for i in range(1, n):
        xpower = xpower * x * x
        sign = -1 * sign
        term = sign * xpower / (2 * i + 1)
        my_sum = my_sum + term
        
    #print("Pi is: ", my_sum)
    return my_sum

def machin(n):
    """Computes pi using Machin's formula. Utilises atan_series."""
    pi = 4 * (4 * atan_series(0.2,n) - atan_series(1.0/239,n))
    return pi

def machin_error(n):
    "Computes the error between pi and Machin's Formula"
    #print("Begin program machin_error")

    for i in range(1, n):
        error = fabs(machin(n) - pi)
        y_error.append(error)
    return error



if __name__ == "__main__":

    print("Begin program...")
    text = input("Enter a value for the number of terms: ")
    z = int(text)
    machin_error(z+1)
    machin(z+1)
    
    for i in range(1, z+1):
        pi = machin(i)
        x_vals.append(i)
        y_vals.append(pi)
    
    semilogy(y_error, '+-', y_vals, 'r--')
    grid(b=True, which='major', color='k', linestyle='-')
    show()
    

 













