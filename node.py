class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    # initialize root of tree
    @classmethod
    def root(cls, init_state):
        return cls(init_state, None, None, 0)

    # initialize new child nodes
    @classmethod
    def child(cls, problem, parent, action):
        return cls(
            problem.result(),
            parent,
            action,
            parent.path_cost + problem.step_cost())

def solution(node):
    actions = []
    cost = node.path_cost
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions, cost