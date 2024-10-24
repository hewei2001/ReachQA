import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Define continents and their respective attraction breakdown
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Australia', 'Antarctica']
attraction_types = ['Natural Wonders', 'Cultural Heritage', 'Tech Innovations', 'Adventure Tourism']

# Data: each sublist corresponds to the attraction distribution for a continent
data = [
    [30, 30, 25, 15],  # Asia
    [20, 35, 30, 15],  # Europe
    [25, 20, 40, 15],  # North America
    [35, 25, 20, 20],  # South America
    [40, 30, 15, 15],  # Africa
    [30, 20, 30, 20],  # Australia
    [50, 0, 20, 30]    # Antarctica
]

# Colors for each type of attraction
colors = ['#4CAF50', '#FF5733', '#3498DB', '#F1C40F']

# Create subplots for each continent
fig, axes = plt.subplots(2, 4, figsize=(20, 10), subplot_kw=dict(aspect='equal'))
fig.suptitle('Interstellar Tourism Attractions by Continent:\nA Glimpse into Earth’s Diverse Offerings - 2075',
             fontsize=16, fontweight='bold', ha='center')

# Plot the pie charts for each continent
for i, ax in enumerate(axes.flat):
    if i < len(continents):
        wedges, texts, autotexts = ax.pie(data[i], labels=attraction_types, autopct='%1.1f%%',
                                          startangle=90, colors=colors,
                                          wedgeprops={'edgecolor': 'black'},
                                          explode=(0.05, 0, 0, 0))
        ax.set_title(continents[i], fontsize=12, fontweight='bold')
        for text in texts + autotexts:
            text.set_fontsize(9)
    else:
        ax.axis('off')

# Customize legend with symbols
legend_elements = [Patch(facecolor=color, edgecolor='black', label=atype) for atype, color in zip(attraction_types, colors)]
fig.legend(handles=legend_elements, loc='center right', fontsize=10, title='Attraction Types', bbox_to_anchor=(1.15, 0.5))

# Add a radar chart as a new subplot
ax_radar = plt.subplot(2, 4, 8, polar=True)
labels = np.array(attraction_types)
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
values = [np.mean([data[j][i] for j in range(len(data))]) for i in range(num_vars)]
values += values[:1]
angles += angles[:1]

ax_radar.fill(angles, values, color='lightblue', alpha=0.25)
ax_radar.plot(angles, values, color='blue', linewidth=2)

ax_radar.set_yticklabels([])
ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(labels, fontsize=10)
ax_radar.set_title('Average Distribution of Attractions', fontsize=12, fontweight='bold')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()