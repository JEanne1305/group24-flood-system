from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    stations=build_station_list()
    print("111")
    
    N=7
    print(rivers_by_station_number(stations,N))

if __name__=="__main__":
    run()

print("ggg")
