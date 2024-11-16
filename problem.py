# from task import Task
class Problem:
    def __init__(self, tasks, init_state):
        self.tasks = tasks
        self.length = len(tasks)
        self.init_state = init_state
        self.schedule = []
        self.today = 0

    #return dictionary with all tasks w/o dependencies & their costs
    def step_cost(self):
        possible_routes = {}
        for task in (self.tasks):
            if not task.getDependencies() and task not in self.schedule:
                cost = task.getDeadline() - task.getDuration() - self.today
                possible_routes[task] = cost
        return possible_routes

    # appends best task to schedule 
    def action(self):
        possible_routes = self.step_cost()
        min_task_cost = min(possible_routes, key=possible_routes.get)
        self.today += min_task_cost.getDuration()
        self.schedule.append(min_task_cost)
        # print(f"Scheduled task {min_task_cost.getID()} at day {self.today}")

        for task in self.tasks:
            if min_task_cost.getID() in task.getDependencies():
                updated_deps = task.getDependencies()
                updated_deps.remove(min_task_cost.getID())  
                task.setDependencies(updated_deps)
                # print(f"Updated dependencies for task {task.getID()}: {updated_deps}")


    # returns schedule    
    def result(self):
        return self.schedule

    # checks whether all tasks have been added
    def goal_state(self):
        if len(self.schedule) == self.length and self.schedule:
            return True
        return False
