import matplotlib.pyplot as plt
import numpy as np

# Data for the years 2010 to 2020
years = np.arange(2010, 2021)

# Hypothetical average temperature data in Celsius
average_temperatures = [14.5, 14.6, 14.7, 14.9, 15.0, 15.2, 15.3, 15.5, 15.7, 15.9, 16.1]

# Hypothetical ice cream consumption in liters per capita
ice_cream_consumption = [6.5, 6.6, 6.8, 7.0, 7.2, 7.4, 7.7, 8.0, 8.3, 8.7, 9.1]

# Hypothetical average monthly ice cream sales (in thousands)
monthly_sales = [550, 560, 580, 610, 640, 670, 710, 750, 800, 860, 920]

# Hypothetical average monthly sunlight hours
monthly_sunlight_hours = [2100, 2150, 2180, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2600]

# Error values for ice cream consumption
error_values = [0.2, 0.3, 0.25, 0.3, 0.35, 0.3, 0.25, 0.35, 0.4, 0.45, 0.5]

fig, ax = plt.subplots(figsize=(14, 9))

# Line plot with error bars
ax.errorbar(years, ice_cream_consumption, yerr=error_values, fmt='-o', color='#ff6347', 
            ecolor='lightgray', elinewidth=2, capsize=5, label='Ice Cream Consumption (Liters per Capita)', alpha=0.8)

# Annotating temperature
for i, temp in enumerate(average_temperatures):
    ax.annotate(f'{temp}°C', (years[i], ice_cream_consumption[i]), textcoords="offset points",
                xytext=(-10, 10), ha='center', fontsize=9, color='darkblue')

# Scatter plot for monthly sales
ax.scatter(years, monthly_sales, color='green', label='Avg Monthly Sales (Thousands)', s=100, alpha=0.6)

# Secondary y-axis for temperature
ax_secondary = ax.twinx()
ax_secondary.plot(years, monthly_sunlight_hours, color='orange', linestyle='--', marker='s', label='Avg Monthly Sunlight Hours')
ax_secondary.set_ylabel('Avg Monthly Sunlight Hours', fontsize=12, color='orange')
ax_secondary.set_yticks([])

# Titles and labels
ax.set_title('Climate & Confectioneries: Ice Cream Consumption & Related Factors (2010-2020)',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Ice Cream Consumption (Liters per Capita)', fontsize=12)

# Grid and layout adjustment
ax.grid(visible=True, linestyle='--', alpha=0.5)
fig.tight_layout()

# Legends
lines_labels = [ax.get_legend_handles_labels(), ax_secondary.get_legend_handles_labels()]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax.legend(lines, labels, loc='upper left', fontsize=10)

# Display the plot
plt.show()