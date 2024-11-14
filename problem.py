from task import Task

class Problem:
    def __init__(self, tasks):
        self.tasks = tasks
        self.schedule = []
        self.today = 0

    # return dictionary with all tasks w/o dependencies & their costs
    def step_cost(self):
        possible_routes = dict()
        for i in range(len(self.tasks)):
            if self.tasks[i].dependcies == []:
                cost = self.tasks[i].deadline - self.tasks[i].duration - self.today
                possible_routes[self.tasks[i]] = cost
        return possible_routes

    # appends best task to schedule 
    def action(self):
        possible_routes = self.step_cost()
        min_task_cost = min(possible_routes, key=possible_routes.get)
        self.today += min_task_cost.get_duration()
        self.schedule.append(min_task_cost)
        for task in self.tasks:
            if min_task_cost.getID() in task.getDependencies():
                deps = task.getDependencies().remove(min_task_cost.getID())
                task.setDependencies(deps)


    # returns schedule    
    def result(self):
        return self.schedule

    # checks whether all tasks have been added
    def goal_state(self):
        if len(self.schedule) == len(self.tasks):
            return True
        return False

