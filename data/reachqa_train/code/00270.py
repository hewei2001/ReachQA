import matplotlib.pyplot as plt
import numpy as np

# Expanded Fictional Data: Annual incomes (in gold coins) for different professions in the Kingdom of Eldoria
wizards = [120, 150, 110, 160, 130, 170, 155, 190, 145, 180, 135, 165, 140, 175, 162, 188, 144, 177, 123]
warriors = [80, 90, 85, 75, 95, 100, 88, 92, 96, 82, 89, 101, 93, 91, 94, 97, 99, 84, 86]
alchemists = [100, 140, 150, 130, 145, 135, 120, 125, 138, 142, 148, 155, 137, 115, 112, 144, 159, 148]
healers = [70, 85, 80, 75, 90, 60, 65, 78, 82, 77, 85, 81, 75, 68, 66, 72, 79, 83]
merchants = [110, 130, 120, 115, 125, 135, 140, 118, 132, 128, 122, 136, 129, 134, 138, 127, 123]
blacksmiths = [95, 105, 90, 115, 108, 97, 101, 110, 104, 99, 103, 106, 107, 94, 92, 100]
bards = [75, 82, 78, 85, 79, 81, 77, 88, 76, 84, 73, 87, 86, 90, 74]
farmers = [65, 70, 68, 72, 74, 76, 71, 69, 73, 75, 67, 66, 78, 80, 77]
hunters = [115, 122, 119, 124, 121, 117, 120, 123, 125, 113, 118, 116, 126, 114]

# Aggregated Data
data = [wizards, warriors, alchemists, healers, merchants, blacksmiths, bards, farmers, hunters]

# Create box plot
fig, ax = plt.subplots(figsize=(16, 10))
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True,
                boxprops=dict(facecolor='#e6f2ff', color='#1a5276'),
                whiskerprops=dict(color='#1a5276'),
                capprops=dict(color='#1a5276'),
                medianprops=dict(color='#d9534f'),
                flierprops=dict(marker='o', color='#ff5733', alpha=0.6))

# Set xticklabels
ax.set_xticklabels(['Wizards', 'Warriors', 'Alchemists', 'Healers', 'Merchants',
                    'Blacksmiths', 'Bards', 'Farmers', 'Hunters'], fontsize=10, rotation=45)
ax.set_ylabel('Annual Income (in Gold Coins)', fontsize=14)
ax.set_xlabel('Professions', fontsize=14)

# Grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Title with line breaks
ax.set_title('Income Distribution Across Various Professions\nin the Kingdom of Eldoria',
             fontsize=16, fontweight='bold', color='#1a5276')

# Statistical Annotations
for i, profession_data in enumerate(data):
    mean_val = np.mean(profession_data)
    ax.text(i + 1, mean_val + 3, f'Mean: {mean_val:.1f}', horizontalalignment='center', color='green', fontsize=9)

# Information box
textstr = ('Kingdom of Eldoria Economic Overview:\n'
           '- Wizards: Mystical guidance\n'
           '- Warriors: Realm protectors\n'
           '- Alchemists: Transformation masters\n'
           '- Healers: Essential well-being\n'
           '- Merchants: Trade pillars\n'
           '- Blacksmiths: Forge keepers\n'
           '- Bards: Story weavers\n'
           '- Farmers: Earth tenders\n'
           '- Hunters: Wilderness scouts')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.95, 0.95, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props, ha='right')

# Tight layout
plt.tight_layout()

# Display the plot
plt.show()