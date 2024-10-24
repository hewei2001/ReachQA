import matplotlib.pyplot as plt
import numpy as np

# Define the years for the timeline
years = np.arange(2010, 2024)

# Define fictional mission data for each space agency
nasa_missions = np.array([10, 12, 15, 13, 16, 18, 20, 22, 25, 28, 30, 32, 35, 37])
esa_missions = np.array([5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22])
cnsa_missions = np.array([2, 3, 5, 7, 9, 12, 15, 17, 20, 24, 28, 30, 32, 34])
isro_missions = np.array([1, 2, 3, 4, 5, 7, 9, 11, 14, 16, 18, 20, 23, 25])

# Create a new figure for the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the data with different styles for each agency
ax.plot(years, nasa_missions, '-o', color='blue', label='NASA', linewidth=2, markersize=6)
ax.plot(years, esa_missions, '-s', color='green', label='ESA', linewidth=2, markersize=6)
ax.plot(years, cnsa_missions, '-^', color='red', label='CNSA', linewidth=2, markersize=6)
ax.plot(years, isro_missions, '-d', color='purple', label='ISRO', linewidth=2, markersize=6)

# Set the chart title and labels
ax.set_title("Annual Space Exploration Missions\n(2010-2023)", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Missions", fontsize=12)

# Add gridlines and customize ticks
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.set_tick_params(labelsize=10)

# Add a legend to the chart
ax.legend(title="Space Agencies", fontsize=10, loc='upper left')

# Add annotation for the highest point of NASA's missions
ax.annotate('Record Missions',
            xy=(2023, 37), xytext=(2020, 38),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, ha='center', backgroundcolor='white')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()