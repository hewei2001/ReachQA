import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2000, 2041)

# Artificial data for average ocean temperatures in different oceans (in Celsius)
atlantic_temperatures = 15 + 0.02 * (years - 2000) + 0.5 * np.sin(0.2 * (years - 2000))
pacific_temperatures = 16 + 0.018 * (years - 2000) + 0.3 * np.cos(0.2 * (years - 2000))
indian_temperatures = 15.5 + 0.022 * (years - 2000) + 0.4 * np.sin(0.2 * (years - 2000))

# Simulated measurement errors
measurement_errors = np.full_like(years, 0.15)

# Create the chart with subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data for each ocean with error bands
ax.fill_between(years, atlantic_temperatures - measurement_errors, atlantic_temperatures + measurement_errors, color='b', alpha=0.1)
ax.plot(years, atlantic_temperatures, 'o-', color='b', label='Atlantic Ocean')

ax.fill_between(years, pacific_temperatures - measurement_errors, pacific_temperatures + measurement_errors, color='r', alpha=0.1)
ax.plot(years, pacific_temperatures, 's-', color='r', label='Pacific Ocean')

ax.fill_between(years, indian_temperatures - measurement_errors, indian_temperatures + measurement_errors, color='g', alpha=0.1)
ax.plot(years, indian_temperatures, '^-', color='g', label='Indian Ocean')

# Add titles and labels
ax.set_title("Ocean Temperature Trends and Variability\n(2000-2040)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)

# Add a legend
ax.legend(loc='upper left', fontsize=12)

# Enhance the grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate notable points (e.g., local minima and maxima)
ax.annotate(f'Lowest Point\n{np.min(atlantic_temperatures):.1f}°C', 
            xy=(years[np.argmin(atlantic_temperatures)], np.min(atlantic_temperatures)), 
            xytext=(years[np.argmin(atlantic_temperatures)] - 5, np.min(atlantic_temperatures) - 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='darkblue')

ax.annotate(f'Highest Point\n{np.max(pacific_temperatures):.1f}°C',
            xy=(years[np.argmax(pacific_temperatures)], np.max(pacific_temperatures)),
            xytext=(years[np.argmax(pacific_temperatures)] + 2, np.max(pacific_temperatures) + 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='darkred')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()