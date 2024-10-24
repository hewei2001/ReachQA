import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2023)
subgenres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Paranormal Fantasy', 'Historical Fantasy']

# Number of books published in each subgenre per year
epic_fantasy = [120, 130, 140, 150, 155, 160, 170, 180, 190, 195]
urban_fantasy = [110, 115, 120, 125, 130, 135, 140, 145, 150, 155]
dark_fantasy = [50, 55, 60, 65, 75, 80, 85, 90, 95, 100]
paranormal_fantasy = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
historical_fantasy = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

# Collect data
data = [epic_fantasy, urban_fantasy, dark_fantasy, paranormal_fantasy, historical_fantasy]

# Colors for each subgenre
colors = ['#7f7fff', '#ff7f7f', '#7fff7f', '#ffff7f', '#7fffff']

# Create the bar plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15  # width of each bar
positions = np.arange(len(years))

# Plot each subgenre's data
for idx, subgenre in enumerate(subgenres):
    ax.bar(positions + idx * bar_width, data[idx], width=bar_width, label=subgenre, color=colors[idx])

# Labeling and aesthetics
ax.set_title('Growth of Fantasy Book Subgenres\nin the Last Decade', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Books Published', fontsize=12, labelpad=10)
ax.set_xticks(positions + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title="Fantasy Subgenres", fontsize=10, title_fontsize=12, loc='upper left')
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Display data values on top of bars
for idx, subgenre in enumerate(data):
    for x, y in zip(positions, subgenre):
        ax.text(x + idx * bar_width, y + 2, str(y), ha='center', va='bottom', fontsize=9)

# Set limits and layout
ax.set_xlim([positions[0] - 0.3, positions[-1] + bar_width * 5])
ax.set_ylim([0, max(max(data)) + 20])
plt.tight_layout()

# Show the plot
plt.show()