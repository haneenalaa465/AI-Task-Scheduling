from problem import Problem
from node import Node
from task import Task
from dfs import dfs
from bfs import bfs
from ucs import UCS
from hillclimb import hill_climbing
from a_star import a_star
from sa import simulated_annealing

def run_algorithm(problem, algo):
    if algo == "dfs":
        print("\nRunning DFS:")
        return bfs(problem)
    elif algo == "bfs":
        print("\nRunning BFS:")
        return dfs(problem)
    elif algo == "ids":
        print("\nRunning IDS:")
        return ids(problem)
    elif algo == "UCS":
        print("\nRunning BFS:")
        ucs = UCS(tree=None, init_state=0, problem=problem)
        ucs.findPath() 
    elif algo == "greedy":
        print("\nRunning Greedy:")
        return greedy(problem) 
    elif algo == "a_star":
        print("\nRunning A*:")
        return a_star(problem) 
    elif algo == "hillclimb":
        print("\nRunning IDS:")
        return hill_climbing(problem)
    elif algo == "simulated_annealing":
        print("\nRunning Simulated Annealing:")
        return simulated_annealing(problem)
    elif algo == "genetic":
        print("\nRunning Genetic:")
        return genetic(problem)
    else:
        print("404; algorithm not found")
    