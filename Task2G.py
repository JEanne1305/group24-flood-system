#Task 2G by Jeanne
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels


#set a dangerous value, and use a time step of 30 min 
#to determine whether the river level is rising or falling


#first find the list of stations having 
#the potentially dangerous current level 

stations=build_station_list()
update_water_levels(stations)

dangerous_level=[]
station_list=stations_level_over_threshold(stations, 44)
print(len(station_list))
print(station_list)

#then investigate whether the level at that station is rising or falling
#if from the previous data, for 20 consecutive time steps, the previous level is smaller 
#than the one after it, then it is considered as rising. (here i use a 
# time step of 30 min)




for object in station_list:
    for station in stations:
        if object[0]==station.name:
            #print(object[0])
            if object[0]=='Letcombe Bassett': #ignore the wrong data
                continue
            n=0 #counting the number of time steps
            r=0 #counting the no. of rising
            m=0 #allowance for the level to fluctuate, max is 5
            a=0 #allowance for same level
            for i in range(30):

                if n<30 or m<=15:
                    dt=5
                    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
                #print(dates)
                    if levels[-i]>levels[-i-1]:#when the very last value is greater than the second
                                                #last value, it can be rising
                        #print(dates[-i],'rising')
                        n+=1
                        r+=1
                    elif levels[-i]==levels[-i-1]:
                        #print('same')
                        a+=1
                        n+=1
                    else:
                        #print('falling')
                        #print(levels[-i],dates[-i],'falling')
                        m+=1
                        n+=1
            if m>15 and n==30:
                print(object[0],'is safe, since its level falls for',m,'times')
            elif a>10 and n==30:   
                print(object[0],'is stable, since its level is the same for',a,'times')
            elif r>16 and n==30:
                print(object[0],'is not-safe, since its level rises for',r,'times')
            elif n==30:
                print(object[0],'the boundaries are not applicable, choose another number','it rises, falls, stable for',r,m,a)
            break
                    
                
                        
                        





