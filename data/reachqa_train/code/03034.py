import matplotlib.pyplot as plt
import numpy as np

# Original data for solar power generation
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

# Additional data for sunlight hours (hypothetical)
sunlight_hours = np.array([
    2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650,
    2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150,
    3200, 3250, 3300, 3350
])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot with error bars for solar output
ax1.errorbar(years, average_output, yerr=errors, fmt='-o', 
             color='#1f77b4', ecolor='lightgray', elinewidth=2.5, capsize=5,
             label='Average Monthly Output', alpha=0.8)

# Customizing the primary y-axis
ax1.set_title("Trends in Solar Power Generation and Sunlight Hours\nwith Uncertainty Estimates (2000-2023)", 
              fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Avg. Monthly Solar Output (GWh)', fontsize=14, color='#1f77b4')
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(years[::2])
ax1.set_xlim(years[0] - 1, years[-1] + 1)
ax1.set_ylim(100, max(average_output + errors) + 50)

# Add a legend for the solar output
ax1.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)

# Create a secondary y-axis for sunlight hours
ax2 = ax1.twinx()
ax2.bar(years, sunlight_hours, alpha=0.4, color='orange', label='Avg. Sunlight Hours')
ax2.set_ylabel('Avg. Sunlight Hours', fontsize=14, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(2000, max(sunlight_hours) + 400)

# Add a legend for the sunlight hours
ax2.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)

# Ensure the layout is tight and labels don't overlap
plt.tight_layout()

# Show the chart
plt.show()