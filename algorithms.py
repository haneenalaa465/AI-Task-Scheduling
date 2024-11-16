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
    def run_with_memory_tracking(func):
        t0 = time.time()
        mem_usage, result = memory_usage((func,), retval=True, max_usage=True)
        t1 = time.time()
        return t1 - t0, mem_usage, result

    if algo == "dfs":
        print("\nRunning DFS:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: dfs(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "bfs":
        print("\nRunning BFS:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: bfs(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "ids":
        print("\nRunning IDS:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: ids(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "ucs":
        print("\nRunning UCS:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: UCS(tree=None, init_state=0, problem=problem).findPath())
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "greedy":
        print("\nRunning Greedy:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: greedy(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "a_star":
        print("\nRunning A*:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: a_star(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "hillclimb":
        print("\nRunning Hill Climb:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: hill_climbing(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "simulated_annealing":
        print("\nRunning Simulated Annealing:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: simulated_annealing(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    elif algo == "genetic":
        print("\nRunning Genetic:")
        time_elapsed, max_memory, schedule = run_with_memory_tracking(lambda: genetic(problem))
        print_schedule(schedule)
        print("Time:", time_elapsed, "sec")
        print("Memory:", max_memory, "MB")

    else:
        print("404 - algorithm not found")


def print_schedule(schedule):
    if not schedule:
        print("No schedule :(")
        return

    print("Schedule:")
    for task in schedule:
        task.task_vis()
