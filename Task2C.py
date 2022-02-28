#task 2C by Jeanne
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level


stations=build_station_list()
station=stations[0]
print(station.typical_range)
print(stations[0].name)
#stations_level_over_threshold(stations, 0.8)

def run():
    stations=build_station_list()
    information=stations_highest_rel_level(stations,10)
    print(information)
    for i in information:
        print(i.name,i.typical_range[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
