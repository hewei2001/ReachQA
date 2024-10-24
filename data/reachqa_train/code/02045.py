import matplotlib.pyplot as plt
import numpy as np

# Define flavor intensity data for each tea variety from different continents
tea_varieties = ['Green Tea', 'Black Tea', 'Herbal Tea']
continents = ['Asia', 'Africa', 'Europe']

green_tea_scores = [
    [70, 82, 85, 90, 72],  # Asia
    [60, 65, 68, 62, 70],  # Africa
    [75, 78, 80, 85, 82]   # Europe
]

black_tea_scores = [
    [85, 88, 90, 92, 89],  # Asia
    [70, 72, 75, 78, 74],  # Africa
    [80, 83, 85, 88, 86]   # Europe
]

herbal_tea_scores = [
    [60, 65, 62, 68, 63],  # Asia
    [75, 78, 80, 85, 82],  # Africa
    [65, 67, 70, 72, 68]   # Europe
]

# Aggregate the data
data = [green_tea_scores, black_tea_scores, herbal_tea_scores]

# Plot configuration
fig, ax = plt.subplots(figsize=(14, 8))

# Create a box plot for each tea variety
positions = np.array(range(len(continents))) * 4
for i, scores in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(scores, positions=pos, widths=0.6, patch_artist=True, notch=True)

    # Color each box according to its variety
    colors = ['#66c2a5', '#fc8d62', '#8da0cb']
    for patch, color in zip(bp['boxes'], [colors[i]] * len(continents)):
        patch.set_facecolor(color)

    # Customize the whiskers, caps, and medians
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1.5)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)

# Set x-ticks to position in the middle of the boxplot groups
ax.set_xticks(positions + 1)
ax.set_xticklabels(continents, fontsize=12)

# Labels and Title
ax.set_title("Global Rise of Tea Varieties:\nTaste Profiles Across Continents", fontsize=16, fontweight='bold')
ax.set_ylabel("Flavor Intensity Score", fontsize=14)
ax.set_xlabel("Continents", fontsize=14)

# Grid customization
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Legend indicating tea variety colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, tea_varieties, title='Tea Varieties', loc='upper right', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()