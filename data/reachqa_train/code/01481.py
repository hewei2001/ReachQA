import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Percentage of new buildings using sustainable materials each year
sustainable_percentage = np.array([5, 8, 12, 18, 26, 35, 42, 50, 60, 70, 80])

# Assume total buildings constructed each year (in thousands)
total_buildings = np.array([100, 110, 120, 135, 150, 160, 175, 190, 210, 230, 250])

# Create the main figure
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for sustainable percentage
bars = ax1.bar(years, sustainable_percentage, color='#76c7c0', edgecolor='black', label='Sustainable %')

# Annotate the bars with the percentage values
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkgreen')

# Axes labels and chart title
ax1.set_title('Sustainable Architecture: 2013-2023\nPercentage and Total New Buildings Constructed', fontsize=16, pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of New Buildings (%)', fontsize=12, color='#76c7c0')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.tick_params(axis='y', labelcolor='#76c7c0')

# Line plot for total number of buildings
ax2 = ax1.twinx()  # Create a secondary y-axis
ax2.plot(years, total_buildings, color='orange', marker='o', linestyle='-', linewidth=2, label='Total Buildings (k)')
ax2.set_ylabel('Total Buildings Constructed (thousands)', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_yticks(np.arange(100, 300, 25))

# Highlight certain milestones in the trend
ax1.axhline(y=50, color='gray', linestyle='--', linewidth=1)
ax1.text(years[0] - 0.7, 51, '50% Milestone', fontsize=10, color='gray')

ax1.axhline(y=75, color='gray', linestyle='--', linewidth=1)
ax1.text(years[0] - 0.7, 76, '75% Target', fontsize=10, color='gray')

# Add a legend that includes both plots
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85), fontsize=10, frameon=False)

# Improve layout to prevent overlap
fig.tight_layout()

# Display the chart
plt.show()