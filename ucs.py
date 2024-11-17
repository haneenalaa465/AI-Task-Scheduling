import queue  # enqueue -> q.put() / dequeue -> get()
from problem import Problem

class UCS:
    def __init__(self, tree, init_state, problem):
        self.frontier = queue.PriorityQueue()  # the frontier's data str is a priority queue
        self.tree = tree
        self.init_state = init_state 
        self.min_Path_cost = {}
        self.problem = problem  # Problem inst

    def findPath(self):
        initial_task = self.problem.tasks[self.init_state]  
        self.frontier.put((0, initial_task.getID(), initial_task))  #begin with init task and cost=0
        self.min_Path_cost[initial_task.getID()] = 0

        while not self.frontier.empty():
            current_cost, taskID, current_task = self.frontier.get()
            
            # this is already scheduled so I will skip it --> continue
            if current_task in self.problem.schedule:
                continue  

            self.problem.schedule.append(current_task)
            # check if all tasks are done
            if len(self.problem.schedule) == len(self.problem.tasks):
                break

            # check if we reached the goal
            # if self.problem.goal_state():
            #     break

            # possible_routes = self.problem.step_cost()

            for t, t_cost in self.getStepCost(current_task).items():
                total_cost = current_cost + t_cost
                if total_cost < self.min_Path_cost.get(t.getID(), float('inf')):
                    self.min_Path_cost[t.getID()] = total_cost
                    # after updating, add the t and cost to the frontier
                    self.frontier.put((total_cost, t.getID(), t))  

        self.printSchedule()

    def getStepCost(self, current_task):
            routes = {}
            for task in self.problem.tasks:
                #skip the already scheduled
                if task in self.problem.schedule:
                    continue
                # dependencies check 
                if all(dep in [t.getID() for t in self.problem.schedule] for dep in task.getDependencies()):
                    routes[task] = task.getDuration()  
            return routes

    def printSchedule(self):
        print("Optimal Schedule:")
        print("-" * 80)
        print(f"{'Task ID':<8}{'Description':<20}{'Duration':<10}{'Deadline':<10}{'Dependencies':<20}{'Total Cost'}")
        print("-" * 80)

        for task in self.problem.schedule:
            task_id = task.getID()
            description = task.getDescription()
            duration = task.getDuration()
            deadline = task.getDeadline()
            dependencies = ", ".join(map(str, task.getDependencies()))
            cost = self.min_Path_cost.get(task_id, "N/A")
            
            print(f"{task_id:<8}{description:<20}{duration:<10}{deadline:<10}{dependencies:<20}{cost}")

        print("-" * 80)
        print(f"Minimum Path Cost: {self.min_Path_cost}")