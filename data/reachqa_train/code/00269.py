import matplotlib.pyplot as plt
import numpy as np

# Fictional Data: Annual incomes (in gold coins) for different professions in the Kingdom of Eldoria
wizards = [120, 150, 110, 160, 130, 170, 155, 190, 145, 180, 135, 165, 140, 175]
warriors = [80, 90, 85, 75, 95, 100, 88, 92, 96, 82, 89, 101, 93, 91]
alchemists = [100, 140, 150, 130, 145, 135, 120, 125, 138, 142, 148, 155, 137, 115]
healers = [70, 85, 80, 75, 90, 60, 65, 78, 82, 77, 85, 81, 75, 68]
merchants = [110, 130, 120, 115, 125, 135, 140, 118, 132, 128, 122, 136, 129, 134]

# Aggregated Data
data = [wizards, warriors, alchemists, healers, merchants]

# Create box plot
fig, ax = plt.subplots(figsize=(12, 8))
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True,
                boxprops=dict(facecolor='#f0f0f5', color='#0b5394'),
                whiskerprops=dict(color='#0b5394'),
                capprops=dict(color='#0b5394'),
                medianprops=dict(color='#990000'),
                flierprops=dict(marker='o', color='#ff5733', alpha=0.6))

# Set xticklabels
ax.set_xticklabels(['Wizards', 'Warriors', 'Alchemists', 'Healers', 'Merchants'], fontsize=12)
ax.set_ylabel('Annual Income (in Gold Coins)', fontsize=14)
ax.set_xlabel('Professions', fontsize=14)

# Grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Title with line breaks
ax.set_title('Income Distribution Across Professions\nin the Kingdom of Eldoria',
             fontsize=16, fontweight='bold', color='#0b5394')

# Information box
textstr = ('Kingdom of Eldoria Economic Overview:\n'
           '- Wizards: Mystical guidance\n'
           '- Warriors: Realm protectors\n'
           '- Alchemists: Transformation masters\n'
           '- Healers: Essential well-being\n'
           '- Merchants: Trade pillars')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.95, 0.95, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props, ha='right')

# Tight layout
plt.tight_layout()

# Display the plot
plt.show()