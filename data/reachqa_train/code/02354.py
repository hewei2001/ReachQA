import matplotlib.pyplot as plt
import numpy as np

# Define the years and extend the range
years = np.arange(2010, 2023)

# Data for the number of bikers, cyclists, pedestrians, and public transit users (in thousands)
bikers = [8, 10, 12, 15, 18, 22, 28, 35, 40, 45, 50, 60, 70]
cyclists = [5, 6, 8, 10, 13, 15, 20, 25, 30, 35, 38, 40, 42]
pedestrians = [50, 52, 53, 55, 56, 58, 60, 62, 64, 66, 67, 68, 70]
transit_users = [30, 32, 34, 36, 38, 40, 43, 45, 46, 48, 49, 50, 52]

# CO2 emissions data for secondary y-axis (in million tons)
co2_emissions = [180, 175, 170, 165, 162, 160, 158, 155, 153, 150, 147, 145, 140]

# Create the line chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the lines for different transport modes
ax1.plot(years, bikers, marker='o', color='seagreen', linestyle='-', linewidth=2.5, markersize=8, label='Bikers')
ax1.plot(years, cyclists, marker='s', color='darkorange', linestyle='--', linewidth=2.5, markersize=8, label='Cyclists')
ax1.plot(years, pedestrians, marker='^', color='royalblue', linestyle='-.', linewidth=2.5, markersize=8, label='Pedestrians')
ax1.plot(years, transit_users, marker='d', color='crimson', linestyle=':', linewidth=2.5, markersize=8, label='Public Transit')

# Annotate significant points on one line to avoid clutter
for i, value in enumerate(bikers):
    ax1.text(years[i], value + 2, f"{value}k", ha='center', fontsize=9, color='darkgreen')

# Secondary y-axis for CO2 emissions
ax2 = ax1.twinx()
ax2.plot(years, co2_emissions, marker='x', color='gray', linestyle='-', linewidth=2, markersize=8, label='CO2 Emissions')

# Titles and labels
ax1.set_title('Trends in UrbanVille Transport Modes (2010-2022)\nImpact of Climate Change Awareness and CO2 Reduction',
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of People (Thousands)', fontsize=14)
ax2.set_ylabel('CO2 Emissions (Million Tons)', fontsize=14, color='gray')

# Add a legend and adjust for clarity
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12, frameon=False)

# Customize grid and layout
ax1.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years)
ax1.set_yticks(np.arange(0, 80, 10))
ax2.set_yticks(np.arange(130, 200, 10))
fig.tight_layout()

# Display the chart
plt.show()