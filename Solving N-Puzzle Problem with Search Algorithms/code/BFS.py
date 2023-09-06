class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):

        if self.queue[0].is_equal(target):
            return True, 0, 0
                
        while self.queue:
            
            current = self.queue.pop(0)
            self.visited[current.UID] = current
            self.counter += 1 
            
            successors = self.graph.reveal_neighbors(current)
            
            for node in successors:
                if node.is_equal(target):
                    return True, self.counter, node.step
                
                elif node.UID not in self.visited:
                    self.queue.append(node)
        

        return False,  self.counter, current.step
