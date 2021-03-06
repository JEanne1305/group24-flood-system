"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius,rivers_by_station_number
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.flood import stations_highest_rel_level


# Test 1B: stations by distance
# Yuqing Xue (yx357)
def test_stations_by_distance():
    # Build list of stations
    stations = build_station_list()
    cambridge=(52.2053, 0.1218)
    x=stations_by_distance(stations, cambridge)
    initial_distance=0
    for i in range(len(x)-1):
        assert x[i][1]<=x[i+1][1] # test that the distance is ascending


# Test 1D: rivers with station & stations by river
# Yuqing Xue (yx357)
def test_stations_by_river():
    stations = build_station_list()

    rivers_dict=stations_by_river(stations)
    assert len(rivers_dict)==len(rivers_with_station(stations)) # check the number of rivers that have at least one monitoring station

    station_count=0
    for i in rivers_dict.values():
        assert len(i) # check that value of the item is not empty
        station_count+=len(i)
    assert station_count==len(stations) # check the total number of stations is correct (i.e. no station is left out)


#task 1C
#Jeanne
def test_station_within_radius():
    stations=build_station_list()
    centre=(52.2053, 0.1218)
    r=10
    required=stations_within_radius(stations,centre,r)
    for i in required :
        assert required[i]<required[i+1]

#task 1E
#Jeanne
def test_rivers_by_station_number():
    stations=build_station_list()
    N=7
    outcome=rivers_by_station_number(stations,N)
    assert outcome[N-1][1]>outcome[N][1] #make sure the repeated no. has already displayed


#task 2C
#Jeanne

#test if the output is a station object:

def test_stations_highest_rel_level():
    stations= stations=build_station_list()
    N=7
    outcome=stations_highest_rel_level(stations,N)
    assert type(outcome)=='floodsystem.station.MonitoringStation' #make sure the individual element of the list is station object
