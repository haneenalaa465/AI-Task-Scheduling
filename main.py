from problem import Problem
from node import Node
from task import Task
from dfs import dfs
from bfs import bfs
from ucs import UCS

def main():
    task1 = Task("A", "Task A", 2, 10, [])
    task2 = Task("B", "Task B", 3, 8, ["A"])
    task3 = Task("C", "Task C", 1, 6, ["A"])
    task4 = Task("D", "Task D", 2, 12, ["B", "C"])
    tasks = [task1, task2, task3, task4]

    problem = Problem(tasks, init_state = task1)
    ucs = UCS(tree=None, init_state=task1, problem=problem)  
    ucs.findPath()

if __name__ == "__main__":
    main()

