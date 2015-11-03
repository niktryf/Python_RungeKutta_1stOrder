#############################################################################
### Python ODE solver, using the Runge-Kutta 4th order method
### Solves ordinary differential equations of the form (dy/dx) = f(x,y)
###
### User must input the following parameters:
### 1. Via command line arguments: time step, total time, output interval
### 2. The right-hand side of the differential equation 
###    inside the rhs function, in the rungekutta.py file.
### 3. Initial conditions x_0, y_0 (example: y(x_0) = y_0),
###    at the beginning of the code, right below the imports
###
### Example: python ODE.py 0.1 100 10
### This will solve the ODE with a timestep of dt = 0.1, for 100 time units,
### writing output every 10 time steps.
###
### Output: File "RK4_output.txt", also plots results.
### 
### Author: Nikos Tryfonidis, November 2015
### The MIT License (MIT)
### Copyright (c) 2015 Nikos Tryfonidis
### See LICENSE.txt
#############################################################################

# Import necessary packages
import numpy as np
import sys

# Import runge kutta and right-hand-side function
# from rungekutta.py
from rungekutta import *
from plot1D import *

##### Set Initial Conditions Here: #####
x_0 = 0
y_0 = 1
########################################

#################################################################################
### Command line arguments:
#################################################################################

# Check number of command line arguments
if len(sys.argv) != 4:
	print "Usage: python ODE.py <timestep> <total time> <output interval>"
	print "Please run again following the command line input format above."
	print "Exiting..."
	sys.exit(1)

# Get command line arguments
h = float(sys.argv[1])
totalTime = float(sys.argv[2])
interval = int(sys.argv[3])

#################################################################################

# Calculate number of time steps
totalSteps = totalTime/h
# Find size of output
size = int(totalSteps/interval) + 1

# Print a summary of parameters
print "Running Runge-Kutta with the following parameters:"
print "Time step: %f\tTotal time: %f\t" %(h, totalTime)
print "Output interval: %d" %interval

# Initialize variable arrays:
x = np.linspace(x_0, x_0 + totalTime, size)
y = np.zeros(size)
# Initial y value:
y[0] = y_0

# Call Runge Kutta
xOld = x[0]
yOld = y[0]
for t in xrange(1, size):

    for i in xrange(0, interval):
        xOld = xOld + h
        yOld = RK4(xOld, yOld, h, rhs)
        
    y[t] = yOld


# Save x and y into output file (each array is a column)
np.savetxt('RK4_output.txt', np.c_[x, y], fmt='%.10f')

# Plot x, y (plot1d function in plot1D.py)
plot1D(size, "RK4_output.txt")






