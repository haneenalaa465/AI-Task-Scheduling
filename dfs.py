from node import Node

def depth_first_graph_search(problem, verbose=False):
    """
    Implements DFS for graph search with an optional verbose output.
    """
    # Initialize the root node with the initial list of tasks (problem.tasks)
    node = Node.root(problem.tasks)  
    if problem.goal_state():  # Check if the initial state is the goal
        return solution(node), 1  # Return immediately if start is the goal

    frontier = [node]  # Initialize the frontier as a stack with the root node
    explored = set()  # Set to keep track of explored nodes
    max_frontier_size = 1  # Initialize max frontier size

    # if verbose:
    #     visualizer = Visualizer(problem)  # Optional visualizer for debugging
    #     visualizer.visualize(frontier)

    while frontier:  # While there are nodes to explore
        node = frontier.pop()  # Pop the last node in the frontier (LIFO order for DFS)
        explored.add(node.state)  # Mark the node as explored

        # Expand the frontier with the children
        for action in problem.actions(node.state):  # Get possible actions from the current state
            child = Node.child(problem, node, action)  # Generate child node
            if child.state not in explored and child not in frontier:  # Check if child is unexplored
                if problem.goal_state():  # Check if the child is the goal
                    return solution(child), max_frontier_size  # Return the solution and max frontier size
                frontier.append(child)  # Add child to the frontier (stack)

        # Track the maximum size of the frontier
        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            visualizer.visualize(frontier)  # Visualize the current state of the frontier

    return None, max_frontier_size  # Return None if no solution is found


from problem import Problem
from task import Task

def main():
    # Define tasks with dependencies, durations, deadlines, etc.
    tasks = [
        Task(1, "Task 1", 2, 5, []),
        Task(2, "Task 2", 3, 7, [1]),
        Task(3, "Task 3", 1, 4, [2]),
        # Additional tasks can be added here...
    ]

    # Initialize the Problem instance with tasks
    problem = Problem(tasks)

    # Run Depth-First Search
    solution_path, max_frontier_size = depth_first_graph_search(problem, verbose=True)

    # Print the results
    if solution_path:
        actions, total_cost = solution_path
        print("Solution actions:", actions)
        print("Total path cost:", total_cost)
    else:
        print("No solution found.")

    print("Maximum frontier size encountered:", max_frontier_size)

if __name__ == "__main__":
    main()
