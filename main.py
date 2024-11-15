from problem import Problem
from node import Node
from task import Task
from bfs import bfs_scheduler, print_schedule
from ucs import UCS

def main():
    task1 = Task(1, "Task 1", 2, 5, [2, 3, 5])
    task2 = Task(2, "Task 2", 3, 8, [])
    task3 = Task(3, "Task 3", 1, 6, [])
    task4 = Task(4, "Task 4", 2, 10, [1])
    task5 = Task(5, "Task 5", 2, 20, [])

    tasks = [task1, task2, task3, task4, task5]

    problem = Problem(tasks, init_state=0)

    # BFS Trials
    print("\nRunning BFS Scheduler:")
    optimal_schedule_bfs = bfs_scheduler(problem)  
    print_schedule(optimal_schedule_bfs)  
    # UCS Trials
    print("\nRunning UCS Scheduler:")
    ucs = UCS(tree=None, init_state=0, problem=problem)
    ucs.findPath()  

if __name__ == "__main__":
    main()
