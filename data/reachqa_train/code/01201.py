import matplotlib.pyplot as plt
import numpy as np

# Years from 2023 to 2033
years = np.arange(2023, 2034)

# Artificial data representing TWh generation
solar_power = np.array([80, 110, 140, 175, 215, 260, 310, 365, 425, 490, 560])
wind_power = np.array([90, 120, 155, 195, 240, 290, 345, 405, 470, 540, 615])
hydro_power = np.array([200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])

# Compute total power
total_power = solar_power + wind_power + hydro_power

# Calculate the percentage growth of solar power
solar_growth_percentage = np.gradient(solar_power) / solar_power * 100

# Create the area chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked area chart with markers
ax1.fill_between(years, 0, solar_power, label='Solar Power', color='#FFD700', alpha=0.8)
ax1.fill_between(years, solar_power, solar_power + wind_power, label='Wind Power', color='#87CEEB', alpha=0.8)
ax1.fill_between(years, solar_power + wind_power, total_power, label='Hydroelectric Power', color='#90EE90', alpha=0.8)
ax1.plot(years, solar_power, marker='o', color='orange', lw=2)
ax1.plot(years, solar_power + wind_power, marker='o', color='deepskyblue', lw=2)
ax1.plot(years, total_power, marker='o', color='green', lw=2)

# Primary y-axis setup
ax1.set_title("Projected Growth in Renewable Energy Generation (2023-2033)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Power Generation (TWh)", fontsize=12)

# Secondary y-axis for solar power growth percentage
ax2 = ax1.twinx()
ax2.plot(years, solar_growth_percentage, color='red', marker='s', linestyle='--', label='Solar Growth (%)')
ax2.set_ylabel("Solar Growth (%)", fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Legend and grid
ax1.legend(loc='upper left', fontsize=10, title="Energy Source")
ax2.legend(loc='upper right', fontsize=10)
ax1.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotations
ax1.annotate('Major Solar Expansion', xy=(2027, 250), xytext=(2025, 750),
             arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.5),
             fontsize=10, fontweight='bold', color='gold')

# Ensure layout is tight to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()