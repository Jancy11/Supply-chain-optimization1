import math

def calculate_eoq(demand, ordering_cost, holding_cost):
    return math.sqrt((2 * demand * ordering_cost) / holding_cost)
