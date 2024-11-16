import heapq  

def a_star(problem):
    pq = []  
    initial_state = (0, [], problem.tasks, problem.init_state, set())  
    heapq.heappush(pq, initial_state) 

    best_schedule = []
    min_cost = float('inf')

    while pq:
        current_cost, current_schedule, remaining_tasks, current_day, completed_tasks = heapq.heappop(pq)

        if len(current_schedule) == problem.length:
            if current_cost < min_cost:
                min_cost = current_cost
                best_schedule = current_schedule
            continue

        possible_tasks = []
        for task in remaining_tasks:
            if not task.getDependencies() or all(dep in completed_tasks for dep in task.getDependencies()):
                possible_tasks.append(task)

        for task in possible_tasks:
            new_schedule = current_schedule + [task]
            new_remaining_tasks = [t for t in remaining_tasks if t != task]
            new_current_day = current_day + task.getDuration()
            new_completed_tasks = completed_tasks | {task.getID()}

            penalty_cost = sum(max(0, new_current_day + t.getDuration() - t.getDeadline()) for t in new_schedule)
            total_cost = new_current_day + penalty_cost

            heapq.heappush(pq, (total_cost, new_schedule, new_remaining_tasks, new_current_day, new_completed_tasks))
    return best_schedule
