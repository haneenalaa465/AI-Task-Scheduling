import queue  # q.put() / get()
from problem import Problem

class UCS:
    def __init__(self, tree, init_state, problem):
        self.frontier = queue.PriorityQueue()  # the frontier's data str is a priority queue
        self.tree = tree
        self.init_state = init_state 
        self.min_Path_cost = {}
        self.problem = problem  # instance of Problem

    def findPath(self):
        initial_task = self.problem.tasks[self.init_state]  
        self.frontier.put((0, initial_task.getID(), initial_task))  # Start with the initial task and 0 cost
        self.min_Path_cost[initial_task.getID()] = 0

        while not self.frontier.empty():
            current_cost, taskID, current_task = self.frontier.get()

            if current_task in self.problem.schedule:
                continue  # this is already scheduled so I will skip it --> continue

            # check if we have reached the goal
            if self.problem.goal_state():
                break

            possible_routes = self.problem.step_cost()

            for t, t_cost in possible_routes.items():
                total_cost = current_cost + t_cost
                if total_cost < self.min_Path_cost.get(t.getID(), float('inf')):
                    self.min_Path_cost[t.getID()] = total_cost
                    # after updating, add the t and cost to both the front. and to the final schedule
                    self.frontier.put((total_cost, t.getID(), t))  
                    self.problem.schedule.append(t)  

            self.problem.action()

        self.print_schedule()

    def print_schedule(self):
        print("Optimal Schedule:")
        print("-" *80 )
        print(f"{'Task ID':<8}{'Description':<20}{'Duration':<10}{'Deadline':<10}{'Dependencies':<20}{'Total Cost'}")
        print("-" * 80)

        for task in self.problem.schedule:
            task_id = task.getID()
            description = task.getDescription()
            duration = task.getDuration()
            deadline = task.getDeadline()
            dependencies = ", ".join([str(dep) for dep in task.getDependencies()])
            cost = self.min_Path_cost.get(task_id, "N/A")
            
            print(f"{task_id:<8}{description:<20}{duration:<10}{deadline:<10}{dependencies:<20}{cost}")

        print("-" * 80)
        print(f"Minimum Path Cost: {self.min_Path_cost}")
