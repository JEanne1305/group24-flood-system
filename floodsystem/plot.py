import datetime
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta




#Task 2E Jeanne
#data about dates and levels:

    
for date, level in zip(dates, levels):
    t.append(date)
    level.append(level)


# Plot
def plot_water_levels(station, dates, levels):
    
    plt.plot(t, level)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);

    
    plt.title(station.name)

    #add lines of typical high and low levels
    typ_high=station.typical_range[1]
    typ_low=station.typical_range[0]
    plt.plot(typ_low, t, label="typical low")
    plt.plot(typ_high, t, label="typical high")

# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
