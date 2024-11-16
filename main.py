from problem import Problem
from node import Node
from task import Task
from ucs import UCS
from IDS import IDS


# task1 = Task(1, "run", 2, 3, [])
# print(task1.getID(), task1.getDescription(), task1.getDuration(), task1.getDeadline(), task1.getDependencies())
def main():
    task1 = Task("A", "Task A", 2, 10, [])
    task2 = Task("B", "Task B", 3, 8, ["A"])
    task3 = Task("C", "Task C", 1, 6, ["A"])
    task4 = Task("D", "Task D", 2, 12, ["B", "C"])
    tasks = [task1, task2, task3, task4]

    # problem = Problem(tasks, init_state = task1)
    # ucs = UCS(tree=None, init_state=task1, problem=problem)  
    # ucs.findPath()

    init_state = []
    problem = Problem(tasks, init_state)
    actions, cost = IDS(problem)
    print(f"Optimal Schedule: {actions}, Total Cost: {cost}")
    

if __name__ == "__main__":
    main()


# task1 = Task(1, "run", 2, 3, [])
# task1.task_vis()
# task2 = Task(2, "walk", 2, 5, [])
# task2.task_vis()
# task3 = Task(3, "crawl", 2, 7, [1])
# task3.task_vis()
