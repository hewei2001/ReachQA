import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.array([2015, 2016, 2017, 2018, 2019])

# Energy output data in TWh for each year
solar_output = np.array([220, 245, 260, 280, 310])
wind_output = np.array([180, 210, 230, 270, 290])
hydro_output = np.array([260, 255, 265, 270, 275])

# Create the line plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, solar_output, label='Solar Energy', color='gold', marker='o', linewidth=2, linestyle='-')
ax.plot(years, wind_output, label='Wind Energy', color='skyblue', marker='^', linewidth=2, linestyle='--')
ax.plot(years, hydro_output, label='Hydro Energy', color='blue', marker='s', linewidth=2, linestyle='-.')

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Output (TWh)', fontsize=12)
ax.set_title('Annual Renewable Energy Output\nby Source (2015-2019)', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust the subplot layout for better fit
plt.tight_layout()

# Show the plot
plt.show()