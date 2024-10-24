import matplotlib.pyplot as plt
import numpy as np

# Data generation
years = np.arange(2013, 2023)
energy_consumption = np.array([145, 155, 165, 150, 160, 170, 185, 195, 205, 200])
uncertainty = np.array([4, 5, 7, 6, 5, 8, 6, 7, 5, 6])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the line chart with error bars
ax.errorbar(years, energy_consumption, yerr=uncertainty, fmt='-o', 
            color='mediumseagreen', ecolor='lightgray', elinewidth=3, capsize=5, 
            markerfacecolor='white', label='Energy Consumption (with uncertainty)')

# Adding plot details
ax.set_title("Annual Energy Consumption Trends in Tech Companies\nwith Measurement Uncertainty", 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (GWh)', fontsize=12)
ax.legend(loc='upper left', fontsize=10)

# Annotate key points to highlight
ax.annotate('Peak in 2021', xy=(2021, 205), xytext=(2018, 215),
            arrowprops=dict(facecolor='black', shrink=0.05, lw=0.5),
            fontsize=10, color='darkred')
ax.annotate('Notable Drop', xy=(2015, 150), xytext=(2013, 140),
            arrowprops=dict(facecolor='black', shrink=0.05, lw=0.5),
            fontsize=10, color='darkblue')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Ensure all elements fit within the plot
plt.tight_layout()

# Display the plot
plt.show()