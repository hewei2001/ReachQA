import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy output in GWh for each type of turbine
offshore_output = np.array([120, 125, 130, 133, 135, 140, 142, 145, 150, 152, 155])
onshore_output = np.array([80, 83, 85, 90, 92, 95, 98, 101, 105, 108, 110])
hybrid_output = np.array([50, 60, 65, 72, 85, 90, 100, 110, 120, 130, 140])

# Plotting
plt.figure(figsize=(12, 7))

plt.plot(years, offshore_output, marker='o', label='Offshore Turbine', linestyle='-', linewidth=2, color='b')
plt.plot(years, onshore_output, marker='s', label='Onshore Turbine', linestyle='--', linewidth=2, color='g')
plt.plot(years, hybrid_output, marker='^', label='Hybrid Turbine', linestyle='-.', linewidth=2, color='r')

# Chart details
plt.title('Decade of Progress: EcoPower Co. Wind Turbine Performance\n(2010-2020)', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Output (GWh)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(50, 161, 10))

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', fontsize=10, title='Turbine Type', title_fontsize='13')

# Highlight a specific point on the line (for example, maximum output in 2020)
max_output_year = years[-1]
plt.annotate('Max Offshore Output',
             xy=(max_output_year, offshore_output[-1]), 
             xytext=(max_output_year - 3, offshore_output[-1] + 10),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=10, color='blue')

# Layout adjustment
plt.tight_layout()

# Display the chart
plt.show()