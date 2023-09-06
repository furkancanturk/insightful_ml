class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):

        if self.stack[0].is_equal(target):
            return True, 0, 0
                
        while self.stack:

            current = self.stack.pop(-1)
            self.visited[current.UID] = current
            self.counter += 1 
            
            successors = self.graph.reveal_neighbors(current)
            
            for node in successors:
                if node.is_equal(target):
                    return True, self.counter, node.step
                
                elif node.UID not in self.visited:
                    self.stack.append(node)
                    
        return False, self.counter, current.step
