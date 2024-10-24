import numpy as np
import matplotlib.pyplot as plt

# Extend the time range and increase data points by using monthly intervals
years = np.arange(2020, 2030, 0.5)

# Create complex non-linear growth patterns for each forest type
rainforest = 15 + 10 * np.sin(0.3 * np.pi * (years - 2020))
deciduous = 45 - 5 * np.log1p(years - 2020)
coniferous = 40 + 3 * np.cos(0.4 * np.pi * (years - 2020))
boreal = 20 + 5 * np.tanh(0.2 * (years - 2020))
tropical_dry = 25 - 4 * np.exp(-0.1 * (years - 2020))

# Ensure the total percentage remains at 100%
total_percentage = rainforest + deciduous + coniferous + boreal + tropical_dry
rainforest = (rainforest / total_percentage) * 100
deciduous = (deciduous / total_percentage) * 100
coniferous = (coniferous / total_percentage) * 100
boreal = (boreal / total_percentage) * 100
tropical_dry = (tropical_dry / total_percentage) * 100

# Stack the data for the stacked area plot
stacked_data = np.vstack([rainforest, deciduous, coniferous, boreal, tropical_dry])

# Initialize the plot
plt.figure(figsize=(14, 10))

# Create the stacked area chart
plt.stackplot(years, stacked_data, labels=['Rainforest', 'Deciduous', 'Coniferous', 'Boreal', 'Tropical Dry'], 
              colors=['#2ca02c', '#ff7f0e', '#1f77b4', '#9467bd', '#8c564b'], alpha=0.8)

# Add title, labels, and a legend
plt.title("Dynamic Changes in Forest Composition\nEmerald Woods National Park (2020-2029)", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage of Total Area Covered", fontsize=14)
plt.legend(loc='upper left', fontsize=12, title='Forest Types')

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Annotate significant inflection points
plt.annotate('Ecological Shift', xy=(2024, 50), xytext=(2022, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()