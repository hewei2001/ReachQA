import matplotlib.pyplot as plt
import numpy as np

# Define the years and regions
years = np.arange(2000, 2021)

# Data: Renewable energy capacity increase (in GW) for each region over the years
north_america_growth = [5, 7, 8, 10, 12, 15, 17, 20, 22, 25, 28, 30, 33, 36, 39, 42, 46, 50, 53, 57, 60]
europe_growth = [6, 9, 12, 15, 18, 21, 24, 28, 32, 35, 39, 43, 47, 50, 54, 58, 62, 67, 72, 78, 85]
asia_pacific_growth = [10, 13, 16, 20, 25, 30, 36, 42, 49, 57, 66, 75, 85, 96, 108, 121, 135, 150, 166, 183, 201]
africa_growth = [1, 2, 3, 3, 4, 5, 6, 7, 9, 11, 13, 16, 19, 22, 25, 29, 34, 39, 44, 50, 57]

# Calculate total capacity growth for each year
total_growth = [sum(x) for x in zip(north_america_growth, europe_growth, asia_pacific_growth, africa_growth)]

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Line plots for each region
ax1.plot(years, north_america_growth, label='North America', marker='o', linestyle='-', linewidth=2, color='blue')
ax1.plot(years, europe_growth, label='Europe', marker='s', linestyle='--', linewidth=2, color='green')
ax1.plot(years, asia_pacific_growth, label='Asia-Pacific', marker='^', linestyle='-.', linewidth=2, color='orange')
ax1.plot(years, africa_growth, label='Africa', marker='D', linestyle=':', linewidth=2, color='red')

# Twin axis for bar chart
ax2 = ax1.twinx()
ax2.bar(years, total_growth, alpha=0.2, color='grey', label='Total Capacity Growth')

# Annotate specific years with events
annotations = [
    (2005, asia_pacific_growth[5], "Kyoto Protocol\nImplementation"),
    (2010, europe_growth[10], "EU Renewable\nDirective"),
    (2015, africa_growth[15], "Paris\nAgreement"),
    (2020, north_america_growth[20], "Green Deal\nInitiatives")
]
for year, value, note in annotations:
    ax1.annotate(note, (year, value), textcoords="offset points", xytext=(0,10), ha='center',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

# Titles and labels
ax1.set_title("Renewable Energy Capacity Growth (2000-2020)\nA Journey Towards Sustainable Energy", fontsize=18, pad=30)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Capacity Increase (GW) by Region', fontsize=14)
ax2.set_ylabel('Total Capacity Increase (GW)', fontsize=14)

# Grids and legends
ax1.grid(True, linestyle='--', which='both', color='grey', alpha=0.6)
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Customize ticks
plt.xticks(years[::2], rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()