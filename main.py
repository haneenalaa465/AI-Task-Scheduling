from problem import Problem
from node import Node
from task import Task
from dfs import dfs
from bfs import bfs, print_schedule
from ucs import UCS
from hillclimb import hill_climbing
from a_star import a_star

def main():
    task1 = Task(1, "Task 1", 2, 5, [2, 3, 5])
    task2 = Task(2, "Task 2", 3, 8, [])
    task3 = Task(3, "Task 3", 1, 6, [])
    task4 = Task(4, "Task 4", 2, 10, [1])
    task5 = Task(5, "Task 5", 2, 20, [])

    # task1 = Task(1, "Task 1", 2, 6, [])  
    # task2 = Task(2, "Task 2", 4, 8, [1, 3])  
    # task3 = Task(3, "Task 3", 3, 5, [1])  
    # task4 = Task(4, "Task 4", 2, 7, [2, 5])  
    # task5 = Task(5, "Task 5", 5, 9, [3])

    tasks = [task1, task2, task3, task4, task5]

    problem = Problem(tasks, init_state=0)

    # BFS Trials
    print("\nRunning BFS:")
    bfs(problem)  

    # # Run the DFS scheduler
    # print("\nRunning DFS Scheduler:")
    # schedule = dfs(problem)
    # print_schedule(schedule)

    # # UCS Trials
    # print("\nRunning UCS Scheduler:")
    # ucs = UCS(tree=None, init_state=0, problem=problem)
    # ucs.findPath()  

    # # a* trials
    # print("\nRunning A*:")
    # a_star(problem)

    # hill_climb_trials
    # print("\nRunning hill climb:")
    # hill_climbing(problem)




if __name__ == "__main__":
    main()

