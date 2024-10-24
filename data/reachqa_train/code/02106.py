import matplotlib.pyplot as plt
import numpy as np

# Define data for ancient civilizations' lifespans
# Each list contains fictional lifespan periods within a specific civilization
egyptian_years = [500, 400, 600, 700, 800, 850, 900, 1000, 1050, 1100, 1150]
roman_years = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1453]
greek_years = [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
mesopotamian_years = [1000, 900, 800, 700, 600, 500, 400, 300, 250]
indus_years = [500, 450, 400, 350, 300, 250, 200, 150]

# Combine data into a list for plotting
data = [egyptian_years, roman_years, greek_years, mesopotamian_years, indus_years]
civilizations = ['Egyptian', 'Roman', 'Greek', 'Mesopotamian', 'Indus Valley']

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create the vertical box plot
box = ax.boxplot(data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='#FFDDC1', color='brown'),
                 whiskerprops=dict(color='brown'),
                 capprops=dict(color='brown'),
                 medianprops=dict(color='darkred', linewidth=2),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none'))

# Colors for each civilization
colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#B0E0E6', '#AFEEEE']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set the labels and title
ax.set_xticklabels(civilizations, fontsize=12)
ax.set_xlabel('Civilizations', fontsize=12)
ax.set_ylabel('Lifespan (Years)', fontsize=12)
ax.set_title('Lifespans of Prominent Ancient Civilizations\nAn Analysis of Historical Longevity and Stability',
             fontsize=16, fontweight='bold', loc='center')

# Add grid and average line
ax.grid(True, linestyle='--', alpha=0.6)
overall_mean = np.mean(egyptian_years + roman_years + greek_years + mesopotamian_years + indus_years)
ax.axhline(overall_mean, color='green', linestyle='--', linewidth=1.5, label='Overall Average Lifespan')

# Add a legend
ax.legend(loc='upper right', fontsize=10)

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()