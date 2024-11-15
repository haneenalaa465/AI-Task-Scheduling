from problem import Problem
from node import Node
from task import Task
from bfs import BFSScheduler

# BFS trials
task1 = Task(1, "Task 1", 2, 5, [])
task2 = Task(2, "Task 2", 3, 8, [1, 3])
task3 = Task(3, "Task 3", 1, 6, [])  
task4 = Task(4, "Task 4", 2, 10, [3])   

tasks = [task1, task2, task3, task4]
problem = Problem(tasks, init_state=0)

scheduler = BFSScheduler(problem)
scheduler.bfs_tree()
scheduler.print_schedule()
