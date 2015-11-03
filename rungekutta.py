#############################################################
### Runge-Kutta 4th Order 
###   for differential equations of the form (dy/dx) = (rhs)
###   the rhs function is the right-hand side of the O.D.E.
###  
###   Author: Nikos Tryfonidis
###   The MIT License (MIT)
###   Copyright (c) 2015 Nikos Tryfonidis
###   See LICENSE.txt
#############################################################################


#####################################################
# Right-hand side of differential equation.
# Set desired rhs function here:
#####################################################

def rhs(x, y):
    return -y*y


#####################################################
# Runge Kutta 4th order method
# Returns new y value from old x, y values
#####################################################

def RK4(x_old, y_old, h, function):
    k1 = h*function(x_old, y_old)
    k2 = h*function(x_old + 0.5*h, y_old + 0.5*k1)
    k3 = h*function(x_old + 0.5*h, y_old + 0.5*k2)
    k4 = h*function(x_old + h, y_old + k3)

    return y_old + (1.0/6.0)*(k1 + 2*k2 + 2*k3 + k4)

