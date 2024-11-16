from problem import Problem
from node import Node
from task import Task
from dfs import dfs
from bfs import bfs
from ucs import UCS
from hillclimb import hill_climbing
from a_star import a_star
from sa import simulated_annealing
from algorithms import run_algorithm

def main():
    # example 1
    task1 = Task(1, "Task 1", 2, 5, [2, 3, 5])
    task2 = Task(2, "Task 2", 3, 8, [])
    task3 = Task(3, "Task 3", 1, 6, [])
    task4 = Task(4, "Task 4", 2, 10, [1])
    task5 = Task(5, "Task 5", 2, 20, [])

    # example 2
    # task1 = Task(1, "Task 1", 2, 6, [])  
    # task2 = Task(2, "Task 2", 4, 8, [1, 3])  
    # task3 = Task(3, "Task 3", 3, 5, [1])  
    # task4 = Task(4, "Task 4", 2, 7, [2, 5])  
    # task5 = Task(5, "Task 5", 5, 9, [3])

    tasks = [task1, task2, task3, task4, task5]
    problem = Problem(tasks, 0)

    while True:
        print("\nbfs, dfs, ids, ucs, greedy, a_star, hillclimb, simulated_annealing, genetic\nType 0 to exit")
        algo = input("Select algorithm (type as above):")
        if algo == "0":
            break
        schedule = run_algorithm(problem, algo)
        print_schedule(schedule)
    

def print_schedule(schedule):
    if not schedule:
        print("No schedule :(")
        return

    print("Schedule:")
    for task in schedule:
        task.task_vis()  

if __name__ == "__main__":
    main()

