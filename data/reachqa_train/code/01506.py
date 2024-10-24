import matplotlib.pyplot as plt
import numpy as np

# Define years and seasons
years = np.arange(2015, 2023)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# Average temperature data (in Celsius) for each season over the years
temperature_data = {
    'Spring': [12, 13, 14, 13, 15, 15, 16, 16],
    'Summer': [25, 26, 27, 28, 27, 29, 30, 31],
    'Fall': [14, 14, 13, 15, 16, 16, 15, 14],
    'Winter': [5, 4, 5, 6, 5, 6, 7, 8]
}

# Colors for each season
colors = ['#FFB6C1', '#FFD700', '#90EE90', '#ADD8E6']

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Convert dictionary data into a list of arrays for stacked area plotting
data = np.row_stack(list(temperature_data.values()))

# Create stacked area plot
ax.stackplot(years, data, labels=seasons, colors=colors, alpha=0.8)

# Titles and labels
ax.set_title('Seasonal Temperature Trends in Climatia (2015-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Temperature (°C)', fontsize=12)

# Customize grid and legend
ax.grid(visible=True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Seasons', fontsize=10)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()