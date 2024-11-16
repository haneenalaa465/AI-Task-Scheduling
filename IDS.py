from task import Task
from node import Node
from problem import Problem

node_obj = Node

def dls(problem, limit):
    frontier = [Node.root(problem.init_state)]
    result = "failure"
    while frontier:
        node = frontier.pop() #stack
        if problem.goal_state():
            return node_obj.solution(node)
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


def mainIDS(problem):
    while not problem.goal_state():
        problem.action()
    schedule = problem.result()
    # print("Final Schedule:")
    # total_cost = 0
    # completion_time = 0
    # for task in schedule:
    #     completion_time += task.getDuration()
    #     latency_cost = max(0, completion_time - task.getDeadline())
    #     total_cost += latency_cost
    #     print(
    #         f"ID: {task.getID()} | Description: {task.getDescription()} | "
    #         f"Duration: {task.getDuration()} | Deadline: {task.getDeadline()} | "
    #         f"Completion Time: {completion_time} | Latency Cost: {latency_cost}"
    #     )
    # print(f"\nTotal Latency Cost: {total_cost}")
    return schedule
