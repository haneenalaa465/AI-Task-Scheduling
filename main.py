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
from ucs import UCS

# task1 = Task(1, "run", 2, 3, [])
# print(task1.getID(), task1.getDescription(), task1.getDuration(), task1.getDeadline(), task1.getDependencies())
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


# task1 = Task(1, "run", 2, 3, [])
# task1.task_vis()
# task2 = Task(2, "walk", 2, 5, [])
# task2.task_vis()
# task3 = Task(3, "crawl", 2, 7, [1])
# task3.task_vis()
