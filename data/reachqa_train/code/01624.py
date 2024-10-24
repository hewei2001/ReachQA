import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Transportation mode usage data (as percentages of total transport usage)
bicycles = np.array([5, 7, 10, 13, 17, 22, 27, 33, 40, 48, 55])
electric_vehicles = np.array([2, 3, 5, 8, 13, 20, 30, 45, 65, 85, 100])
public_transport = np.array([20, 22, 25, 27, 28, 30, 32, 35, 38, 40, 42])
traditional_cars = np.array([73, 68, 60, 52, 42, 28, 11, 7, 5, 2, 3])

# Hypothetical emissions reduction data (as percentages from a baseline year)
emissions_reduction = np.array([1, 3, 5, 9, 15, 25, 35, 50, 65, 75, 85])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Define color palette for each transportation mode
colors = ['#6a51a3', '#3182bd', '#31a354', '#de2d26']

# Create stacked area plot
ax1.stackplot(years, bicycles, electric_vehicles, public_transport, traditional_cars,
              labels=['Bicycles', 'Electric Vehicles', 'Public Transport', 'Traditional Cars'],
              colors=colors, alpha=0.8)

# Title and axis labels
ax1.set_title('GreenCity Transportation Evolution (2010-2020)\nTransition Towards Sustainability',
              fontsize=16, fontweight='bold', linespacing=1.5)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Percentage of Total Usage', fontsize=14)

# Create a second y-axis for the emissions reduction line plot
ax2 = ax1.twinx()
ax2.plot(years, emissions_reduction, color='black', linestyle='--', marker='o', linewidth=2, label='Emissions Reduction (%)')
ax2.set_ylabel('Emissions Reduction (%)', fontsize=14, color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Adjust layout to prevent overlap and ensure readability
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# Add a legend with a title for both plots
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, title='Transportation Mode and Emissions', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=12)

# Add gridlines for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.show()