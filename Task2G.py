#Task 2G by Jeanne
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

#set a dangerous value, and use a time step of 30 min 
#to determine whether the river level is rising or falling


#first find the list of stations having 
#the potentially dangerous current level 

stations=build_station_list()
update_water_levels(stations)

dangerous_level=[]
station_list=stations_level_over_threshold(stations, 1.3)

print(station_list)

#then investigate whether the level at that station is rising or falling
#if from the previous data, for 10 consecutive  time steps, the previous level is smaller 
#than the one after it, then it is considered as rising. (here i use a 
# time step of 30 min)
n=0
for station in stations:
    for object in station_list:
        for i in range(20):
            if n<=20:
                dt=3
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            #print(dates)
                if levels[-i]>levels[-i-1]:
                #when the very last value is greater than the second
                #last value, it can be rising
                    print(dates[-i],'rising')
                    n+=1
                else:
                    print('falling')
                





