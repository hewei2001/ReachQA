import matplotlib.pyplot as plt
import numpy as np

# Define energy sources and their projected contributions in 2050
energy_sources = ['Solar Power', 'Wind Power', 'Hydropower', 'Biomass Energy', 'Geothermal Energy', 'Ocean Energy']
energy_contribution = [35, 30, 15, 10, 7, 3]  # Hypothetical percentages for 2050

# Colors for energy sources
colors = ['#FFD700', '#87CEEB', '#4682B4', '#8FBC8F', '#DEB887', '#20B2AA']

# Hypothetical growth data over time
years = np.array([2000, 2010, 2020, 2030, 2040, 2050])
growth_data = {
    'Solar Power': [1, 2, 5, 10, 20, 35],
    'Wind Power': [1, 4, 8, 12, 20, 30],
    'Hydropower': [20, 18, 17, 16, 15, 15],
    'Biomass Energy': [5, 6, 7, 8, 9, 10],
    'Geothermal Energy': [2, 3, 4, 5, 6, 7],
    'Ocean Energy': [1, 1.5, 2, 2.5, 3, 3]
}

# Create the subplot structure
fig, axes = plt.subplots(ncols=2, figsize=(15, 7))

# Plot the pie chart
axes[0].pie(
    energy_contribution,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='white'),
    explode=(0.1, 0, 0, 0, 0, 0)
)

# Create a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axes[0].add_artist(centre_circle)

# Title for the pie chart
axes[0].set_title("Projected Energy Sources in 2050", fontsize=13, fontweight='bold', y=1.05)

# Bar chart for energy growth over time
for i, (energy, data) in enumerate(growth_data.items()):
    axes[1].plot(years, data, marker='o', label=energy, color=colors[i])

# Set labels and title for bar chart
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Energy Contribution (%)', fontsize=12)
axes[1].set_title("Growth Trend of Renewable Energy Sources (2000-2050)", fontsize=13, fontweight='bold')

# Enhance layout and add grid
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(title="Energy Sources", fontsize=10, title_fontsize='11')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()