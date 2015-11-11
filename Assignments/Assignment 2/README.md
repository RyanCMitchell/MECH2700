MECH2700 Numerical Analysis 1
2015 Semester 2
Assignment 2
Ryan MITCHELL 4185 0178

------------------------------------------------------------------------------

The Python script has been created for ease of use, to make your life as easy
as possible. There are 2 files that contain all of the functions and
computations.

------------------------------------------------------------------------------

Assignment2.py
Contains 2 functions which are:

1 - TransferFunction(w, Vin=5)
    This function calculates the Transfer Function of the Chebyshev
    circuit for a single frequency. The Tranfer Function is an
    independant multiplication factor; regardless of what is selected for Vin, the result will be the same for the same frequency.

2 - Bode(start=10, end=10e7)
    Makes use of TransferFunction to calculate the transfer function for
    a range of frequencies and plots the frequency response both linearly
    and on a semi-log (frequency axis).
    No values are required. The default range is 10Hz to 10MHz and cannot
    be extended but can be narrowed.

These can be called from the command prompt once loaded.
In order to recreate the graphs in the report, run the module. Text will
print once the script has loaded. Once loaded there is only 1 function
required - Bode(start=10, end=10e7). No inputs are required unless the user would like to narrow the frequency range.

At the bottom of the function is where the plotting occurs. Only one plot can
be made at a time and as such either lines 113 or 114 must be commented out.
The function iterates through a large amount of data and takes approx 1 min
to complete.

If you would like to check the Gain (Vout / Vin) for a single frequency, use
Transfer function. This will not display a graph though.

------------------------------------------------------------------------------

gjSolver.py
Contains 2 functions which are:

1 - GaussJordan(A, b)
    Gauss-Jordan Matrix elimination solver with partial pivoting.

    Params:
        A: square (nxn) matrix of coefficients
        B: column vector of RHS values (nx1 matrix)

    Returns:
        x, which is the solution of Ax = b

2 - ConditionNumber(A)
    Assuming that the matrix is non-singular, its condition number can be
    calculated as the scalar of
    ||A||.||A^(-1)||
    The actual value depends on which norm is used, but for this function
    the row-sum norm is used.

    Params:
        A: square (nxn) matrix of coefficients

    Returns:
        norm, as a float

and can be called from the command prompt once loaded.
