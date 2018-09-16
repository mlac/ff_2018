
from pyomo.environ import *
infinity = float('inf')

model = AbstractModel()

#Players
model.P = Set()

#Expected Scoring
model.S = Set()

#value of each player
model.v = Param(model.P, within=PositiveReals)

#expected Positions for each player
model.e = Param(model.P,model.S, within=NonNegativeReals)

#Lower and upper bound on each Position
model.Smin = Param(model.S, within=NonNegativeIntegers, default = 0)
model.Smax = Param(model.S, within=NonNegativeIntegers, default = 4)

#Cost by player
model.C = Param(model.P, within=PositiveReals)

#Max Cost
model.Cmax = Param(within=PositiveReals)

# Whether player plays
model.x = Var(model.P, within=Binary)

# Minimize the cost of players that are played
def value_rule(model):
    return sum(model.v[i]*model.x[i] for i in model.P)
model.value = Objective(rule=value_rule)

# Limit Positions
def position_rule(model, j):
    value = sum(model.e[i,j]*model.x[i] for i in model.P)
    return model.Smin[j] <= value <= model.Smax[j]
model.positions = Constraint(model.S, rule=position_rule)

# Limit the cost of the Players
def cost_rule(model):
    return sum(model.C[i]*model.x[i] for i in model.P) <= model.Cmax
model.cost = Constraint(rule=cost_rule)



'''
cost over the average
expected points over the average

cost_premium = cost-avg_cost
points_premium = ex_pts - avg_ex_pts

We want a higher points_premium/cost_premium
This could be a useful indicator of a players Value
'''
