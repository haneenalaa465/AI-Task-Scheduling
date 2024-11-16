import heapq
from task import Task
from problem import Problem

class GreedyBestFirstSearch:
    def __init__(self, problem):
        self.problem = problem
        self.schedule = []
        self.current_time = 0

    def heuristic(self, task):
        return task.getDeadline() - (self.current_time + task.getDuration())

    def search(self):
        frontier = []
        visited = set()
        for task in self.problem.tasks:
            if not task.getDependencies():
                heapq.heappush(frontier, (self.heuristic(task), task))
        while frontier:
            _, task = heapq.heappop(frontier)
            if task in visited:
                continue 
            visited.add(task)
            self.schedule.append(task)
            self.current_time += task.getDuration()
            for next_task in self.problem.tasks:
                if task.getID() in next_task.getDependencies():
                    next_task.getDependencies().remove(task.getID())
                    if not next_task.getDependencies() and next_task not in visited:
                        heapq.heappush(frontier, (self.heuristic(next_task), next_task))
        return self.schedule
    
    
def mainGreedy(problem):
    # task1 = Task("A", "Task A", 2, 3, [])
    # task2 = Task("B", "Task B", 3, 5, ["A"])
    # task3 = Task("C", "Task C", 2, 4, [])
    # task4 = Task("D", "Task D", 2, 5, ["A"])
    # task5 = Task("E", "Task E", 1, 5, ["B", "D"])
    # tasks = [task1, task2, task3, task4, task5]

    # init_state = []
    # problem = Problem(tasks, init_state)

    gbfs = GreedyBestFirstSearch(problem)
    schedule = gbfs.search()
    return schedule

#     print("Final Schedule:")
#     total_cost = 0
#     completion_time = 0

#     for task in schedule:
#         completion_time += task.getDuration()
#         latency_cost = max(0, completion_time - task.getDeadline())
#         total_cost += latency_cost

#         print(
#             f"ID: {task.getID()} | Description: {task.getDescription()} | "
#             f"Duration: {task.getDuration()} | Deadline: {task.getDeadline()} | "
#             f"Completion Time: {completion_time} | Latency Cost: {latency_cost}"
#         )

#     print(f"\nTotal Latency Cost: {total_cost}")


# mainGreedy()
