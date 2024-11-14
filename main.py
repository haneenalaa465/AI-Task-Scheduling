from problem import Problem
from node import Node
from task import Task

task1 = Task(1, "run", 2, 3, [])
print(task1.getID(), task1.getDescription(), task1.getDuration(), task1.getDeadline(), task1.getDependencies())