def dfs(problem):
    # initialize stack
    stack = [([], problem.tasks, problem.init_state, set())]
    best_schedule = []
    minimum_cost = float('inf')

   
    while stack:
        current_schedule, remaining_tasks, current_day, completed_tasks = stack.pop()

        # if the schedule is complete, calculate the cost
        if len(current_schedule) == problem.length:
            cost = 0
            for task in current_schedule:
                delay = max(0, current_day + task.getDuration() - task.getDeadline())
                cost += delay
            # Update best schedule if the cost is lower
            if cost < minimum_cost:
                minimum_cost = cost
                best_schedule = current_schedule
            continue

        # Find tasks can be added next
        next_tasks = []
        for task in remaining_tasks:
            dependencies = task.getDependencies()
            if not dependencies or all(dep in completed_tasks for dep in dependencies):
                next_tasks.append(task)

        # sort tasks 
        next_tasks.sort(key=lambda t: t.getDeadline())

        # updated state in stack
        for task in next_tasks:
            new_schedule = current_schedule + [task]
            new_remaining_tasks = []
            for t in remaining_tasks:
                if t != task:
                    new_remaining_tasks.append(t)
            new_day = current_day + task.getDuration()
            completed_tasks.add(task.getID())

            stack.append((new_schedule, new_remaining_tasks, new_day, completed_tasks))

    return best_schedule
