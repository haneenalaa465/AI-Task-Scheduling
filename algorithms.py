from problem import Problem
from node import Node
from task import Task
from dfs import dfs
from bfs import bfs
from ucs import UCS
from hillclimb import hill_climbing
from a_star import a_star
from sa import simulated_annealing
import time, copy

def run_algorithm(problem, algo):
    if algo == "dfs":
        print("\nRunning DFS:")
        print_schedule(dfs(problem))
    elif algo == "bfs":
        print("\nRunning BFS:")
        print_schedule(bfs(problem))
    elif algo == "ids":
        print("\nRunning IDS:")
        print_schedule(ids(problem))
    elif algo == "ucs":
        print("\nRunning UCS:")
        ucs = UCS(tree=None, init_state=0, problem=problem)
        ucs.findPath() 
    elif algo == "greedy":
        print("\nRunning Greedy:")
        print_schedule(greedy(problem))
    elif algo == "a_star":
        print("\nRunning A*:")
        print_schedule(a_star(problem)) 
    elif algo == "hillclimb":
        print("\nRunning IDS:")
        print_schedule(hill_climbing(problem))
    elif algo == "simulated_annealing":
        print("\nRunning Simulated Annealing:")
        print_schedule(simulated_annealing(problem))
    elif algo == "genetic":
        print("\nRunning Genetic:")
        print_schedule(genetic(problem))
    else:
        print("404; algorithm not found")
    

algos = ["bfs", "dfs", "ids", "ucs", "greedy", "a_star", "hillclimb", "simulated_annealing", "genetic"]
algos = ["bfs", "dfs", "ucs", "a_star", "hillclimb", "simulated_annealing"]
def comparison(problem):
    og_prob = copy.deepcopy(problem)
    for algo in algos:
        prob = copy.deepcopy(og_prob)
        print(f"\nTesting {algos}:")
        t0 = time.time()
        run_algorithm(prob, algos)
        t1 = time.time()
        print("Time taken:", t1-t0)
        print("=====================================================================================================")


def print_schedule(schedule):
    if not schedule:
        print("No schedule :(")
        return

    print("Schedule:")
    for task in schedule:
        task.task_vis()  