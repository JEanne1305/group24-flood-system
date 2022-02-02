# Task 1F Demonstration program
# Yuqing Xue (yx357)

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    stations=build_station_list()
    inconsistency=inconsistent_typical_range_stations(stations)
    inconsistency.sort()
    print(inconsistency)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
