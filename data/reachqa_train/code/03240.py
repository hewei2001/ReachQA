import numpy as np
import matplotlib.pyplot as plt

# Years spanning the period from 2010 to 2020
years = np.arange(2010, 2021)

# Population data for different marine life forms (in millions)
coral_reefs_population = np.array([55, 54, 50, 48, 47, 46, 45, 44, 43, 41, 40])
fish_population = np.array([100, 102, 105, 108, 110, 112, 114, 116, 118, 119, 120])
marine_mammals_population = np.array([15, 15, 16, 17, 18, 18, 19, 19, 20, 21, 21])

# Create the plot
plt.figure(figsize=(12, 7))

# Use stackplot to plot cumulative data
plt.stackplot(years, coral_reefs_population, fish_population, marine_mammals_population,
              labels=['Coral Reefs', 'Fish', 'Marine Mammals'],
              colors=['#FFA07A', '#87CEEB', '#3CB371'], alpha=0.7)

# Adding labels, title, and legend
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Population (millions)', fontsize=12, fontweight='bold')
plt.title('Ocean Life Dynamics:\nA Decade of Change in Marine Populations', fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper left', title='Marine Species', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Add gridlines to improve readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent text clipping
plt.tight_layout()

# Display the plot
plt.show()