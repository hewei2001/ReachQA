import numpy as np
import matplotlib.pyplot as plt

# Define extended years
years = np.arange(2010, 2024)

# Define harvest data for each region (in tons) for extended years
# Manually constructed for meaningful complexity
applejoys_yield = np.array([
    [100, 120, 130, 150, 160, 170, 160, 180, 190, 185, 200, 210, 220, 230],  # Golden Valley
    [70, 80, 90, 95, 100, 110, 105, 110, 120, 115, 125, 130, 135, 140],     # Silver Plains
    [50, 60, 70, 75, 80, 85, 90, 85, 95, 100, 105, 110, 115, 120],          # Emerald Highlands
    [40, 45, 50, 60, 65, 70, 75, 70, 80, 85, 90, 95, 100, 105]              # Ruby Hills
])

berrybliss_yield = np.array([
    [90, 100, 110, 120, 130, 140, 145, 150, 155, 150, 160, 165, 170, 175],  # Golden Valley
    [80, 85, 90, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],    # Silver Plains
    [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120],          # Emerald Highlands
    [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]          # Ruby Hills
])

citrusburst_yield = np.array([
    [85, 90, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],       # Golden Valley
    [95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160],  # Silver Plains
    [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],       # Emerald Highlands
    [65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130]         # Ruby Hills
])

# Additional fruit for complexity
peachdelight_yield = np.array([
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],           # Golden Valley
    [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],         # Silver Plains
    [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],             # Emerald Highlands
    [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120]           # Ruby Hills
])

# Define colors for each fruit
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700']

# Initialize the plot with subplots for each region
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

region_names = ['Golden Valley', 'Silver Plains', 'Emerald Highlands', 'Ruby Hills']

# Plot stacked bars for each region
bar_width = 0.15

for i, ax in enumerate(axs):
    # Calculate bottom stacks for bars
    bottom_applejoys = np.zeros_like(years)
    bottom_berrybliss = applejoys_yield[i]
    bottom_citrusburst = applejoys_yield[i] + berrybliss_yield[i]

    # Applejoys
    ax.bar(years + i * bar_width, applejoys_yield[i], width=bar_width, color=colors[0],
           label='Applejoys', alpha=0.8, edgecolor='grey')

    # Berrybliss
    ax.bar(years + i * bar_width, berrybliss_yield[i], width=bar_width, bottom=bottom_berrybliss,
           color=colors[1], label='Berrybliss', alpha=0.8, edgecolor='grey')

    # Citrusburst
    ax.bar(years + i * bar_width, citrusburst_yield[i], width=bar_width, bottom=bottom_citrusburst,
           color=colors[2], label='Citrusburst', alpha=0.8, edgecolor='grey')

    # Peach Delight
    ax.bar(years + i * bar_width, peachdelight_yield[i], width=bar_width, bottom=bottom_citrusburst + citrusburst_yield[i],
           color=colors[3], label='Peach Delight', alpha=0.8, edgecolor='grey')

    # Customize each subplot
    ax.set_title(f"{region_names[i]} Harvest Yield", fontsize=12)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Yield (Tons)', fontsize=10)
    ax.set_xticks(years + bar_width)
    ax.set_xticklabels(years, rotation=45)
    ax.legend(loc='upper left', fontsize=8)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure all text and elements are visible
plt.tight_layout()

# Show the plot
plt.show()