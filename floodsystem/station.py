# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Task 1F: add a method to check data consistency
    # Yuqing Xue (yx357)
    def typical_range_consistent(self):
        if self.typical_range==None or self.typical_range[0]>self.typical_range[1]:
            #print(self. name, self.typical_range)
            return False
        else:
            return True

    # Task 2B: return the latest water level as a fraction of the typical range
    # Yuqing Xue (yx357)
    def relative_water_level(self):
        if self.typical_range!=None or self.typical_range[0]<=self.typical_range[1]:
            fraction=(self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            return fraction
        else:
            return None

# Task 1F: implement the submodule inconsistent_typical_range_stations
# Yuqing Xue (yx357)
def inconsistent_typical_range_stations(stations):
    inconsistent_stations_list=[]
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) is False:
            inconsistent_stations_list.append(station.name) 
    return inconsistent_stations_list
