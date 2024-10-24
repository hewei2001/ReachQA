import matplotlib.pyplot as plt
import numpy as np

# Data for the years 2010 to 2020
years = np.arange(2010, 2021)

# Hypothetical average temperature data in Celsius
average_temperatures = [14.5, 14.6, 14.7, 14.9, 15.0, 15.2, 15.3, 15.5, 15.7, 15.9, 16.1]

# Hypothetical ice cream consumption in liters per capita
ice_cream_consumption = [6.5, 6.6, 6.8, 7.0, 7.2, 7.4, 7.7, 8.0, 8.3, 8.7, 9.1]

# Define error values for ice cream consumption (reflecting variability)
error_values = [0.2, 0.3, 0.25, 0.3, 0.35, 0.3, 0.25, 0.35, 0.4, 0.45, 0.5]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the line with error bars
ax.errorbar(years, ice_cream_consumption, yerr=error_values, fmt='-o', color='#ff6347', 
            ecolor='lightgray', elinewidth=2, capsize=5, label='Ice Cream Consumption (Liters per Capita)',
            alpha=0.8)

# Annotate the line chart with average temperature values
for i in range(len(years)):
    ax.annotate(f'{average_temperatures[i]}°C', (years[i], ice_cream_consumption[i]), 
                textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color='darkblue')

# Set the title and labels
ax.set_title('A Sweet Consequence of Climate Change:\nIce Cream Consumption Trends (2010-2020)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Ice Cream Consumption (Liters per Capita)', fontsize=12)

# Add a secondary y-axis for temperature annotations
ax_secondary = ax.twinx()
ax_secondary.set_ylabel('Average Temperature (°C)', fontsize=12, color='darkblue')
ax_secondary.set_yticks([])  # Hide y-ticks for clarity

# Add grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.5)

# Show legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()