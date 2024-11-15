import queue  # q.put() / get()
from problem import Problem
class UCS:
    def __init__(self, tree, init_state, problem):
        self.frontier = queue.PriorityQueue() # the frontier's data str is a priority queue
        self.tree = tree
        self.init_state = init_state
        self.min_Path_cost = {}
        self.problem = problem # an instance form Problem

    def findPath(self):
        init_state = self.problem.init_state
        self.frontier.put((0, self.init_state))
        self.min_Path_cost[self.init_state.getID()] = 0 
        while not self.frontier.empty():
            current_cost, current_task = self.frontier.get()
            # check if it is the goal
            if self.problem.goal_state():
                break
            possible_routes = self.problem.step_cost()
            for t, t_cost in possible_routes.items():
                total_cost = current_cost+ t_cost
                # print(f"Checking task {t.getID()} with cost {total_cost}")
                if total_cost < self.min_Path_cost.get(t.getID()):
                    self.min_Path_cost[t.getID()] = total_cost
                    self.frontier.put((total_cost, t)) #  tuple
                    self.problem.schedule.append(t) 
                    # print(f"Added task {task.getID()} to frontier with cost {total_cost}")

            self.problem.action()

        self.print()

    def print(self):
        print("Optimal Schedule:", self.problem.schedule)
        print("Minimum Path Cost:", self.min_Path_cost)




        







    


# 2.      Add the starting node to the opened list. The node has
# 3.      has zero distance value from itself
# 4.      while True:
# 5.         if opened is empty:
# 6.            break # No solution found
# 7.         selecte_node = remove from opened list, the node with
# 8.                        the minimun distance value
# 9.         if selected_node == target:
# 10.           calculate path
# 11.           return path
# 12.        add selected_node to closed list
# 13.        new_nodes = get the children of selected_node
# 14.        if the selected node has children:
# 15.           for each child in children:
# 16.              calculate the distance value of child
# 17.              if child not in closed and opened lists:
# 18.                 child.parent = selected_node
# 19.                 add the child to opened list
# 20.              else if child in opened list:
# 21.                 if the distance value of child is lower than
# 22.                  the corresponding node in opened list:
# 23.                    child.parent = selected_node
# 24.                    add the child to opened list