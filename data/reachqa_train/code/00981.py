import matplotlib.pyplot as plt
import numpy as np

# Festivals and their participation levels in thousands
festivals = ['Diwali', 'Rio Carnival', 'Chinese New Year', 'Oktoberfest', 
             'Mardi Gras', 'Day of the Dead', 'Holi', 'Edinburgh Festival']
participation_levels = [600, 1200, 800, 1500, 900, 500, 750, 1100]

# Calculate the number of categories and angle for each sector
num_festivals = len(festivals)
sector_angle = (2 * np.pi) / num_festivals
angles = np.linspace(0, 2 * np.pi, num_festivals, endpoint=False).tolist()

# Create the rose chart
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))

# Define a segmented color map
colors = plt.cm.Spectral(np.linspace(0, 1, num_festivals))

# Plot each festival's participation level
bars = ax.bar(angles, participation_levels, width=sector_angle*0.9, color=colors, edgecolor='black', alpha=0.85)

# Set the labels for each festival
ax.set_xticks(angles)
ax.set_xticklabels(festivals, fontsize=10, color='black', fontweight='bold')

# Add participation level labels on the bars
for bar, level in zip(bars, participation_levels):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 50, f'{level}k', 
            ha='center', va='center', fontsize=9, color='black', fontweight='bold')

# Customize grid and remove unnecessary radial ticks
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_yticklabels([])

# Add a title with line breaks
plt.title('Global Festival Enthusiast’s Guide:\nCultural Festival Participation Trends\n(Participation in Thousands)', 
          size=16, color='navy', pad=20)

# Enhance the legend placement
legend_labels = [f'{festival} ({level}k)' for festival, level in zip(festivals, participation_levels)]
ax.legend(bars, legend_labels, loc='upper left', bbox_to_anchor=(-0.1, 1.15), fontsize=10, title='Festivals', frameon=False)

# Center text annotation
total_participation = sum(participation_levels)
ax.annotate(f'Total Participation:\n{total_participation}k', xy=(0, 0), fontsize=12, ha='center', color='darkgreen', fontweight='bold')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the rose chart
plt.show()