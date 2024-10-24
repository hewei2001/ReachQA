import matplotlib.pyplot as plt
import numpy as np

# Extended list of technologies and their adoption rates over a three-year period
technologies = [
    'IoT', 'AI-Driven\nPublic Services', 'Autonomous\nVehicles',
    'Smart Grids', 'Blockchain\nGovernance', 'Renewable\nEnergy Systems',
    'Urban Analytics', 'Digital Twins', 'Cybersecurity', '5G Networks'
]

# Hypothetical adoption rates for 2021, 2022, 2023
adoption_rates_2021 = np.array([75, 65, 45, 60, 35, 40, 50, 30, 55, 20])
adoption_rates_2022 = np.array([80, 68, 48, 63, 38, 45, 55, 35, 60, 25])
adoption_rates_2023 = np.array([85, 70, 50, 65, 40, 50, 60, 40, 65, 30])

# Error bars for 2023 rates
error = np.array([3, 2, 4, 3, 5, 3, 2, 2, 3, 4])

# Calculate non-adoption rates
non_adoption_rates_2023 = 100 - adoption_rates_2023

# Create subplots
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked bars for 2023
bars1 = ax.barh(technologies, adoption_rates_2023, xerr=error, color='#1f77b4', label='Adoption (2023)', capsize=5)
bars2 = ax.barh(technologies, non_adoption_rates_2023, left=adoption_rates_2023, color='#c7c7c7', label='Non-Adoption (2023)')

# Plot line segments within bars to show previous years
for i, tech in enumerate(technologies):
    ax.plot([adoption_rates_2021[i], adoption_rates_2022[i], adoption_rates_2023[i]],
            [i, i, i], marker='o', color='orange', markersize=5, label='Previous Years' if i == 0 else "")

# Titles and labels
ax.set_title('Adoption of Emerging Technologies in Smart Cities (2021-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_xlim(0, 100)

# Percentage labels inside each bar for 2023
for bar in bars1:
    width = bar.get_width()
    label_position = width - 10 if width > 10 else width + 5
    ax.text(label_position, bar.get_y() + bar.get_height() / 2, f'{int(width)}%', ha='center', va='center', color='white' if width > 10 else 'black', fontsize=10, weight='bold')

# Grid and ticks
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.set_tick_params(rotation=0)

# Add legend
ax.legend(loc='lower right', fontsize=10, title='Adoption Status')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()