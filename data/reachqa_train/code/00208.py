import matplotlib.pyplot as plt
import numpy as np

# Data: Energy consumption in kWh for each day of the week
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
energy_consumption = np.array([18.5, 19.0, 17.5, 20.5, 22.0, 21.5, 18.0])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(days, energy_consumption, marker='o', linestyle='-', color='navy', linewidth=2, markersize=8, label='Energy Consumption')

# Annotations for specific events or peak times
events = {
    "Mon": "Device Setup",
    "Thu": "Thermostat Change",
    "Fri": "Movie Night",
    "Sat": "Low Power Mode"
}

for day, event in events.items():
    plt.annotate(event, xy=(day, energy_consumption[list(days).index(day)]),
                 xytext=(0, 20), textcoords='offset points', ha='center',
                 arrowprops=dict(arrowstyle='->', color='grey', lw=1.5))

# Titles and labels
plt.title("Weekly Energy Consumption Patterns\nin a Smart Home", fontsize=16, pad=20)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Energy Consumption (kWh)", fontsize=12)

# Displaying a legend
plt.legend(loc='upper right')

# Aesthetic improvements
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()