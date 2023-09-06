from RouteManager import RouteManager
from Route import Route
import random


class GeneticAlgorithmSolver:
    def __init__(self, cities, 
                 population_size=150, 
                 mutation_rate=0.4, 
                 tournament_size=2, 
                 elitism=True, 
                 n_generations=200, 
                 random_seed=42):
        
        self.cities = cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elitism = elitism
        self.n_generations = n_generations
        self.random_seed = random_seed

    def solve(self, rm):
        random.seed(self.random_seed)
        rm = self.evolve(rm)
        for i in range(self.n_generations):
            rm = self.evolve(rm)
        return rm

    def evolve(self, rm):
        routes = rm.routes
        pool = self.tournament(routes)
        
        new_generation = []
        parent1 = next(pool, False)
        parent2 = next(pool, False)
            
        while parent1 and parent2:
            
            siblings = self.crossover(parent1, parent2)
            new_generation += siblings
            
            parent1 = next(pool, False)
            parent2 = next(pool, False)
        
        for individual in new_generation:
            if random.random() < self.mutation_rate:
                self.mutate(individual)


        if self.elitism:
            new_generation += routes
            new_generation = sorted(new_generation, key=lambda r: r.fitness, reverse=True)
            new_generation = new_generation[:self.population_size]
            
        rm.routes = new_generation
  
        return rm

    def crossover(self, route_1, route_2):
       
        siblings = []
        for i in range(2):
            
            beg_ind, end_ind = sorted([random.randint(0, len(self.cities)-1), random.randint(0, len(self.cities)-1)])        
            child = []
    
            for i in range(len(self.cities)):
                if i >= beg_ind and i<= end_ind:
                    child.append(route_1[i])
            
            child += [c for c in route_2 if c not in child]
                    
            new_route = Route(self.cities)
            new_route.route = child
            new_route.calc_route_distance()
            new_route.calc_fitness()
            siblings.append(new_route)
        
        return siblings
    
    def mutate(self, route):
        
        ind1, ind2 = sorted([random.randint(0, len(self.cities)-1), random.randint(0, len(self.cities)-1)])        
        
        c1 = route[ind1]
        c2 = route[ind2]
        route[ind1] = c2
        route[ind2] = c1
        route.calc_route_distance()
        route.calc_fitness()


    def tournament(self, population):
        pool = []
        
        for i in range(len(population)):
            individuals = random.choices(population, k=self.tournament_size)
            pool.append(max(individuals, key=lambda route: route.fitness))
            
        return iter(pool)
