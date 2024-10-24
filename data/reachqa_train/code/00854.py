import matplotlib.pyplot as plt
import numpy as np

# Define months for the x-axis
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Temperature data for each city in degrees Celsius
climatia_temps = np.array([-2, 0, 5, 12, 18, 24, 28, 26, 19, 12, 6, 1])
tempestville_temps = np.array([8, 9, 10, 13, 16, 20, 22, 21, 18, 14, 10, 9])
sunnyvale_temps = np.array([15, 16, 18, 20, 24, 28, 30, 29, 27, 22, 18, 16])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the data with different styles for each city
ax.plot(months, climatia_temps, label='Climatia', color='blue', marker='o', linestyle='-', linewidth=2.5)
ax.plot(months, tempestville_temps, label='Tempestville', color='green', marker='s', linestyle='--', linewidth=2)
ax.plot(months, sunnyvale_temps, label='Sunnyvale', color='orange', marker='^', linestyle='-.', linewidth=2)

# Set the title and labels
ax.set_title('Urban Temperature Variations in 2023\nClimatia, Tempestville & Sunnyvale', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Adding a legend
ax.legend(loc='upper right', fontsize=12, frameon=False)

# Enable grid lines for readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotating peak temperatures for emphasis
ax.annotate(f"Peak: {climatia_temps.max()}°C", 
            (months[climatia_temps.argmax()], climatia_temps.max()), 
            textcoords="offset points", xytext=(-30, 10), ha='center', fontsize=10, color='blue')

ax.annotate(f"Peak: {tempestville_temps.max()}°C", 
            (months[tempestville_temps.argmax()], tempestville_temps.max()), 
            textcoords="offset points", xytext=(-30, 10), ha='center', fontsize=10, color='green')

ax.annotate(f"Peak: {sunnyvale_temps.max()}°C", 
            (months[sunnyvale_temps.argmax()], sunnyvale_temps.max()), 
            textcoords="offset points", xytext=(-30, -25), ha='center', fontsize=10, color='orange')

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()