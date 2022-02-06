# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


# Test 1F: inconsistent typical range stations
# Yuqing Xue (yx357)
def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    inconsistency=inconsistent_typical_range_stations(stations)
    inconsistency.sort()
    for i in inconsistency:
        for station in stations:
            if i==station.name:
                assert station.typical_range==None or station.typical_range[0]>station.typical_range[1]
                # check that every station in the "inconsistency" list have an empty range or the range is inconsistent

