import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Define the average sea surface temperatures in degrees Celsius
sst_data = [16.1, 16.3, 16.5, 16.6, 16.8, 17.1, 17.3, 17.6, 17.8, 18.0, 18.3]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the line with markers
ax.plot(years, sst_data, marker='o', linestyle='-', color='navy', linewidth=2, markersize=6, label='SST')

# Add annotations for key data points
for year, sst in zip(years, sst_data):
    ax.annotate(f'{sst}°C', 
                xy=(year, sst), 
                xytext=(0, 10), 
                textcoords='offset points',
                fontsize=9,
                ha='center',
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Set the title with line breaks for better readability
ax.set_title('Decadal Sea Surface Temperature Changes\n(2010-2020)', fontsize=14, fontweight='bold', pad=15)

# Label the x-axis and y-axis
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Sea Surface Temperature (°C)', fontsize=12)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()