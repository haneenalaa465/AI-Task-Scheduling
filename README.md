# AI Task Scheduling - Application of Search Algorithms

## 📚 Course
- Artificial Intelligence (CSAI 301)
- School of Computer Science and Artificial Intelligence
- Zewail City of Science and Technology

## 📌 Objective
We model the task scheduling problem as a search problem. Our goal is to explore and compare the performance of classical search algorithms in generating an optimal execution order of dependent tasks, each with a specific duration and deadline.

## 🧠 Problem Description
The system is given a set of project tasks, where each task has:
 - A unique ID and name
 - A duration and deadline
 - A set of dependencies (other tasks that must be completed first)

The goal is to schedule all tasks in a valid order that:
 - Respects all task dependencies
 - Minimizes delay beyond deadlines

## ▶️ Running the Project
```
python main.py
```

You will be prompted to select one of the following algorithms:
```
bfs, dfs, ids, ucs, greedy, a_star, hillclimb, simulated_annealing, genetic
```
Each algorithm will return a valid task execution order based on the strategy, showing completeness, optimality, and efficiency differences.

