import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# CO2 absorption data (in kg) for three tree species over a week
oak_absorption = np.array([12, 15, 11, 16, 14, 13, 15])
pine_absorption = np.array([8, 9, 10, 9, 8, 10, 11])
maple_absorption = np.array([6, 7, 7, 6, 8, 9, 7])

# Sunlight hours data over the same week
sunlight_hours = np.array([8, 10, 9, 11, 10, 7, 8])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plotting the area chart
ax1.fill_between(days, 0, oak_absorption, label='Oak', color='#8B4513', alpha=0.7)
ax1.fill_between(days, oak_absorption, oak_absorption + pine_absorption, label='Pine', color='#228B22', alpha=0.7)
ax1.fill_between(days, oak_absorption + pine_absorption, oak_absorption + pine_absorption + maple_absorption, label='Maple', color='#FFD700', alpha=0.7)

# Set title and labels for the primary y-axis
ax1.set_title('CO2 Absorption by Trees and Daily Sunlight Hours\nGreen Valley Park Over a Week', fontsize=16, pad=20)
ax1.set_xlabel('Days of the Week', fontsize=12)
ax1.set_ylabel('CO2 Absorption (kg)', fontsize=12)
ax1.set_xticks(range(len(days)))
ax1.set_xticklabels(days, rotation=45)
ax1.grid(linestyle='--', alpha=0.5)

# Create a second y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(days, sunlight_hours, label='Sunlight Hours', color='royalblue', marker='o', linewidth=2)
ax2.set_ylabel('Sunlight Hours (hours)', fontsize=12)

# Combine legends from both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10, frameon=True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()