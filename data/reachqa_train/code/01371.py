import matplotlib.pyplot as plt
import numpy as np

# Define the years and sectors
years = np.array([2018, 2019, 2020, 2021, 2022])
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']

# Define fictional energy consumption data in GWh
energy_consumption = np.array([
    [120, 135, 145, 155, 160],  # Residential
    [200, 215, 225, 235, 240],  # Commercial
    [300, 290, 280, 270, 265],  # Industrial
    [180, 195, 205, 220, 230]   # Transportation
])

# Colors for each sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

# Plot each sector's data
bottoms = np.zeros(len(years))
for i, (sector, color) in enumerate(zip(sectors, colors)):
    ax.bar(years, energy_consumption[i], bar_width, bottom=bottoms, label=sector, color=color, alpha=0.85)
    bottoms += energy_consumption[i]

# Add titles and labels
plt.title("Energy Consumption by Sector in Solar City\n(2018-2022)", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Consumption (GWh)", fontsize=12)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Adding a legend to distinguish the sectors
plt.legend(title='Sector', title_fontsize=12, fontsize=10, loc='upper right')

# Add data labels to the bars
for i, (consumptions, bottom) in enumerate(zip(energy_consumption, np.cumsum(energy_consumption, axis=0))):
    for j, (consumption, b) in enumerate(zip(consumptions, bottom)):
        ax.text(years[j], b - consumption / 2, f'{consumption}', ha='center', va='center', color='black', fontsize=9)

# Set y-axis limit to ensure all labels are visible
ax.set_ylim(0, np.max(bottoms) + 50)

# Ensure the x-axis labels are rotated if necessary
plt.xticks(years, rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()