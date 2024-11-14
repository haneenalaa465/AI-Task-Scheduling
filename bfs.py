from collections import deque
from node import Node

def breadth_first_graph_search(problem, verbose=False):
    """
    Implements BFS for graph search with an optional verbose output.
    """
    node = Node.root(problem.init_state)  # Create the root node from the initial state
    if problem.goal_test(node.state):  # Check if the initial state is the goal
        return solution(node), 1  # Return immediately if start is the goal

    frontier = deque([node])  # Initialize the frontier with the root node
    explored = set()  # Set to keep track of explored nodes
    max_frontier_size = 1  # Initialize max frontier size

    if verbose:
        visualizer = Visualizer(problem)  # Optional visualizer for debugging
        visualizer.visualize(frontier)

    while frontier:  # While there are nodes to explore
        node = frontier.popleft()  # Dequeue the first node in the frontier
        explored.add(node.state)  # Mark the node as explored

        # Expand the frontier with the children
        for action in problem.actions(node.state):  # Get possible actions from the current state
            child = Node.child(problem, node, action)  # Generate child node
            if child.state not in explored and child not in frontier:  # Check if child is unexplored
                if problem.goal_test(child.state):  # Check if the child is the goal
                    return solution(child), max_frontier_size  # Return the solution and max frontier size
                frontier.append(child)  # Add child to the frontier

        # Track the maximum size of the frontier
        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            visualizer.visualize(frontier)  # Visualize the current state of the frontier

    return None, max_frontier_size  # Return None if no solution is found
