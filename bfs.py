from collections import deque

def bfs(problem):
    queue = deque()
    initial_state = ([], problem.tasks, problem.init_state, set())
    queue.append(initial_state)
    schedule = []
    min_cost = float('inf')  
    task_dependencies = {task.getID(): set(task.getDependencies()) for task in problem.tasks}

    while queue:
        current_schedule, remaining_tasks, current_day, completed_tasks = queue.popleft()
        
        if len(current_schedule) == problem.length:
            cost = sum((task.getDeadline() - task.getDuration() - current_day) for task in current_schedule)
            if cost < min_cost:
                min_cost = cost
                schedule = current_schedule
            continue

        possible_routes = {}
        for task in remaining_tasks:
            dependencies = task_dependencies.get(task.getID(), set())
            if dependencies.issubset(completed_tasks):  
                cost = task.getDeadline() - task.getDuration() - current_day
                possible_routes[task] = cost

        if not possible_routes:
            continue

        for task, cost in possible_routes.items():
            new_schedule = current_schedule + [task]  
            new_remaining_tasks = [t for t in remaining_tasks if t != task]
            new_current_day = current_day + task.getDuration()

            remaining_completed_tasks = completed_tasks.copy()
            remaining_completed_tasks.add(task.getID())

            for t in new_remaining_tasks:
                dependencies = t.getDependencies()
                if task.getID() in dependencies:
                    dependencies.remove(task.getID())  
                    t.setDependencies(dependencies)

            queue.append((new_schedule, new_remaining_tasks, new_current_day, remaining_completed_tasks))

    return schedule

def print_schedule(schedule):
    if not schedule:
        print("No schedule :(")
        return

    print("Schedule:")
    for task in schedule:
        task.task_vis()  
