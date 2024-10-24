import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Transportation mode usage data (as percentages of total transport usage)
bicycles = np.array([5, 7, 10, 13, 17, 22, 27, 33, 40, 48, 55])
electric_vehicles = np.array([2, 3, 5, 8, 13, 20, 30, 45, 65, 85, 100])
public_transport = np.array([20, 22, 25, 27, 28, 30, 32, 35, 38, 40, 42])
traditional_cars = np.array([73, 68, 60, 52, 42, 28, 11, 7, 5, 2, 3])

# Create the figure and axis
plt.figure(figsize=(14, 8))

# Define color palette for each transportation mode
colors = ['#6a51a3', '#3182bd', '#31a354', '#de2d26']

# Create stacked area plot
plt.stackplot(years, bicycles, electric_vehicles, public_transport, traditional_cars,
              labels=['Bicycles', 'Electric Vehicles', 'Public Transport', 'Traditional Cars'],
              colors=colors, alpha=0.8)

# Title and axis labels
plt.title('GreenCity Transportation Evolution (2010-2020)\nTransition Towards Sustainability', 
          fontsize=16, fontweight='bold', linespacing=1.5)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Percentage of Total Usage', fontsize=14)

# Add a legend with a title
plt.legend(title='Transportation Mode', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=12)

# Add gridlines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()