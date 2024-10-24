import matplotlib.pyplot as plt
import numpy as np

# Years from 2023 to 2033
years = np.arange(2023, 2034)

# Artificial data representing TWh generation
solar_power = np.array([80, 110, 140, 175, 215, 260, 310, 365, 425, 490, 560])
wind_power = np.array([90, 120, 155, 195, 240, 290, 345, 405, 470, 540, 615])
hydro_power = np.array([200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked area chart
ax.fill_between(years, 0, solar_power, label='Solar Power', color='#FFD700', alpha=0.8)
ax.fill_between(years, solar_power, solar_power + wind_power, label='Wind Power', color='#87CEEB', alpha=0.8)
ax.fill_between(years, solar_power + wind_power, solar_power + wind_power + hydro_power, label='Hydroelectric Power', color='#90EE90', alpha=0.8)

# Add title and labels
ax.set_title("Projected Growth in Renewable Energy\nGeneration (2023-2033)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Power Generation (TWh)", fontsize=12)

# Customize gridlines
ax.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend to the chart
ax.legend(loc='upper left', fontsize=10, title="Energy Source")

# Rotate x-axis labels if necessary
plt.xticks(rotation=45)

# Annotate a significant event
ax.annotate('Major Solar Expansion', xy=(2027, 250), xytext=(2025, 800),
            arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='gold')

# Ensure layout is tight to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()