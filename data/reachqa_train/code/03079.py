import matplotlib.pyplot as plt
import numpy as np

# Define the types of renewable energy
energy_types = ['Solar', 'Wind', 'Hydroelectric']

# Define the percentage adoption for each energy type in urban and rural areas
urban_adoption = [60, 20, 15]
rural_adoption = [25, 35, 30]
other_sources = [15, 45, 55]  # Represents non-renewable or less common energy sources

# Ensure each category sums to 100%
assert all(u + r + o == 100 for u, r, o in zip(urban_adoption, rural_adoption, other_sources)), "Percentages must sum to 100."

# Plot the percentage bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack bars: Urban, Rural, Other
p1 = ax.bar(energy_types, urban_adoption, label='Urban Areas', color='lightblue', width=0.5)
p2 = ax.bar(energy_types, rural_adoption, bottom=urban_adoption, label='Rural Areas', color='lightgreen', width=0.5)
p3 = ax.bar(energy_types, other_sources, bottom=np.array(urban_adoption) + np.array(rural_adoption), label='Other Sources', color='lightcoral', width=0.5)

# Annotate bars with percentage values
for bars in (p1, p2, p3):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 0), textcoords='offset points', ha='center', va='center', fontsize=10)

# Customize the plot
ax.set_title("Renewable Energy Adoption in 2023:\nUrban vs. Rural Areas", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Type of Renewable Energy", fontsize=12)
ax.set_ylabel("Percentage of Households (%)", fontsize=12)
ax.set_ylim(0, 100)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Set x-ticks and adjust them
ax.set_xticks(np.arange(len(energy_types)))
ax.set_xticklabels(energy_types)

# Add legend and layout adjustments
ax.legend(title='Regions', fontsize=10, title_fontsize=11, loc='upper right')
plt.tight_layout()

# Display the chart
plt.show()