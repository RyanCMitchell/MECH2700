# file: machin1.py
"""
MECH2700: Using Python as a calculator.
Compute and display an estimate of pi using Machin’s formula.
Use only three terms in the arctangent expansions.
Check against another estimate obtained via the math library.
P. A. Jacobs
School of Engineering, UQ.
2014-07-08 Python3 compatibility.
"""
from math import *
print("Begin program Machin1...")
a1 = 1.0 / 5
a2 = pow(a1,3) / 3
a3 = pow(a1,5) / 5
b1 = 1.0 / 239
b2 = pow(b1,3) / 3
b3 = pow(b1,5) / 5
pi_1 = 4 * (4 * (a1 - a2 + a3) - (b1 - b2 + b3))
print("Truncated series estimate is ", pi_1)
pi_2 = 4.0 * atan(1.0)
print("Math library estimate is ", pi_2)
print("Difference is ", pi_1 - pi_2)
print("End of program Machin1.")
