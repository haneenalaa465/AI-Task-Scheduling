from task import Task
from problem import Problem
import random
import math

def simulated_annealing(problem, initial_temperature=1000, cooling_rate=0.99, min_temperature=1e-3):
     # initial state (empty schedule) & initial schedule (empty list)
    current_state = problem.init_state 
    current_schedule = problem.schedule 
    # total duration as cost 
    current_cost = 0
    for task in current_schedule:
        current_cost += task.getDuration()
    # initial tem=1000
    temperature = initial_temperature

    while temperature > min_temperature:
        # select a task and add it to the schedule & update the schedule
        problem.action() 
        # updated schedule and cost
        current_schedule = problem.result()
        # update cost
        for task in current_schedule:
            current_cost += task.getDuration()
        # delta = cost difference between new and old schedule
        delta = current_cost - sum(task.getDuration() for task in current_schedule)
        # Accept new schedule with a probability based on temperature
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            pass  #nothing to do because we updated the schedule already
        else:
            # If the new schedule is worse => revert the old one
            problem.schedule = current_schedule  
        
        # Cool down temp
        temperature *= cooling_rate
        # is goal state reached yet?
        if problem.goal_state():
            break

    schedule = problem.result()
    return schedule