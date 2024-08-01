"""


It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import sys
import math
import networkx as nx
import path_finding
from country import Country, find_country_of_city
from city import City, get_city_by_id, get_cities_by_name
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, TeleportingTarteTrolley
from csv_parsing import create_cities_countries_from_csv
import csv_parsing
from map_plotting import plot_itinerary
from path_finding import find_shortest_path




def plot_from_origin_destination(vehicle: Vehicle)->None:
    """
    Plot the shortest path on the map from the origin and destination given by  user input.

    :param vehicle: The vehicle to use.
    :return None
    """
    display_all_cities()  # display only one time
    while True:
        try:
            print("============================== Travel locations ============================")
            print("The above is the list of cities you can travel")
            print("Enter the name of orgin and distination you want to travel")
            print(f"We will be Searching minimum itinerary traveling by [{vehicle.__class__.__name__}]...")
            print("==============================================================================")
            origin_index = 0
            destination_index = 0 # default index val
						
            origin = input("Origin: ")
            assert origin in City.name_to_cities.keys()  # origin must be in the list of city names
            if len(City.name_to_cities[origin])>= 2: # when user entered homonyms city
                origin_index = homonyms_cities_case(origin)

            destination = input("Destination: ")
            assert destination in City.name_to_cities.keys()  # destination must be in the list of city names
            if len(City.name_to_cities[destination])>= 2:
                destination_index = homonyms_cities_case(destination)
            print("")
            print("Seaching...")
            print("The route will be displayed when the search is done...")

        except AssertionError:  # if user input is invalid, promt user input again with the attention
            clear_screen()
            print("**************************************************")
            print("Attention: Make sure you key in valid city name   ")
            print("**************************************************")
            continue

        itinerary_path = find_shortest_path(vehicle, get_cities_by_name(origin)[origin_index], get_cities_by_name(destination)[destination_index])
        if itinerary_path == None:  # no path
            print("Sorry, there is no path in the route. Try other origin and distination.")
            sys.exit()
        else:  # create a map of the shortest path
            plot_itinerary(itinerary_path)
            sys.exit()

def homonyms_cities_case(place: str)->int:
    """
    Give users option of country when user key in homonyms city name.

    :param place: origin or destination
    :return: index 
    """
    while True:
        print("There are 2 same name cities, which city of the country do u choose?") #give user choice
        countryName_city1 = str(find_country_of_city(City.name_to_cities[place][0]).name)
        countryName_city2 = str(find_country_of_city(City.name_to_cities[place][1]).name)
        print("1. "+ countryName_city1)
        print("2. "+ countryName_city2)
        print("Enter the number here: ")
	
        try:
            user_num = input("Number: ")
            assert user_num == "1" or user_num == "2"

        except AssertionError:  # if user key in invalid input(other than 1-2), let user try again with the attention
            clear_screen()
            print("****************************************")
            print("Attention: Enter the number between 1-2")
            print("****************************************")
            continue

        if user_num == "1":
            index = 0
        elif user_num == "2":
            index = 1
        return index #return the country's city user choiced


def display_all_cities()->None:
    """
    Create country objects from csv file and display it on console

    :return: None
    """
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():  # this should have the list and each element is
        country.print_cities()


def clear_screen()->None:
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main()->None:
    """
    Defines the main application loop.
    User chooses the vehicle to travle by.

    :return: None
    """
    while True:
        print("=============== Main Menu ===============")
        print("Enter the number of vehicle to travel by")
        print("1. CrappyCrepeCar")
        print("2. DiplomacyDonutDinghy")
        print("3. TeleportingTarteTrolley")
        print("=========================================")

        try:
            user_input = input("Number: ")
            assert user_input == "1" or user_input == "2" or user_input == "3"

        except AssertionError:  # if user key in invalid input(other than 1-3), let user try again with the attention
            clear_screen()
            print("****************************************")
            print("Attention: Enter the number between 1-3")
            print("****************************************")
            continue

        vehicles = create_example_vehicles()  # set vehicles in vehicles.py as default vehicles
        if user_input == "1":
            clear_screen()
            plot_from_origin_destination(vehicles[0])
        elif user_input == "2":
            clear_screen()
            plot_from_origin_destination(vehicles[1])
        elif user_input == "3":
            clear_screen()
            plot_from_origin_destination(vehicles[2])


main()








