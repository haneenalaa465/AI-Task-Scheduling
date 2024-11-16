# from task import Task
class Problem:
    def __init__(self, tasks, init_state):
        self.tasks = tasks
        self.init_state = init_state
        self.length = len(tasks)
        self.schedule = []
        self.today = 0

    #return dictionary with all tasks w/o dependencies & their costs
    def step_cost(self):
        possible_routes = {}
        for task in (self.tasks):
            if not task.getDependencies():
                cost = max(0, task.getDeadline() - (self.today + task.getDuration()))
                possible_routes[task] = cost
        return possible_routes

    # appends best task to schedule 
    def action(self):
        possible_routes = self.step_cost()
        if not possible_routes:
            return
    
        selected_task = min(possible_routes, key=possible_routes.get)
        self.today += selected_task.getDuration()
        self.schedule.append(selected_task)
        self.tasks.remove(selected_task)
        for task in self.tasks:
            if selected_task.getID() in task.getDependencies():
                deps = task.getDependencies()
                deps.remove(selected_task.getID())
                task.setDependencies(deps)


    # returns schedule    
    def result(self):
        return self.schedule

    def goal_state(self, state=None):
        return len(self.schedule) == self.length and bool(self.schedule)

    # checks whether all tasks have been added
    def actions(self, state=None):
        return list(self.step_cost().keys())