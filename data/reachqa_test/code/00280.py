import matplotlib.pyplot as plt
import numpy as np

# Data for environmental impact reduction initiatives (in thousand tons of CO₂ equivalent)
cities = ['New York', 'Tokyo', 'London', 'Berlin', 'Sydney']
recycling = np.array([30, 25, 28, 22, 20])
green_spaces = np.array([15, 20, 18, 25, 10])
public_transport = np.array([25, 30, 22, 28, 15])

# Construct cumulative impact data for the second subplot
# Example: Total reduction over a hypothetical time period, showing changes across years
years = np.array([2013, 2015, 2017, 2019, 2021])
total_reduction_ny = np.array([10, 20, 35, 50, 70])
total_reduction_tokyo = np.array([8, 16, 32, 45, 68])
total_reduction_london = np.array([12, 25, 38, 52, 74])
total_reduction_berlin = np.array([9, 19, 28, 42, 60])
total_reduction_sydney = np.array([7, 15, 25, 35, 55])

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [1, 1]})

# First subplot: Stacked Bar Chart
axs[0].bar(cities, recycling, label='Recycling Improvements', color='#76c7c0')
axs[0].bar(cities, green_spaces, bottom=recycling, label='Expansion of Green Spaces', color='#ffcc5c')
axs[0].bar(cities, public_transport, bottom=recycling + green_spaces, label='Public Transport & Cycling', color='#ff6f69')

axs[0].set_ylabel('Reduction in Environmental Impact\n(Thousand Tons of CO₂ Equiv.)', fontsize=12)
axs[0].set_title('Urban Environmental Initiatives:\nA Decade of Progress in Major Cities', fontsize=14, fontweight='bold')
axs[0].legend(title='Initiatives', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].tick_params(axis='x', rotation=45)

# Second subplot: Line Chart of Cumulative Impact Over Years
axs[1].plot(years, total_reduction_ny, marker='o', label='New York', color='#76c7c0')
axs[1].plot(years, total_reduction_tokyo, marker='s', label='Tokyo', color='#ffcc5c')
axs[1].plot(years, total_reduction_london, marker='^', label='London', color='#ff6f69')
axs[1].plot(years, total_reduction_berlin, marker='d', label='Berlin', color='#77dd77')
axs[1].plot(years, total_reduction_sydney, marker='x', label='Sydney', color='#f49ac2')

axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative CO₂ Reduction\n(Thousand Tons)', fontsize=12)
axs[1].set_title('Cumulative Impact Over Time:\nUrban Environmental Initiatives', fontsize=14, fontweight='bold')
axs[1].legend(title='Cities', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
axs[1].grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()