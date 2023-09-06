import queue as Q

class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
     
        self.root.distance = self.manhattan_distance(self.root, target)
        self.root.distance_top = self.root.distance + self.root.step 
        self.queue.put((self.root, self.root.UID))
        
        while not self.queue.empty():
            
            current, UID = self.queue.get(False)

            self.visited[UID] = current
            self.counter += 1 

            if current.is_equal(target):
                return True, self.counter, current.step
            
            successors = self.graph.reveal_neighbors(current)
            
            for node in successors:
                if node.UID not in self.visited:   
                    node.distance = self.manhattan_distance(node, target)
                    node.distance_top = node.distance + node.step
                    self.queue.put((node, node.UID))

            
        return False,  self.counter, current.step

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size+1)
        brr = [0] * (self.graph.size+1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        
        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        
        dist = 0

        for i in range(1,len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
