from collections import deque

class BFSScheduler:
    def __init__(self, problem):
        self.problem = problem
        self.optimal_schedule = None

    def bfs_tree(self):
        # Initialize BFS queue
        queue = deque()
        # Each queue element is a tuple: (current_schedule, remaining_tasks, current_day, completed_tasks)
        initial_state = ([], self.problem.tasks, self.problem.init_state, set())
        queue.append(initial_state)
        
        optimal_schedule = None
        optimal_cost = float('inf')  # Tracks the lowest cost

        while queue:
            current_schedule, remaining_tasks, current_day, completed_tasks = queue.popleft()

            # Check if we reached a goal state (all tasks are scheduled)
            if len(current_schedule) == self.problem.length:
                # Compute total cost of this schedule
                cost = sum(
                    task.getDeadline() - task.getDuration() - current_day 
                    for task in current_schedule
                )
                # Update optimal schedule if this one is better
                if cost < optimal_cost:
                    optimal_cost = cost
                    optimal_schedule = current_schedule
                continue

            # Generate all possible actions (tasks that have no remaining dependencies)
            possible_routes = {}
            for task in remaining_tasks:
                # A task is ready to be scheduled if all its dependencies are completed
                dependencies = task.getDependencies()
                if all(dep in completed_tasks for dep in dependencies):
                    cost = task.getDeadline() - task.getDuration() - current_day
                    possible_routes[task] = cost

            # Enqueue new states for BFS
            for task, cost in possible_routes.items():
                # Create new state: append the task to the schedule, mark it as completed
                new_schedule = current_schedule + [task]
                new_remaining_tasks = [t for t in remaining_tasks if t != task]
                new_current_day = current_day + task.getDuration()

                # Update completed tasks set
                new_completed_tasks = completed_tasks.copy()
                new_completed_tasks.add(task.getID())

                # Update dependencies for the remaining tasks
                for t in new_remaining_tasks:
                    dependencies = t.getDependencies()
                    if task.getID() in dependencies:
                        dependencies.remove(task.getID())  # Remove completed task ID
                        t.setDependencies(dependencies)

                queue.append((new_schedule, new_remaining_tasks, new_current_day, new_completed_tasks))

        # Set the optimal schedule
        self.optimal_schedule = optimal_schedule

    def get_optimal_schedule(self):
        return self.optimal_schedule

    def print_schedule(self):
        if not self.optimal_schedule:
            print("No schedule has been computed yet. Run bfs_tree() first.")
            return

        print("Optimal Schedule:")
        for idx, task in enumerate(self.optimal_schedule, start=1):
            print(f"{idx}. Task ID: {task.getID()}, Description: {task.getDescription()}, "
                  f"Deadline: {task.getDeadline()}, Duration: {task.getDuration()}")
