import matplotlib.pyplot as plt

# Efficiency scores for renewable energy sources across different regions
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
efficiency_data = [
    [75, 85, 80, 88, 90, 95, 93, 77, 82, 78],  # Solar
    [60, 72, 68, 66, 74, 75, 73, 71, 70, 69],  # Wind
    [85, 87, 90, 92, 88, 85, 89, 91, 86, 84],  # Hydroelectric
    [55, 60, 58, 62, 59, 57, 61, 63, 64, 56],  # Biomass
    [70, 72, 73, 78, 80, 75, 77, 76, 74, 71],  # Geothermal
]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Horizontal box plot
bp = ax.boxplot(efficiency_data, vert=False, patch_artist=True, notch=True, showmeans=True,
                meanline=True, meanprops=dict(linestyle='-', linewidth=2.5, color='blue'))

# Customizing colors for each box
colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color, alpha=0.6)

# Enhance medians, whiskers, and caps
for whisker in bp['whiskers']:
    whisker.set(color='#2C3E50', linewidth=2, linestyle="--")

for cap in bp['caps']:
    cap.set(color='#2C3E50', linewidth=2)

for median in bp['medians']:
    median.set(color='green', linewidth=3)

# Adding title and labels
ax.set_title('Global Renewable Energy Efficiency Evaluation:\nPerformance Across Various Test Regions', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Efficiency Score (%)', fontsize=13)
ax.set_yticklabels(energy_sources, fontsize=12)

# Grid and limits
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(50, 100)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()