"""


It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City

def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    (Changes: If you plot the map of the entire globe, 
    you can ignore the constraints on size and padding given in the docstring of plot_itinerary.)
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.

    """
    
    m = Basemap(projection= projection,lon_0= 0, resolution='c') # lon_0...central longitude of projection. # resolution = 'c'...use crude resolution coastlines.
    m.drawcoastlines() 
    m.fillcontinents() 

    for i in range(0, len(itinerary.cities)- 1, 1): # draw line between each cities in itinerary
        origin_lat = itinerary.cities[i].coordinates[0]; origin_lon = itinerary.cities[i].coordinates[1]
        distination_lat = itinerary.cities[i + 1].coordinates[0]; distination_lon = itinerary.cities[i + 1].coordinates[1]
        m.drawgreatcircle(origin_lon,origin_lat,distination_lon,distination_lat, linewidth=2,color='b', del_s = 1) 

    filename = "map_"
    for city in itinerary.cities:
        filename += city.name +"_"
    plt.savefig(filename + ".png") 

    





if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))

