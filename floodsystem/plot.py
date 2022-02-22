#Task 2E Jeanne

import datetime
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta



t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

# Plot
def plot_water_levels(station, dates, levels):
    t=[]
    level=[]
    dt = 10
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
    
    for date, level in zip(dates, levels):
        t.append(date)
        level.append(level)

    plt.plot(t, level)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);

    name=station.name
    plt.title(name)

    #add lines of typical high and low levels
    typ_high=station.typical_range[1]
    typ_low=station.typical_range[0]
    plt.plot(typ_low, t, label="typical low")
    plt.plot(typ_high, t, label="typical high")

# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
