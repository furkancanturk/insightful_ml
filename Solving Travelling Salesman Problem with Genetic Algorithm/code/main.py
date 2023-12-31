from CityManager import CityManager
from RouteManager import RouteManager
from GeneticAlgorithmSolver import GeneticAlgorithmSolver

if __name__ == '__main__':
    cm = CityManager()
    cm.build_country()

    cm = CityManager()
    cm.build_country()
    rm = RouteManager(cm, 150)

    print(rm.find_best_route().calc_route_distance())

    gas = GeneticAlgorithmSolver(cm, 150)
    rm = gas.solve(rm)

    print(rm.find_best_route().calc_route_distance())
    print(rm.find_best_route())

