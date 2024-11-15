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
        possible_routes = dict()
        for i in range(len(self.tasks)):
            if self.tasks[i].getDependencies() == []:
                cost = self.tasks[i]._deadline - self.tasks[i].getDuration() - self.today
                possible_routes[self.tasks[i]] = cost
        # print("Possible Routes:", {t.getID(): c for t, c in possible_routes.items()})
        return possible_routes

    # appends best task to schedule 
    def action(self):
        possible_routes = self.step_cost()
        if not possible_routes:  
            # print("No tasks available to schedule!")
            return
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
        if len(self.schedule) == self.length:
            return True
        return False
