# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

# Task 1B
# Yuqing Xue (yx357)
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    station_list=[] #create an empty list to store the output
    for station in stations:
       distance=haversine(station.coord, p) # in kilometers
       station_tuple=(station.name, distance) # create the tuple for individual stations
       station_list.append(station_tuple)

    # sort stations by distance
    return sorted_by_key(station_list, 1)


# Task 1D 
# Yuqing Xue (yx357)
def rivers_with_station(stations):
   rivers_set=set()
   for station in stations:
      rivers_set.add(station.river)
   return rivers_set 

def stations_by_river(stations):
   rivers_dict={}
   for station in stations:
      if station.river in rivers_dict:
         rivers_dict[station.river].append(station.name)
         rivers_dict[station.river].sort()
      else:
         rivers_dict[station.river]=[station.name] # create a list of station names
   return rivers_dict


#Task 1C
#Jeanne
def stations_within_radius(stations,centre,r):
    
    required=[]
    for i in stations:
        distance=haversine(i.coord,centre)
        if distance<=r:
            required.append(i)
    required.sort()
    return required