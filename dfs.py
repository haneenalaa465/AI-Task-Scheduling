def dfs(problem):
    stack = []  # Stack for depth-first search
    initial_state = ([], problem.tasks, problem.init_state, set())
    stack.append(initial_state)
    best_schedule = []
    min_cost = float('inf')

    while stack:
        current_schedule, remaining_tasks, current_day, completed_tasks = stack.pop()

        # Check if we have completed a valid schedule
        if len(current_schedule) == problem.length:
            # Calculate cost based on deadlines
            cost = sum(max(0, current_day + task.getDuration() - task.getDeadline()) for task in current_schedule)
            if cost < min_cost:
                min_cost = cost
                best_schedule = current_schedule
            continue

        # Find all possible tasks that can be scheduled next
        possible_tasks = []
        for task in remaining_tasks:
            if not task.getDependencies() or all(dep in completed_tasks for dep in task.getDependencies()):
                possible_tasks.append(task)

        # Sort possible tasks to prioritize those with nearer deadlines
        possible_tasks.sort(key=lambda t: t.getDeadline())

        # Explore each possible task
        for task in possible_tasks:
            new_schedule = current_schedule + [task]
            new_remaining_tasks = [t for t in remaining_tasks if t != task]
            new_current_day = current_day + task.getDuration()
            new_completed_tasks = completed_tasks | {task.getID()}

            stack.append((new_schedule, new_remaining_tasks, new_current_day, new_completed_tasks))

    return best_schedule