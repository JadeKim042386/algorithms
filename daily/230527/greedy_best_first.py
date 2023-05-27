delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

class Node:
    def __init__(self, pos_x, pos_y, goal_x, goal_y, g_cost, parent) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_x, pos_y)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.g_cost = g_cost
        self.parent = parent
        self.f_cost = self.calculate_heuristic()

    def calculate_heuristic(self):
        dx = abs(self.goal_x - self.pos_x)
        dy = abs(self.goal_y - self.pos_y)
        return dx + dy
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    
    

class GreedyBestFirst:
    def __init__(self, grid, start, goal) -> None:
        self.grid = grid
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 9999, None)
        self.open_nodes = [self.start]
        self.closed_nodes = []
        self.reached = False
    
    def search(self):
        while self.open_nodes:
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)
            if current_node.pos == self.target.pos:
                self.reached = True
                return self.retrace_path(current_node)
            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)
            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue
                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)
                else:
                    better_node = self.open_nodes.pop(self.open_nodes.index(child_node))
                    if better_node.g_cost < child_node.g_cost:
                        self.open_nodes.append(better_node)
                    else:
                        self.open_nodes.append(child_node)
        
        if not self.reached:
            return [self.start.pos]
        
    def get_successors(self, parent):
        successors = []
        for action in delta:
            pos_x = action[0] + parent.pos_x
            pos_y = action[1] + parent.pos_y
            if 0 <= pos_x <= len(self.grid[0]) - 1 and 0 <= pos_y <= len(self.grid) - 1 and self.grid[pos_y][pos_x] == 0:
                successors.append(Node(pos_x, pos_y, self.target.pos_x, self.target.pos_y, parent.g_cost + 1, parent))
        return successors
    
    def retrace_path(self, node):
        path = []
        current_node = node
        while current_node:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path