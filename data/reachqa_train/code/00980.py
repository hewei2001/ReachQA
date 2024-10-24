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
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# Define colors for each festival
colors = plt.cm.viridis(np.linspace(0, 1, num_festivals))

# Plot each festival's participation level
bars = ax.bar(angles, participation_levels, width=sector_angle, color=colors, edgecolor='black', alpha=0.7)

# Set the labels for each festival
ax.set_xticks(angles)
ax.set_xticklabels(festivals, fontsize=10, color='black', fontweight='bold')

# Add a title and customize the radial ticks
plt.title('Global Festival Enthusiast’s Guide:\nCultural Festival Participation Trends', 
          size=16, color='navy', pad=20)
ax.set_yticklabels([])
ax.yaxis.grid(False)

# Add a legend
legend_labels = [f'{festival} ({level}k)' for festival, level in zip(festivals, participation_levels)]
ax.legend(bars, legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Festivals', frameon=False)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the rose chart
plt.show()