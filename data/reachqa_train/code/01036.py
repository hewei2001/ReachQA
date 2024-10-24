import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Artificial data representing growth in energy consumption (TWh)
solar_energy = [
    5, 7, 10, 15, 22, 35, 53, 77, 110, 150,
    210, 290, 380, 500, 630, 800, 1000, 1250, 1550, 1900, 2300
]
wind_energy = [
    20, 30, 45, 70, 95, 130, 175, 230, 300, 380,
    470, 575, 690, 820, 960, 1100, 1260, 1450, 1650, 1900, 2200
]
hydropower_energy = [
    800, 820, 850, 880, 910, 940, 970, 1000, 1030, 1060,
    1100, 1140, 1180, 1230, 1280, 1340, 1400, 1470, 1550, 1630, 1720
]

# Create a new figure and axis
plt.figure(figsize=(12, 8))

# Plot each energy source
plt.plot(years, solar_energy, color='goldenrod', linewidth=2, marker='o', label='Solar Energy')
plt.plot(years, wind_energy, color='skyblue', linewidth=2, marker='s', label='Wind Energy')
plt.plot(years, hydropower_energy, color='seagreen', linewidth=2, marker='^', label='Hydropower Energy')

# Add titles and labels
plt.title("Global Renewable Energy Consumption (2000-2020)\nA Transition to Sustainable Energy Sources", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Consumption (TWh)", fontsize=12)

# Add a legend
plt.legend(title='Energy Source', loc='upper left', fontsize=10)

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Add annotations to highlight milestones
plt.annotate('Rapid Growth\nin Solar', xy=(2012, 380), xytext=(2008, 800),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')

plt.annotate('Wind Energy Surge', xy=(2008, 300), xytext=(2002, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')

plt.annotate('Steady Growth\nin Hydropower', xy=(2015, 1340), xytext=(2002, 1500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()