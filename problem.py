class Problem:
    def __init__(self, tasks):
        self.tasks = tasks
        self.schedule = []
        self.today = 0

    def action(self):
        # dictionary of possible tasks w/o dependencies with their costs
        possible_routes = dict()
        for i in range(len(self.tasks)):
            if self.tasks[i].dependcies == []:
                cost = self.tasks[i].deadline - self.tasks[i].duration - self.today
                possible_routes[self.tasks[i]] = cost

        min_task_cost = min(possible_routes, key=possible_routes.get)
        self.today += min_task_cost.get_duration()
        self.schedule.append(min_task_cost)
        
    def result(self):
        return self.schedule
