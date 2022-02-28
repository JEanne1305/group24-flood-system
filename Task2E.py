#Task 2E by Jeanne
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np



#what i need is let stations_highest_rel locate the 5 stations 
#that needed to be on the graph
#and then the input 



def run():
    #to locate the 5 stations that has greatest current relative water level.
    #And produce a list of names
    stations=build_station_list()
    station_required=list(stations_highest_rel_level(stations,5))

    required_list=[]
    for i in range(len(station_required)):
        required_list.append(station_required[i][0])

    print(required_list)
    #data about dates and level:
    t=[]
    levels_=[]
    dt = 10
    for station in required_list:
        station_r=None
        for i in stations:
            #print(i)
            if  i.name == station:
                print('333')
                station_r=i
        dt=10
        dates, levels = fetch_measure_levels(station_r.measure_id, dt=datetime.timedelta(days=dt))
        print(len(dates))
        print(len(levels))        
                
        plot_water_levels(station_r,np.transpose(dates),levels)
        print('444')        
            


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
        