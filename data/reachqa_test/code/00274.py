import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data representing the percentage of urban area covered by green spaces
city_a_green_space = [5, 6, 7, 8, 10, 12, 13, 15, 17, 19, 21]  # Growth in City A
city_b_green_space = [8, 9, 11, 13, 15, 17, 18, 20, 23, 25, 28]  # Growth in City B
city_c_green_space = [7, 7.5, 8, 9, 11, 13, 15, 17, 19, 21, 24]  # Growth in City C

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Enhanced plotting with different line styles and markers
ax.plot(years, city_a_green_space, label='City A', color='#1f77b4', linewidth=2.5, marker='o', linestyle='-', markersize=8)
ax.plot(years, city_b_green_space, label='City B', color='#ff7f0e', linewidth=2.5, marker='s', linestyle='--', markersize=8)
ax.plot(years, city_c_green_space, label='City C', color='#2ca02c', linewidth=2.5, marker='^', linestyle='-.', markersize=8)

# Title with line breaks for better readability
ax.set_title('The Rise of Urban Green Spaces:\nA Decade of Growth in Major Cities', fontsize=16, fontweight='bold')

# Axis labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Green Space (% of Urban Area)', fontsize=12)

# Annotate key data points every two years
for i in range(len(years)):
    if i % 2 == 0:  # Annotate every two years
        ax.annotate(f'{city_a_green_space[i]}%', (years[i], city_a_green_space[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)
        ax.annotate(f'{city_b_green_space[i]}%', (years[i], city_b_green_space[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)
        ax.annotate(f'{city_c_green_space[i]}%', (years[i], city_c_green_space[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

# Adding a shaded background for the range of years
ax.axvspan(2014, 2016, color='grey', alpha=0.1, label="Policy Implementation Period")

# Add gridlines with increased opacity
ax.grid(True, alpha=0.5, linestyle='--')

# Improved legend with a border
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='grey', alpha=0.1, label='Policy Implementation Period'))
ax.legend(handles=handles, loc='upper left', title='Cities', frameon=True, fontsize=11)

# Set the x-axis ticks for years and adjust limits
ax.set_xticks(years)
ax.set_xlim([2010, 2020])
ax.set_ylim([0, 30])

# Use tight layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()