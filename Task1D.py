# Task 1D Demonstration program
# Yuqing Xue (yx357)

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    stations=build_station_list()
    x=rivers_with_station(stations)
    l=list(x) # convert the set to list
    l.sort() # sort the list in alphabetical order
    print("Number of rivers that have at least one monitoring station:", len(l))
    print("First 10 rivers with stations in alphabetical order:", l[:10])

    rivers_dict=stations_by_river(stations)
    print(rivers_dict['River Aire'])
    print(rivers_dict['River Cam'])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()