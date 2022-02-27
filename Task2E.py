#Task 2E by Jeanne
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels

#to locate the 5 stations that has greatest current relative water level.
#And produce a list of names
stations=build_station_list()
station_required=list(stations_highest_rel_level(stations,5))

required_list=[]
for i in range(len(station_required)):
    
    required_list.append(station_required[i][0])

print(required_list)

#what i need is let stations_highest_rel locate the 5 stations 
#that needed to be on the graph
#and then the input 



def run():

    #data about dates and level:
    t=[]
    level=[]
    dt = 10
    for i in stations:
        for station in required_list:
            #print(station)
            if station==i.name:
                #print('111')
                dates, levels = fetch_measure_levels(
                        i.measure_id, dt=datetime.timedelta(days=dt))
                #print('222')
                for date, levels in zip(dates, levels):
                    appro_date=date.strftime("%H:%M:%S.%f - %b %d %Y")
                    t.append(appro_date)
                    #print('333')#print(level)
                    level.append(levels)
                    #print('555')
                    #print(t)
                plot_water_levels(i,t,level)
                print('444')
                
            else:
                break


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
        
