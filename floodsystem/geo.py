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
def rivers_with_station(stations): # return a set of names of rivers that have at least one monitoring station
   rivers_set=set()
   for station in stations:
      rivers_set.add(station.river)
   return rivers_set 

def stations_by_river(stations): # returns a dictionary of rivers (key: river, value: array of station names)
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
            required.append(i.name)#if within the range, add it to the list
    
    return sorted(required)




#Task 1E
#Jeanne - lab group 24 river


    
def rivers_by_station_number(stations, N):
    print("hello")
    a=0
    required={}
    for station in stations:
        #a+=1
        #if a>40:
        #    break
        river=station.river
        if river in required:
            required[river]+=1
        else: 
            required[river]=1
    
    print(required)
    a_tuple=required.items()
    a_list=list(a_tuple)
    #print(a_list)
    

    #sort the list of tuple by the number of station
    final_version = sorted(a_list, key=lambda tup: tup[1], reverse=True)

    #create a list that contains N rivers with largest no. of stations
    outcome=final_version[:N]

    #see if any rivers after the 'Nth' river has the same no. of stations,
    #if so, add it to the outcome list
    M=N-1
    while final_version[M][1]==final_version[M+1][1] and M<=(len(final_version)-1):
        outcome.append(final_version[M+1])
        M+=1


    return outcome




#Task 2C Jeanne
def stations_highest_rel_level(stations, N):
    station_level={}
    n=0
    for i in range(len(stations)):
        name=stations[i].name
            
        typ_range=stations[i].typical_range
        if typ_range == None:
            break
        else:
            station_level[name]=typ_range[1]

    a_tuple=station_level.items()
    a_list=list(a_tuple)
    #print(a_list)
    
    #sort the list of tuple by the highest level
    sorted_level = sorted(a_list, key=lambda tup: tup[1], reverse=True)

    #create a list that contains N stations with highest relative level
    outcome =sorted_level[:N]
    

    return outcome
