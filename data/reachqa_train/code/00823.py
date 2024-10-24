import matplotlib.pyplot as plt
import numpy as np

# Data: Renewable energy adoption rates by continent in 2025 (%)
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
adoption_rates = [
    [12, 15, 14, 18, 20, 11, 22, 21, 19, 17],  # Africa
    [35, 38, 37, 40, 42, 36, 43, 41, 39, 34],  # Asia
    [60, 62, 65, 64, 67, 61, 63, 66, 68, 69],  # Europe
    [45, 47, 49, 48, 50, 46, 44, 51, 53, 52],  # North America
    [55, 58, 57, 59, 56, 54, 60, 61, 62, 63],  # South America
    [70, 72, 71, 73, 74, 75, 76, 77, 78, 79]   # Oceania
]

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each continent's data
bp = ax.boxplot(adoption_rates, vert=False, patch_artist=True, notch=True, labels=continents)

# Customize boxplot colors
colors = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.75)

# Customize whiskers, caps, and medians
for whisker, cap in zip(bp['whiskers'], bp['caps']):
    whisker.set(color='#7570b3', linewidth=1.5)
    cap.set(color='#7570b3', linewidth=1.5)

for median in bp['medians']:
    median.set(color='#d95f02', linewidth=2)

# Titles and labels
ax.set_title('Renewable Energy Adoption Rates\nby Continent in 2025', fontsize=16, pad=20)
ax.set_xlabel('Adoption Rate (%)', fontsize=14)
ax.set_ylabel('Continent', fontsize=14)

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add legend
legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=continent) for color, continent in zip(colors, continents)]
ax.legend(handles=legend_elements, title='Continents', loc='lower right', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()