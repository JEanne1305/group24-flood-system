#Task 2E by Jeanne

from floodsystem.stationdata import build_station_list, update_water_levels
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
    update_water_levels(stations)
    station_required=stations_highest_rel_level(stations,5)
    print(station_required)
    t=[]
    levels_=[]
    dt = 10
    for station in station_required:  
        
        if station.name=='Letcombe Bassett':
            print('same')
            continue
        dt=10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        print(len(dates))
        print(len(levels))        
        plot_water_levels(station,dates,levels)
        print('444')        
            


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
        