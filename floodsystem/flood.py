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
    outcome1 =sorted_level[:N]
    outcome2=[]
    print(outcome1[1])
    for i in range(len(outcome1)):
        for name in outcome1[i]:
            #print(name)
            for station in stations:
                #print('222')
                if station.name==name :
                    
                    outcome2.append(station) 
    
    outcome = sorted(outcome2, key=lambda x: x.typical_range[1],reverse=True)

    return outcome