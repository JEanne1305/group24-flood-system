#Task 2E by Jeanne
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

#to locate the 5 stations that has greatest current relative water level.
stations=build_station_list()
station_required=stations_highest_rel_level(stations,5)

#def run():

    #for i in station_required:
    #   plot_water_levels(i,,)
