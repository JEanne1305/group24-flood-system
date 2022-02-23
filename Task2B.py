from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    tol=0.8
    station_list=stations_level_over_threshold(stations, tol)
    sorted_station_list=sorted_by_key(station_list, 1)
    sorted_station_list.reverse()
    for i in sorted_station_list:
        print(i[0], i[1])




if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()