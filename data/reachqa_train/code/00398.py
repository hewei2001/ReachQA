import matplotlib.pyplot as plt
import numpy as np

# Years for the forecast period
years = np.arange(2025, 2036)

# Projected adoption levels for each transportation mode (in arbitrary units)
hyperloop = np.array([0, 5, 20, 40, 70, 100, 150, 200, 260, 330, 400])
electric_air_taxis = np.array([10, 30, 60, 100, 150, 210, 280, 360, 450, 550, 660])
autonomous_vehicles = np.array([50, 100, 160, 230, 300, 380, 460, 550, 640, 740, 850])
high_speed_trains = np.array([100, 140, 190, 250, 320, 400, 490, 590, 700, 820, 950])

# Stacking the data
transportation_data = np.vstack([hyperloop, electric_air_taxis, autonomous_vehicles, high_speed_trains])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, transportation_data, labels=['Hyperloop', 'Electric Air Taxis', 'Autonomous Vehicles', 'High-Speed Trains'],
             colors=['#FF6347', '#4682B4', '#32CD32', '#FFD700'], alpha=0.7)

# Customize the plot
ax.set_title('Projected Adoption of Futuristic Transportation Modes\n(2025-2035)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Level (Arbitrary Units)', fontsize=12)

# Add legend and grid
ax.legend(loc='upper left', fontsize=10, title='Transportation Mode', frameon=False)
ax.grid(linestyle='--', alpha=0.5)

# Enhance readability of x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1001, 100))

# Annotate significant milestones
ax.annotate('Hyperloop Operational Launch', xy=(2028, 40), xytext=(2026, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

ax.annotate('Electric Air Taxis Major Uptake', xy=(2030, 360), xytext=(2028, 500),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=1.5),
            fontsize=10, color='blue')

# Add a brief description or note
description_box = dict(boxstyle='round', facecolor='lightgray', alpha=0.3)
description = ("Anticipated shift towards innovative transport modes\n"
               "driven by sustainability and technological advances.")
ax.text(0.02, 0.97, description, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=description_box)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()