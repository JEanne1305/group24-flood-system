# Task 2B: return a list of tuples, where each tuple holds 
# (i) a station (object) at which the latest relative water level is over tol 
# (ii) the relative water level at the station
# Yuqing Xue (yx357)

from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    # create an empty list for station with level over threshold
    list_of_stations_over_threshold=[]

    for station in stations:
        # check the consistency of water level
        if station.latest_level!=None:
            if MonitoringStation.typical_range_consistent(station) is True:
                # if the range data is validated
                if station.latest_level>tol:
                    station_tuple=(station.name, MonitoringStation.relative_water_level(station)) # create the tuple for individual stations
                    list_of_stations_over_threshold.append(station_tuple)
    return list_of_stations_over_threshold
