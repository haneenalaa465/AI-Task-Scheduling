from problem import Problem
from node import Node
from task import Task

task1 = Task(1, "run", 2, 3, [])
task1.task_vis()
task2 = Task(2, "walk", 2, 5, [])
task2.task_vis()
task3 = Task(3, "crawl", 2, 7, [1])
task3.task_vis()
