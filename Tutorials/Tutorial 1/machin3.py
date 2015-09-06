# file: machin3.py
"""
Python program for MECH2700
Computes and displays an estimate of pi using Machin’s Formula
and an alternate formula.
R. C. Mitchell
2015-08-16
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
    "Computes pi using Machin's formula."
    return 4 * (4 * atan_series(0.2,n) - atan_series(1.0/239,n))

def machin_alt(n):
    "Computes pi using Machin's formula."
    return 4 * (4 * atan_series(0.1,n) - atan_series(1.0/239,n))


def machin_error():
    "Computes the error between pi and Machin's Formula"
    print("Begin program machin_error")
    for i in [3,5,7,9,11,13,15]:
        error = math.fabs(machin(i) - math.pi)
        print("Term number: ", i, ". Error is: ", error)
    return


def machin_error_alt():
    "Computes the error between pi and an alternate Machin's Formula"
    print("Begin program machin_error_alt")
    for i in [3,5,7,9,11,13,15]:
        error = math.fabs(machin_alt(i) - math.pi)
        print("Term number ", i, ". Error is: ", error)
    return
#---------------------------------------------------------------

machin_error()
print("machin_error program complete...")

#machin_error_alt()
#print("machin_error_alt program complete...")
