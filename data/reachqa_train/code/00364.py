import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2015, 2024)

# Data: Electric vehicle sales in thousands for 6 cities
ev_sales = np.array([
    [5, 8, 12, 16, 22, 29, 35, 42, 50],   # New York
    [4, 7, 10, 15, 20, 28, 38, 45, 55],   # London
    [6, 9, 14, 18, 25, 33, 41, 49, 60],   # Tokyo
    [3, 6, 9, 13, 19, 26, 34, 44, 54],    # Paris
    [5, 10, 15, 21, 30, 38, 48, 58, 70],  # Beijing
    [7, 12, 17, 23, 32, 42, 53, 65, 78]   # Los Angeles
])

# Non-linear growth model using exponential growth to simulate complexity
battery_capacities = np.array([
    100 * np.exp(0.05 * np.arange(9)),    # New York
    95 * np.exp(0.06 * np.arange(9)),     # London
    90 * np.exp(0.045 * np.arange(9)),    # Tokyo
    110 * np.exp(0.047 * np.arange(9)),   # Paris
    105 * np.exp(0.052 * np.arange(9)),   # Beijing
    115 * np.exp(0.049 * np.arange(9))    # Los Angeles
])

# City names for legend
cities = ["New York", "London", "Tokyo", "Paris", "Beijing", "Los Angeles"]

# Colors and markers for the line plots
styles = [{'color': '#FF5733', 'marker': 'o'}, 
          {'color': '#33FF57', 'marker': 's'}, 
          {'color': '#3357FF', 'marker': '^'},
          {'color': '#FF33A1', 'marker': 'd'},
          {'color': '#33FFF5', 'marker': 'x'},
          {'color': '#FF9633', 'marker': 'v'}]

# Create the plot with subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 12), constrained_layout=True)

# Plot EV Sales
for idx, city in enumerate(cities):
    axs[0].plot(years, ev_sales[idx], label=city,
                color=styles[idx]['color'], marker=styles[idx]['marker'],
                markersize=6, linewidth=2, alpha=0.9)

axs[0].set_title("Electric Vehicle Sales (2015-2023)\nAcross Major Cities", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("EV Sales (thousands)", fontsize=12)
axs[0].set_xticks(years)
axs[0].legend(title="City", fontsize=10, loc='upper left', frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Plot Battery Capacity Growth
for idx, city in enumerate(cities):
    axs[1].plot(years, battery_capacities[idx], label=f"{city} Battery",
                color=styles[idx]['color'], linestyle='--', linewidth=2)

axs[1].set_title("Growth in Average Battery Capacity\nof Electric Vehicles (2015-2023)", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Battery Capacity (kWh)", fontsize=12)
axs[1].set_xticks(years)
axs[1].legend(title="City", fontsize=10, loc='upper left', frameon=False)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Display the plot
plt.show()