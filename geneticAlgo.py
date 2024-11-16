import random

class GeneticAlgorithm:
    def __init__(self, tasks, population_size, max_generations, mutation_rate):
        self.tasks = tasks
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.population = self.init_population()

    def init_population(self):
        population = []
        for i in range(self.population_size):
            chromosome = random.sample(self.tasks, len(self.tasks))  #shuffle 
            population.append(chromosome)
        return population

    def fitness_fn(self, chromosome):
        fit = 0
        for task in chromosome:
            if task:
                fit += 1
        return fit

    def selection(self, population, fitness_fn):
        population_with_fitness = [(chrom, fitness_fn(chrom)) for chrom in population]
        population_with_fitness.sort(key=lambda x: x[1], reverse=True)
        return population_with_fitness[0][0], population_with_fitness[1][0]

    def crossover(self, parent1, parent2):
        half = len(parent1) // 2
        parent1_half_tasks = parent1[:half]
        parent2_half_tasks = []
        for task in parent2:
            if task not in parent1_half_tasks:
                parent2_half_tasks.append(task)
        new_child = parent1_half_tasks + parent2_half_tasks
        return new_child

    # swap:
    def mutate(self, chromosome):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(len(chromosome)), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

    def genetic(self):
        generation = 1
        best_solution = None
        while generation <= self.max_generations:
            new_population = []

            for i in range(self.population_size // 2):
                parent1, parent2 = self.selection(self.population, self.fitness_fn)
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])
            self.population = new_population
            
            best_solution = self.population[0]
            print(f"Generation {generation}: Best chromosome:")
            for task in best_solution:
                task.task_vis()  

            generation += 1

        return best_solution

# //////////////////////////////////////////////////////////////////////////////////////////////////////
