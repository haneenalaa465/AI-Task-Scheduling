from problem import Problem
from node import Node
from task import Task
from algorithms import run_algorithm

def main():
    # example 1
    # task1 = Task(1, "Task 1", 2, 5, [2, 3, 5])
    # task2 = Task(2, "Task 2", 3, 8, [])
    # task3 = Task(3, "Task 3", 1, 6, [])
    # task4 = Task(4, "Task 4", 2, 10, [1])
    # task5 = Task(5, "Task 5", 2, 20, [])

    # example 2
    task1 = Task(1, "Task 1", 2, 6, [])  
    task2 = Task(2, "Task 2", 4, 8, [1, 3])  
    task3 = Task(3, "Task 3", 3, 5, [1])  
    task4 = Task(4, "Task 4", 2, 7, [2, 5])  
    task5 = Task(5, "Task 5", 5, 9, [3])

    # Show an algorithms result at a time
    tasks = [task1, task2, task3, task4, task5]
    problem = Problem(tasks, 0)
    # print("\nbfs, dfs, ids, ucs, greedy, a_star, hillclimb, simulated_annealing, genetic\nType 0 to exit")
    print("\nbfs, dfs, ucs, a_star, hillclimb, simulated_annealing")
    algo = input("Select algorithm (type as above):")
    run_algorithm(problem, algo)
    

if __name__ == "__main__":
    main()

