from pulp import LpMaximize, LpProblem, LpVariable

def optimize_resources():
    model = LpProblem(name="resource-allocation", sense=LpMaximize)

    # Decision variables
    x1 = LpVariable(name="Resource_1", lowBound=0)
    x2 = LpVariable(name="Resource_2", lowBound=0)

    model += 20 * x1 + 30 * x2, "Total Profit"

    model += 2 * x1 + 4 * x2 <= 100, "Material Constraint"
    model += x1 + x2 <= 40, "Labor Constraint"

    status = model.solve()
    return {
        "status": model.status,
        "Resource_1": x1.value(),
        "Resource_2": x2.value(),
        "Total_Profit": model.objective.value()
    }
