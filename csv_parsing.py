"""


It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country, add_city_to_country


store_cityObj = [] # this store city obj created in the process of reading csv file

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    #TODO
    with open(path_to_csv, "r") as fileref:
        lines = csv.reader(fileref)
        header = next(lines)#skip the header

        #specify index of "The header name"       
        name_index = header.index("city_ascii")
        coordinate_x_index = header.index("lat")
        coordinate_y_index = header.index("lng")
        city_type_index = header.index("capital")
        pupulation_index = header.index("population")
        id_index = header.index("id")

        country_index = header.index("country")
        io3_index = header.index("iso3") 

        for row in lines:
                try:
                    city_obj = City(row[name_index], (float(row[coordinate_x_index]),float(row[coordinate_y_index])), row[city_type_index] , int(row[pupulation_index]), int(row[id_index]))
                    add_city_to_country(city_obj, row[country_index], row[io3_index]) #create country obj 
                    store_cityObj.append(city_obj)# this is for T7

                except ValueError: # when hitting ""(empty string), population will be 0
                    city_obj = City(row[name_index], (float(row[coordinate_x_index]),float(row[coordinate_y_index])), row[city_type_index] , 0, int(row[id_index]))
                    add_city_to_country(city_obj, row[country_index], row[io3_index]) 
                    store_cityObj.append(city_obj)

if __name__ == "__main__":
    #Ex. 1) worldcities_truncated_aus.csv
    #Ex. 2) worldcities_truncated.csv
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values(): # this should have the list and each element is 
        country.print_cities()
    #print(len(City.name_to_cities))
    #print(len(Country.name_to_countries))
