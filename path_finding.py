"""


It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx as nx
import itertools
from country import Country
from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, TeleportingTarteTrolley
from csv_parsing import create_cities_countries_from_csv
import csv_parsing


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    G = nx.Graph()  # create graph obj
    for cityObj in csv_parsing.store_cityObj:  # create nodes of all cities stored in T6(csv_parsing)
        G.add_node(cityObj)

    
    edges_list = []
    for v in itertools.combinations(csv_parsing.store_cityObj, 2):  # do math conbination(unorderd, no repetation)->create edges of all possible combanations of 2 (no duplication)
        if vehicle.compute_travel_time(v[0], v[1]) != math.inf: #v is the tuple of the combination
            edges_list.append((v[0], v[1], {'weight': vehicle.compute_travel_time(v[0], v[1])}))
    G.add_edges_from(edges_list)
    
    try:
        path = nx.shortest_path(G, source=from_city, target=to_city, weight = "weight")  # this returns list of min idstance of itinerary
        return Itinerary(path)
    except:  # this will be executed if path cannot be found(no path error)
        return None


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    # we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)

                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")
    

