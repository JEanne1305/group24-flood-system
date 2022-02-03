#task 1C
#Jeanne 
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


stations=build_station_list()
a=(52.2053,0.1218)
print(stations_within_radius(stations,a,10))