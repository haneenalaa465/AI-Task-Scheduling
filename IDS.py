from task import Task
from node import Node
from problem import Problem
def dls(problem, limit):
    frontier = [Node.root(problem.init_state)]
    result = "failure"
    while frontier:
        node = frontier.pop() #stack
        if problem.goal_state():
            return solution(node)
        if len(node.state) > limit:
            result = "cutoff"
        else:
            for action in problem.actions():
                child = Node.child(problem, node, action)
                frontier.append(child)
    return result

def IDS(problem):
    depth = 0
    while True:
        result = dls(problem, depth)
        if result == "failure":
            return None 
        if result != "cutoff":
            return result
        depth += 1


def mainIDS():
    task1 = Task("A", "Task A", 2, 3, [])
    task2 = Task("B", "Task B", 3, 5, ["A"])
    task3 = Task("C", "Task C", 2, 4, [])
    task4 = Task("D", "Task D", 2, 5, ["A"])
    task5 = Task("E", "Task E", 1, 5, ["B", "D"])
    tasks = [task1, task2, task3, task4, task5]

    init_state = []
    problem = Problem(tasks, init_state)
    while not problem.goal_state():
        problem.action()
    schedule = problem.result()
    print("Final Schedule:")
    total_cost = 0
    completion_time = 0
    for task in schedule:
        completion_time += task.getDuration()
        latency_cost = max(0, completion_time - task.getDeadline())
        total_cost += latency_cost
        print(
            f"ID: {task.getID()} | Description: {task.getDescription()} | "
            f"Duration: {task.getDuration()} | Deadline: {task.getDeadline()} | "
            f"Completion Time: {completion_time} | Latency Cost: {latency_cost}"
        )
    print(f"\nTotal Latency Cost: {total_cost}")


mainIDS()
