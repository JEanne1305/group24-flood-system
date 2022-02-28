import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    tol=0.8
    station_list=stations_level_over_threshold(stations, tol)
    sorted_station_list=sorted_by_key(station_list, 1)
    sorted_station_list.reverse()
    # 5 stations with the greatest current water level
    stations_name_to_fit=[]
    for i in sorted_station_list[1:6]: # exclude letcombe bassett
        stations_name_to_fit.append(i[0])

    print(stations_name_to_fit)

    for i in stations_name_to_fit:
        find_station=None
        for station in stations:
            if station.name==i:
                find_station=station
        print(type(find_station), find_station.name)
        dt=2
        dates, levels = fetch_measure_levels(find_station.measure_id, dt=datetime.timedelta(days=dt))
        #print(dates, levels)
        p=4
        plot_water_level_with_fit(find_station, dates, levels, p)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()