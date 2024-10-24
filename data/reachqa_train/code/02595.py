import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Transportation mode adoption percentages
public_transportation = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
electric_vehicles = [2, 3, 5, 8, 12, 18, 25, 32, 40, 50, 60]
bicycles = [10, 11, 12, 13, 15, 18, 22, 27, 33, 40, 48]
walking = [8, 9, 9, 10, 11, 12, 13, 13, 14, 15, 16]

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Stack the data
ax.stackplot(years, public_transportation, electric_vehicles, bicycles, walking, 
             labels=['Public Transportation', 'Electric Vehicles', 'Bicycles', 'Walking'], 
             colors=['#2a9d8f', '#e9c46a', '#f4a261', '#e76f51'], alpha=0.8)

# Add titles and labels
ax.set_title('The Rise of Sustainable Transportation\nSolutions from 2010 to 2020', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=10, title='Transport Modes', title_fontsize='11')

# Enhance readability with grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()