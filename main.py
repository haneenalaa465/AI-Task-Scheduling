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
    # task1 = Task(1, "Task 1", 2, 6, [])  
    # task2 = Task(2, "Task 2", 4, 8, [1, 3])  
    # task3 = Task(3, "Task 3", 3, 5, [1])  
    # task4 = Task(4, "Task 4", 2, 7, [2, 5])  
    # task5 = Task(5, "Task 5", 5, 9, [3])

    # example 3
    # task1 = Task("A", "Task A", 2, 3, [])
    # task2 = Task("B", "Task B", 3, 5, ["A"])
    # task3 = Task("C", "Task C", 2, 4, [])
    # task4 = Task("D", "Task D", 2, 5, ["A"])
    # task5 = Task("E", "Task E", 1, 5, ["B", "D"])
    # tasks = [task1, task2, task3, task4, task5]

    tasks = [
    Task(1, "Design System Architecture", 2, 3, []),
    Task(2, "Develop Backend Services", 4, 6, [1]),
    Task(3, "Set Up Database Infrastructure", 3, 5, [1]),
    Task(4, "Design Frontend Wireframes", 2, 4, [1]),
    Task(5, "Implement User Authentication", 2, 6, [2, 3]),
    Task(6, "Integrate Backend with Database", 2, 7, [3]),
    Task(7, "Build Frontend Components", 3, 8, [4, 5]),
    Task(8, "Perform API Testing", 2, 9, [6, 7]),
    Task(9, "Prepare Technical Documentation", 2, 10, [5]),
    Task(10, "Security Testing", 3, 11, [8, 9])
]

    # show one algorithm result at a time
    problem = Problem(tasks, 0)
    print("\nbfs, dfs, ids, ucs, greedy, a_star, hillclimb, simulated_annealing, genetic")
    algo = input("Select algorithm (type as above):")
    run_algorithm(problem, algo)
    
if __name__ == "__main__":
    main()

