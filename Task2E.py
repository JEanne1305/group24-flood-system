#Task 2E by Jeanne
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
#to locate the 5 stations that has greatest current relative water level.
stations=build_station_list()
#i want the list of names of the 5 stations
station_required=list(stations_highest_rel_level(stations,5))
print(type(station_required))
print(station_required[:][0])


#what i need is let stations_highest_rel locate the 5 stations 
#that needed to be on the graph
#and then the input 

#data about dates and level:
t=[]
level=[]
dt = 10
dates, levels = fetch_measure_levels(
        station_required.measure_id, dt=datetime.timedelta(days=dt))

def run():
    for station in station_required:
        for i in stations:
            if station==i.name:
                plot_water_levels(i,t,level)

        
        
