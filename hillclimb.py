from node import Node

def hill_climbing(problem):

    while not problem.goal_state():
        neighbors = problem.step_cost()
        if not neighbors:
            break

        problem.action()

    schedule = problem.result()
    print_schedule(schedule)
    return schedule

def print_schedule(schedule):
    if not schedule:
        print("No schedule :(")
        return

    print("Schedule:")
    for task in schedule:
        task.task_vis()  