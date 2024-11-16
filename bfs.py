from collections import deque

def bfs(problem):
    queue = deque()
    min_cost = float('inf')
    
    for task in problem.tasks:
        if not task.getDependencies():
            queue.append(task)
    
    while queue:
        task = queue.popleft()
        
        if task not in problem.schedule:
            problem.action()  

        if problem.goal_state():
            cost = sum((task.getDeadline() - task.getDuration() - problem.today) for task in problem.schedule)
            min_cost = min(cost, min_cost)

        for n_task in problem.tasks:
            if n_task not in problem.schedule and all(dep in problem.schedule for dep in n_task.getDependencies()):
                queue.append(n_task)

    return problem.schedule
