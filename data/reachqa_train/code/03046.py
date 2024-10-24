import numpy as np
import matplotlib.pyplot as plt

# Define years
years = np.array([2019, 2020, 2021, 2022, 2023])

# Define harvest data for each region (in tons)
# Adjusted to ensure clear visualization
applejoys_yield = np.array([
    [120, 150, 170, 160, 180],  # Golden Valley
    [80, 90, 100, 95, 105],     # Silver Plains
    [70, 75, 80, 85, 90]        # Emerald Highlands
])

berrybliss_yield = np.array([
    [100, 120, 130, 140, 150],  # Golden Valley
    [110, 115, 120, 125, 130],  # Silver Plains
    [60, 65, 70, 75, 80]        # Emerald Highlands
])

citrusburst_yield = np.array([
    [90, 85, 80, 95, 100],      # Golden Valley
    [100, 105, 110, 115, 120],  # Silver Plains
    [80, 85, 90, 95, 100]       # Emerald Highlands
])

# Colors for each fruit
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked bars for each region
bar_width = 0.25
for i, region in enumerate(['Golden Valley', 'Silver Plains', 'Emerald Highlands']):
    # Bottom calculations for stacking
    bottom_applejoys = np.zeros_like(years)
    bottom_berrybliss = applejoys_yield[i]
    
    # Applejoys
    ax.bar(years + i * bar_width, applejoys_yield[i], width=bar_width, color=colors[0], 
           label='Applejoys' if i == 0 else "", alpha=0.8, edgecolor='grey')
    
    # Berrybliss
    ax.bar(years + i * bar_width, berrybliss_yield[i], width=bar_width, bottom=bottom_berrybliss, 
           color=colors[1], label='Berrybliss' if i == 0 else "", alpha=0.8, edgecolor='grey')
    
    # Citrusburst
    ax.bar(years + i * bar_width, citrusburst_yield[i], width=bar_width, 
           bottom=bottom_berrybliss + berrybliss_yield[i], color=colors[2], 
           label='Citrusburst' if i == 0 else "", alpha=0.8, edgecolor='grey')

# Customize the plot
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Harvest Yield (Tons)', fontsize=12)
ax.set_title('The Great Fruit Harvest Competition\nin Orchard World (2019-2023)', fontsize=16, fontweight='bold')
ax.set_xticks(years + bar_width)
ax.set_xticklabels(years)
ax.legend(loc='upper left', fontsize=10, title='Fruits')

# Add grid for easier readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()