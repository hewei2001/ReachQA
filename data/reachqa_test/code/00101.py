import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for electric vehicles and charging stations
years = np.array([2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060])
evs = np.array([10, 18, 29, 35, 47, 58, 65, 80, 90, 100, 120])  # in thousands
charging_stations = np.array([5, 8, 12, 18, 25, 30, 40, 50, 60, 70, 80])

# Related data for EV adoption percentage
total_vehicles = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])  # in thousands
ev_adoption_percentage = (evs / total_vehicles) * 100

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('EV Adoption and Infrastructure Development (2050-2060)', fontsize=16, weight='bold')

# First subplot: Scatter plot with interpolation
ax1.scatter(evs, charging_stations, color='blue', edgecolor='black', s=100, label='Data Points')
x_smooth = np.linspace(evs.min(), evs.max(), 300)
spl = make_interp_spline(evs, charging_stations, k=3)
y_smooth = spl(x_smooth)
ax1.plot(x_smooth, y_smooth, color='green', linestyle='--', linewidth=2, label='Smooth Fit')
ax1.set_xlabel('Number of Electric Vehicles (in thousands)', fontsize=10)
ax1.set_ylabel('Number of Charging Stations', fontsize=10)
ax1.set_title('EVs vs Charging Stations', fontsize=12, weight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
for year, ev, station in zip(years, evs, charging_stations):
    ax1.annotate(f'{year}', (ev, station), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=8)

# Second subplot: Bar chart for EV adoption percentage
ax2.bar(years, ev_adoption_percentage, color='orange', edgecolor='black')
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('EV Adoption (%)', fontsize=10)
ax2.set_title('EV Adoption Percentage', fontsize=12, weight='bold')
ax2.set_ylim(0, max(ev_adoption_percentage) + 5)
for year, adoption in zip(years, ev_adoption_percentage):
    ax2.text(year, adoption + 0.5, f'{adoption:.1f}%', ha='center', va='bottom', fontsize=8)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plots
plt.show()