from problem import Problem
from node import Node
from task import Task
from dfs import dfs
from bfs import bfs
from ucs import UCS
from hillclimb import hill_climbing
from a_star import a_star
from sa import simulated_annealing
import time
from memory_profiler import memory_usage

def run_algorithm(problem, algo, timing=False):
    if algo == "dfs":
        print("\nRunning DFS:")
        mem_usage = memory_usage(dfs(problem))
        t0 = time.time()
        print_schedule(dfs(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "bfs":
        print("\nRunning BFS:")
        mem_usage = memory_usage(bfs(problem))
        t0 = time.time()
        print_schedule(bfs(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "ids":
        print("\nRunning IDS:")
        mem_usage = memory_usage(ids(problem))
        t0 = time.time()
        print_schedule(ids(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "ucs":
        print("\nRunning UCS:")
        mem_usage = memory_usage(ucs(problem))
        t0 = time.time()
        ucs = UCS(tree=None, init_state=0, problem=problem)
        ucs.findPath() 
        mem_usage = memory_usage(ucs(problem))
        t0 = time.time()

    elif algo == "greedy":
        print("\nRunning Greedy:")
        print_schedule(greedy(problem))
        mem_usage = memory_usage(greedy(problem))
        t0 = time.time()
        print_schedule(greedy(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "a_star":
        print("\nRunning A*:")
        mem_usage = memory_usage(a_star(problem))
        t0 = time.time()
        print_schedule(a_star(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "hillclimb":
        print("\nRunning Hill Climb:")
        mem_usage = memory_usage(hill_climbing(problem))
        t0 = time.time()
        print_schedule(hill_climbing(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "simulated_annealing":
        print("\nRunning Simulated Annealing:")
        mem_usage = memory_usage(simulated_annealing(problem))
        t0 = time.time()
        print_schedule(simulated_annealing(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    elif algo == "genetic":
        print("\nRunning Genetic:")
        mem_usage = memory_usage(ids(problem))
        t0 = time.time()
        print_schedule(ids(problem))
        t1 = time.time()
        print("Time:", t1-t0)
        print("Memory:", max(mem_usage))

    else:
        print("404 - algorithm not found")
    


def print_schedule(schedule):
    if not schedule:
        print("No schedule :(")
        return

    print("Schedule:")
    for task in schedule:
        task.task_vis()  