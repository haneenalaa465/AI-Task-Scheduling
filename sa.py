from task import Task
from problem import Problem
import random
import math

def simulated_annealing(problem, initial_temperature=1000, cooling_rate=0.99, min_temperature=1e-3):
    current_state = problem.init_state  # Start with the initial state (empty schedule)
    current_schedule = problem.schedule  # Start with the initial schedule (empty list)
    current_cost = sum(task.getDuration() for task in current_schedule)  # Total duration as cost
    temperature = initial_temperature

    while temperature > min_temperature:
        # Perform an action (select a task and add it to the schedule)
        problem.action()  # Call the original action method (it updates the schedule)
        
        # Get the updated schedule and cost
        current_schedule = problem.result()
        current_cost = sum(task.getDuration() for task in current_schedule)  # Update cost
        
        # Calculate cost difference (delta) between new schedule and old schedule
        delta = current_cost - sum(task.getDuration() for task in current_schedule)

        # Accept new schedule with a probability based on temperature
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            pass  # Accept the new schedule (do nothing since it's already updated)
        else:
            # If the new schedule is worse, revert it
            problem.schedule = current_schedule  # Revert to the old schedule
        
        # Cool down the temperature
        temperature *= cooling_rate

        # Check if goal state is reached (all tasks scheduled)
        if problem.goal_state():
            break

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

# Test case
task1 = Task(1, "Task 1", 2, 6, [])
task2 = Task(2, "Task 2", 4, 8, [1, 3])
task3 = Task(3, "Task 3", 3, 5, [1])
task4 = Task(4, "Task 4", 2, 7, [2, 5])
task5 = Task(5, "Task 5", 5, 9, [3])

tasks = [task1, task2, task3, task4, task5]

init_state = []
problem = Problem(tasks, init_state)

# Run Simulated Annealing to find the best schedule
simulated_annealing(problem)
