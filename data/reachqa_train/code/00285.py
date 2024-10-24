import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])

# Average temperatures (°C)
average_temperatures = np.array([
    1.5, 3.0, 6.5, 10.5, 14.0, 18.5, 22.0, 21.0, 16.5, 11.0, 6.0, 2.5
])

# Temperature error margins (°C)
temperature_errors = np.array([
    1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9
])

# Plot the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 6))

ax.errorbar(
    months, average_temperatures, yerr=temperature_errors, fmt='-o', 
    color='#FF5733', ecolor='lightgray', elinewidth=2, capsize=4, label='Average Temp'
)

# Customize the plot appearance
ax.set_title('Average Monthly Temperatures in Evergreen Valley\nwith Climatic Variability', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_ylim(0, 25)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right', fontsize=10)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()