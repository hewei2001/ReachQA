import matplotlib.pyplot as plt
import numpy as np

# Extended data for more civilizations' lifespans
egyptian_years = [500, 400, 600, 700, 800, 850, 900, 1000, 1050, 1100, 1150, 1200, 1300, 1400]
roman_years = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1453, 1476, 1500, 1550]
greek_years = [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100]
mesopotamian_years = [1000, 900, 800, 700, 600, 500, 400, 300, 250, 200, 150]
indus_years = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]
mayan_years = [250, 500, 750, 1000, 1200, 1300, 1400, 1450, 1500]
han_china_years = [206, 220, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
minoan_years = [300, 400, 500, 600, 700, 750, 800, 850, 900, 950, 1000]

# Combine data for plotting
data = [egyptian_years, roman_years, greek_years, mesopotamian_years, indus_years,
        mayan_years, han_china_years, minoan_years]
civilizations = ['Egyptian', 'Roman', 'Greek', 'Mesopotamian', 'Indus Valley',
                 'Mayan', 'Han China', 'Minoan']

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Create the vertical box plot with more customization
box = ax.boxplot(data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(color='black'),
                 whiskerprops=dict(color='blue', linestyle='--'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red', linewidth=2),
                 flierprops=dict(markerfacecolor='yellow', marker='s', markersize=6, linestyle='none'))

# Colors for each civilization
colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#B0E0E6', '#AFEEEE', '#FFB6C1', '#8A2BE2', '#D2691E']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set the labels and title
ax.set_xticklabels(civilizations, fontsize=10, rotation=45, ha='right')
ax.set_xlabel('Civilizations', fontsize=12)
ax.set_ylabel('Lifespan (Years)', fontsize=12)
ax.set_title('Lifespans of Prominent Ancient Civilizations\nAn Analytical Overview of Historical Longevity and Stability',
             fontsize=16, fontweight='bold', loc='center')

# Add grid and average line
ax.grid(True, linestyle='--', alpha=0.6)
overall_mean = np.mean(np.concatenate(data))
ax.axhline(overall_mean, color='green', linestyle='--', linewidth=1.5, label='Overall Average Lifespan')

# Add variance annotations
for i, d in enumerate(data):
    variance = np.var(d)
    ax.text(i+1, np.max(d) + 50, f'Var: {variance:.1f}', ha='center', fontsize=10, color='darkblue')

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()