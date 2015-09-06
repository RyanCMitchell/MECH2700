# cantilever.py

x = [ 50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0]
dx = [ 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
v = [ 16.7, 53.3, 105.7, 174.0, 227.0, 281.3, 344.3, 388.3]
dv = [ 2.0, 4.6, 7.1, 9.7, 12.3, 14.9, 17.4, 20.0]

from pylab import *

def theoretical_v(x_mm):
    """
    Compute cantilever deflection for a fixed load.
    Input: x_mm : position from fixed-end, in mm
    Returns: v : deflection in hundredths of a mm
    """
    P = 1.96        # load, Newtons
    a = 200.0e-3    # position of load, metres
    E = 70.0e9      # Pascals
    I = 45.0e-12    # metres**2
    x = x_mm / 1000.0
    if x < a:
        v = P * x**2 / (6*E*I) * (3*a - x)
    else:
        v = P * a**2 / (6*E*I) * (3*x - a)
    return v * 1.0e5

# Build up a list of theoretical deflections
tx = []; tv = []

for position in arange(0.0, 400.0, 10.0):
    tx.append(position)
    tv.append(theoretical_v(position))

# Now, make the plot using the pylab functions...
# ...
l1 = plot(x, v, 'b--')
suptitle('Cantilever Deflection: Experiment Compared With Theory')
errorbar(x, v, xerr=dx, yerr=dv,)
hold(True)
l2 = plot(tx, tv, 'r')
#legend((l1, l2), ('Experimental', 'Theory'), 'lower right')

#grid(b=True, which='major', color='k', linestyle='-')
show()
    
