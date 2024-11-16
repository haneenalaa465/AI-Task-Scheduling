import heapq

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
