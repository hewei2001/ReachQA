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

# Calculate average yearly temperature for overlay line plot
average_yearly_temp = [np.mean([temperature_data[season][i] for season in seasons]) for i in range(len(years))]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Convert dictionary data into a list of arrays for stacked area plotting
data = np.row_stack(list(temperature_data.values()))

# Create stacked area plot
ax.stackplot(years, data, labels=seasons, colors=colors, alpha=0.8)

# Overlay the average yearly temperature line plot
ax.plot(years, average_yearly_temp, color='darkblue', linewidth=2.5, marker='o', label='Yearly Average')

# Titles and labels
ax.set_title('Seasonal Temperature Trends in Climatia (2015-2022)', fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Temperature (°C)', fontsize=12)

# Customize grid and legend
ax.grid(visible=True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Seasons', fontsize=10, frameon=False)

# Add annotations for peaks
peak_year_summer = np.argmax(temperature_data['Summer'])
ax.annotate('Peak Summer', xy=(years[peak_year_summer], temperature_data['Summer'][peak_year_summer]),
            xytext=(years[peak_year_summer] + 0.3, temperature_data['Summer'][peak_year_summer] + 2),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()