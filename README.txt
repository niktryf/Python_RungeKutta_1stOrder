			ODE.py

			i. Description
			ii. Dependencies
			iii. Instructions
			iv. Output

--------------------------------------------------------------------
i. DESCRIPTION:

The code in ODE.py, rungekutta.py and plot1D.py constitutes 
a simple 1st order ODE solver written in Python.

The program essentially solves equations of the following form:

  		(dy/dx) = f(x,y)

The numerical method used is Runge - Kutta 4th order, one of 
the most well-known methods for the numerical solution of such 
differential equations.

--------------------------------------------------------------------
ii. DEPENDENCIES:

   The program uses numpy and matplotlib, two fundamental packages 
   for numerical Python. 

   Installing is straightforward for linux systems, 
   for example in Ubuntu:

   sudo apt-get install python-numpy python-matplotlib

--------------------------------------------------------------------
iii. INSTRUCTIONS:

1. Enter the desired right-hand side function f(x,y) into the 
   rhs function inside rungekutta.py .

2. Enter the desired initial conditions for x and y at the beginning
   of ODE.py (right after the imports).

3. Run the program from the command line in the following format:
   
	$ python ODE.py <timestep> <total time> <output interval>

   For example, running the following:

	$ python ODE.py 0.1 100 10

   will use a time step of 0.1, up to 100 time units and produce 
   output every 10 timesteps (i.e. every 10*0.1 = 1 time units).

---------------------------------------------------------------------
iv. OUTPUT:

   The program outputs the independent variable x and the numerical 
   solution y as columns in the file "RK4_output.txt".

   It also plots the solution using matplotlib. 

