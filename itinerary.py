"""


It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name 

class Itinerary():
    """
    Itinerary(): 
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order. 
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        #TODO
        self.cities = cities

    def total_distance(self) -> int: 
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive(within the list) cities.
        :return: the total distance.
        """
        #TODO      
        totalDinstance = 0
        for index in range(0, len(self.cities)-1, 1): # the number of leg = num of cities - 1
            eachDistance = self.cities[index].distance(self.cities[index+1]) 
            totalDinstance += eachDistance 
        return totalDinstance  # total distance will be sum of the each ones
       

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        #TODO
        self.cities.append(city)


    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        minDistance =  math.inf #set initial value as math.inf
        minInsertIndex = 0
        each_possible_distance = 0

        for insertIndex in range(0, len(self.cities), 1): 
            each_possible_cities = self.cities[:insertIndex] + [city] + self.cities[insertIndex:] #try inserting city at every possible place and find min total distance
            each_possible_distance = Itinerary(each_possible_cities).total_distance() 
            if minDistance > each_possible_distance:
                minDistance = each_possible_distance #updating min distance every time it find one
                minInsertIndex = insertIndex
        self.cities = self.cities[:minInsertIndex] + [city] + self.cities[minInsertIndex:]
        
    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"
        :return: a string representing the itinerary.
        """
        #TODO
        if self.cities == []:  
            return f"(0 km)"
        else:
            index = 0
            returnVal =  f"{self.cities[index].name} " # case: only one city
            for index in range(1, len(self.cities), 1): 
                returnVal += f"-> {self.cities[index].name} " # case: 2 or more cities
            returnVal+= f"({self.total_distance()} km)" 
            return returnVal


if __name__ == "__main__":

    create_example_cities() 
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],
                           get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)

