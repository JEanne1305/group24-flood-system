import datetime
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import numpy as np



#Task 2E Jeanne
#data about dates and levels:

<<<<<<< HEAD
'''
for date, level in zip(dates, levels):
    t.append(date)
    level.append(level)
'''

=======
    
>>>>>>> b759fc3c542324c8e2fbcea1592b595d4bd156da
# Plot
def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);

    
    plt.title(station.name)

    #add lines of typical high and low levels
    typ_high=station.typical_range[1]
    typ_low=station.typical_range[0]
    print(typ_high)
    print('233')
    plt.plot(typ_low, dates, label="typical low")
    plt.plot(typ_high, dates, label="typical high")

# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

<<<<<<< HEAD

# Task 2F: function fitting
# Yuqing Xue (yx357)

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly, d0=polyfit(dates, levels, p)
    plt.plot(dates, levels, '.', label='measured data')
    x1=np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1-x[0]), label='polyfit')
    plt.axhline(y=station.typical_range[0], color='g', linestyle='-', label='typical low range')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-', label='typical high range')
    plt.title(station.name)
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel('Water level [m]')
    plt.legend()
    plt.show()
=======
>>>>>>> b759fc3c542324c8e2fbcea1592b595d4bd156da
