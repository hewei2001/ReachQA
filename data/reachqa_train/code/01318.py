import matplotlib.pyplot as plt
import numpy as np

# Define the years for the timeline
years = np.arange(2010, 2024)

# Define fictional mission data for each space agency
nasa_missions = np.array([10, 12, 15, 13, 16, 18, 20, 22, 25, 28, 30, 32, 35, 37])
esa_missions = np.array([5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22])
cnsa_missions = np.array([2, 3, 5, 7, 9, 12, 15, 17, 20, 24, 28, 30, 32, 34])
isro_missions = np.array([1, 2, 3, 4, 5, 7, 9, 11, 14, 16, 18, 20, 23, 25])

# Calculate total missions each year
total_missions = nasa_missions + esa_missions + cnsa_missions + isro_missions

# Create a new figure
fig, ax = plt.subplots(figsize=(14, 8))
secondary_ax = ax.twinx()

# Plot the data with different styles for each agency
ax.plot(years, nasa_missions, '-o', color='blue', label='NASA', linewidth=2, markersize=6)
ax.plot(years, esa_missions, '-s', color='green', label='ESA', linewidth=2, markersize=6)
ax.plot(years, cnsa_missions, '-^', color='red', label='CNSA', linewidth=2, markersize=6)
ax.plot(years, isro_missions, '-d', color='purple', label='ISRO', linewidth=2, markersize=6)

# Plot total missions on secondary axis
secondary_ax.plot(years, total_missions, 'o-', color='gray', label='Total Missions', linewidth=1, markersize=4, linestyle='dashed')
secondary_ax.set_ylabel("Total Missions", fontsize=12)

# Set chart title and labels
ax.set_title("Annual Space Exploration Missions\nBy Major Agencies (2010-2023)", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Missions", fontsize=12)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.5)

# Add shaded areas for milestone years
ax.fill_between(years, 0, nasa_missions, color='blue', alpha=0.1)
ax.fill_between(years, 0, esa_missions, color='green', alpha=0.1)
ax.fill_between(years, 0, cnsa_missions, color='red', alpha=0.1)
ax.fill_between(years, 0, isro_missions, color='purple', alpha=0.1)

# Add annotations for key milestones
ax.annotate('Record Missions',
            xy=(2023, 37), xytext=(2020, 40),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center', backgroundcolor='white')

# Customize ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.set_tick_params(labelsize=10)
secondary_ax.yaxis.set_tick_params(labelsize=10, colors='gray')

# Add a legend with enhanced information
ax.legend(title="Space Agencies", fontsize=10, loc='upper left')
secondary_ax.legend(fontsize=10, loc='upper right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()