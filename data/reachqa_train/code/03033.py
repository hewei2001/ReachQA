import matplotlib.pyplot as plt
import numpy as np

# Define the data for years and average solar power generation
years = np.arange(2000, 2024)
average_output = np.array([
    150, 160, 170, 180, 195, 210, 225, 245, 265, 285,
    310, 335, 360, 385, 410, 440, 470, 500, 540, 580, 
    630, 680, 740, 800
])
errors = np.array([
    10, 12, 10, 13, 15, 18, 20, 22, 25, 20,
    18, 17, 15, 20, 22, 25, 30, 28, 27, 29,
    35, 32, 30, 34
])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot with error bars
ax.errorbar(years, average_output, yerr=errors, fmt='-o', 
            color='#1f77b4', ecolor='lightgray', elinewidth=2.5, capsize=5,
            label='Average Monthly Output', alpha=0.8)

# Customizing plot appearance
ax.set_title("Trends in Solar Power Generation\nwith Uncertainty Estimates (2000-2023)", 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Avg. Monthly Solar Output (GWh)', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.6)

# Set x-ticks to show every other year to avoid clutter
ax.set_xticks(years[::2])

# Ensure all data points are clearly visible
ax.set_xlim(years[0] - 1, years[-1] + 1)
ax.set_ylim(100, max(average_output + errors) + 50)

# Add a legend
ax.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()