from task import Task
import random
import math

class Problem:
    def __init__(self, tasks, init_state):
        self.tasks = tasks
        self.init_state = init_state
        self.schedule = None  # store final schedule

class SimulatedAnnealing:
    def __init__(self, problem, initial_temperature=1000, cooling_rate=0.95):
        self.problem = problem
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate

    def evaluate_schedule(self, schedule):
        # Calculate the total penalty for the given schedule
        current_time = 0
        total_penalty = 0
        for task in schedule:
            current_time += task.getDuration()
            if current_time > task.getDeadline():
                total_penalty += current_time - task.getDeadline()  # Penalty for being late
        return -total_penalty  # maximize the negative penalty

    def get_neighbors(self, schedule):
        # Generate neighboring schedules by swapping two tasks
        neighbors = []
        for i in range(len(schedule)):
            for j in range(i + 1, len(schedule)):
                neighbor = schedule[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap tasks
                neighbors.append(neighbor)
        return neighbors

    def climb(self):
        current_schedule = self.problem.init_state
        current_value = self.evaluate_schedule(current_schedule)

        while self.temperature > 1:
            neighbors = self.get_neighbors(current_schedule)
            next_schedule = random.choice(neighbors)
            next_value = self.evaluate_schedule(next_schedule)

            # Calculate value changes
            delta = next_value - current_value

            # Decide whether to accept 
            if delta > 0 or random.uniform(0, 1) < math.exp(delta / self.temperature):
                current_schedule = next_schedule
                current_value = next_value
            
            # Print  current schedule and value for debugging
            print(f"Current Schedule: {[task.getID() for task in current_schedule]}, Value: {current_value}, Temperature: {self.temperature}")

            # cool down  temperature
            self.temperature *= self.cooling_rate

        # Update the problem's schedule with the best found schedule
        self.problem.schedule = current_schedule
        return current_schedule, current_value

# eg
tasks = [
    Task(ID=1, description="Task 1", duration=4, deadline=5, dependencies=[]),  
    Task(ID=2, description="Task 2", duration=3, deadline=6, dependencies=[]),  
    Task(ID=3, description="Task 3", duration=2, deadline=4, dependencies=[]),  
]

initial_state = random.sample(tasks, len(tasks))
problem = Problem(tasks, initial_state)

simulated_annealing = SimulatedAnnealing(problem)
best_schedule, best_value = simulated_annealing.climb()

print("Best Schedule:", [task.getID() for task in best_schedule], "Value:", best_value)