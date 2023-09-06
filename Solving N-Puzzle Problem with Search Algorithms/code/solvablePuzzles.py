import numpy as np
import random
random.seed(42)

import pandas as pd
from Graph import Graph
from Node import Node

from BFS import BFS
from DFS import DFS
from AStar import AStar
from UCS import UCS

from time import time

if __name__ == "__main__":
    N = 8
    G = Graph(N)

    base_arr = list(np.arange(N+1))

    instances = []
    
    for i in range(50):
        random.shuffle(base_arr)
        init_state = np.array(base_arr).reshape(3,3)
        root = Node(init_state, 0, list(), None)
        
        goal_state = root
        n_steps = random.randint(10, 50)
        
        for step in range(n_steps):
            neighbours = G.reveal_neighbors(goal_state)
            goal_state = random.choice(neighbours)
    
        target = Node(goal_state.node, 0, list(), None)
        
        instances.append([root, target, n_steps])

    
    for opt in [1,2,3,4]:
        results = []
        for i in range(50):
            root, target, n_steps = instances[i]
        
            print(root)
            print(target)

            if opt == 1:
                algorithm = BFS(G, root)
            elif opt == 2:
                algorithm = DFS(G, root)
            elif opt == 3:
                algorithm = UCS(G, root)
            elif opt == 4:
                algorithm = AStar(G, root)
            print(opt, i)
            init_time = time()
            found, counter, step = algorithm.run(target)
            elapsed_time = time() - init_time
            results.append([opt, n_steps, int(found), counter, step, elapsed_time])
            
            if found:
                print("Match found!\n"
                      "Num. of visited nodes: {}\n"
                      "Depth of graph: {}".format(counter, step))
            else:
                print("Match not found!\n")
            print("Elapsed time: {} secs.".format(elapsed_time))

        pd.DataFrame(np.array(results)).to_excel(f"results{opt}.xlsx", header=False, index=False)