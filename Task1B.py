# Task 1B Demonstration program
# Yuqing Xue (yx357)

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations=build_station_list()
    cambridge=(52.2053, 0.1218)
    x=stations_by_distance(stations, cambridge)
    print("The closest 10 entries:", x[:10])
    print("The furthest 10 entries:", x[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
