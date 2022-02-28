#Task 2G by Jeanne

#set a dangerous value, and use a time step of 30 min 
#to determine whether the river level is rising or falling
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit



stations=build_station_list()
dangerous_level=0.1
station_list=stations_level_over_threshold(stations, dangerous_level)

print(station_list)