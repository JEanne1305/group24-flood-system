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
        distance=haversine(i.coord,centre) #calculate the distance 
                                            #between the station and the centre
        if distance<=r:
            required.append(i)#if within the range, add it to the list
    required.sort()
    return required




#Task 1E
#Jeanne - lab group 24 river={}

def rivers_by_station_number(stations, N):
    required=[]
    for station in stations:
        n=1
        for i in range(len(stations)):
            if station.river in required[i][0]: #if river name has appeared in the list before, 
                required[i][1] = required[i][1]+1  #add 1 for the number of station
            
        else:                                       #if not, add the river and the original 
            required.append((station.river,n))     #no. of station into the list
   

    #sort the list of tuple by the number of station
    sorted_by_second = sorted(required, key=lambda tup: tup[1], reverse=True)

    #create a list that contains N rivers with largest no. of stations
    outcome=sorted_by_second[:N]

    #see if any rivers after the 'Nth' river has the same no. of stations,
    #if so, add it to the outcome list
    M=N-1
    while sorted_by_second[M][1]==sorted_by_second[M+1][1]:
        outcome.append(sorted_by_second[M+1])
        M+=1

          

    return outcome