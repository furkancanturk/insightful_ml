import queue as Q

class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.step, root, root.UID))

    def run(self, target):

        while not self.queue.empty():
           
            step, current, UID = self.queue.get(False)
            self.visited[UID] = current
            self.counter += 1

            if current.is_equal(target):
                return True, self.counter, current.step

            successors = self.graph.reveal_neighbors(current)

            for node in successors:
                if node.UID not in self.visited:
                    self.queue.put((node.step, node, node.UID))
                          
        return False, self.counter, current.step
