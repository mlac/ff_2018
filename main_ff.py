'''
This is a test program to do optimization for daily fantasy football leagues.

We will see how it goes.
'''

from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linprog.html

# Define simple test example from website to test implementation

'''
Minimize: f = -1*x[0] + 4*x[1]

Subject to: -3*x[0] + 1*x[1] <= 6
1*x[0] + 2*x[1] <= 4
x[1] >= -3
where: -inf <= x[0] <= inf
'''

c = [-1,4]
A = [[-3,1],[1,2]]
b = [6,4]
x0_bounds = (None, None)
x1_bounds = (-3, None)

res = linprog(c,A_ub=A, b_ub=b, bounds=(x0_bounds,x1_bounds),
                                        options={"disp":True})

print res


'''

maxmize expected points

subject to constraint that budget is less than 200

budget = sum product of player * salary
expected points = sum product of expected points * players

position constraints

'''

'''

Realized need for integer constraints - installing Pyomo.


'''
