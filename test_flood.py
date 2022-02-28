# Test Task 2B: return a list of tuples, where each tuple holds 
# (i) a station (object) at which the latest relative water level is over tol 
# (ii) the relative water level at the station
# Yuqing Xue (yx357)

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key

def test_stations_level_over_threshold():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    tol=0.8
    station_list=stations_level_over_threshold(stations, tol)
    for i in station_list:
        for station in stations:
            if i[0]==station.name:
                assert station.latest_level>tol
