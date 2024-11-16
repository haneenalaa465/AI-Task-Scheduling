from node import Node

def hill_climbing(problem):

    while not problem.goal_state():
        neighbors = problem.step_cost()
        if not neighbors:
            break

        problem.action()

    schedule = problem.result()
    return schedule
