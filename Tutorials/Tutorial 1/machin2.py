# file: machin2.py
"""
Sample Python program for MECH2700
Computes and displays an estimate of pi using Machin’s
and a series expansion for the arctangent function.
Check against another estimate obtained via the math library.
P. A. Jacobs
School of Engineering, UQ.
2014-07-08 Python3 compatibility.
"""
import math

#------------------------------------------------------------------

def atan_series(x, n):
    "Computes atan(x) with a truncated series expansion of n terms."
    xpower = x
    my_sum = x
    sign = 1
    for i in range(1,n):
        xpower = xpower * x * x
        sign = -1 * sign
        term = sign * xpower / (2 * i + 1)
        my_sum = my_sum + term
    return my_sum

def machin(n):
    "Computes pi using Machin’s formula."
    return 4 * (4 * atan_series(0.2,n) - atan_series(1.0/239,n))

#---------------------------------------------------------------

print("Begin program Machin2...")
text = input("Enter a value for the number of terms: ")
i = int(text)
pi_1 = machin(i)
print("Truncated series estimate is ", pi_1, " for n=", i)
pi_2 = 4.0 * math.atan(1.0)
print("Math library estimate is ", pi_2)
print("Difference is ", pi_1 - pi_2)
print("End of program Machin2.")
