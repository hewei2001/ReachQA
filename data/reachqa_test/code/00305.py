import matplotlib.pyplot as plt
import numpy as np

# Data for the original ring chart (distribution of influence)
deities = ['Zephyrus', 'Hestara', 'Oronos', 'Nemera', 'Phyrros']
influence_percentages = [20, 25, 15, 30, 10]
colors = ['#98df8a', '#ffbb78', '#aec7e8', '#f7b6d2', '#ff9896']

# New data for the bar chart (influence change over time or across realms)
time_periods = ['Ancient Era', 'Medieval Era', 'Modern Era']
influence_change = {
    'Zephyrus': [15, 18, 20],
    'Hestara': [22, 24, 25],
    'Oronos': [12, 13, 15],
    'Nemera': [28, 29, 30],
    'Phyrros': [8, 9, 10]
}

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Create the ring chart
ax1 = axes[0]
wedges, texts, autotexts = ax1.pie(
    influence_percentages, labels=deities, autopct='%1.1f%%',
    startangle=90, colors=colors, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='w')
ax1.add_artist(centre_circle)
ax1.set_title("Mythical Pantheon Power Dynamics\nDistribution of Divine Influence", fontsize=14, fontweight='bold')
ax1.axis('equal')  
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')
ax1.legend(wedges, deities, title="Deities", loc="center left", bbox_to_anchor=(-0.1, 0.5))

# Create the bar chart for influence change
ax2 = axes[1]
bar_width = 0.15
indices = np.arange(len(time_periods))
for i, deity in enumerate(deities):
    ax2.bar(indices + i * bar_width, influence_change[deity], bar_width, label=deity, color=colors[i])

ax2.set_title('Influence Change Over Time', fontsize=12, fontweight='bold')
ax2.set_xlabel('Time Periods', fontsize=10)
ax2.set_ylabel('Influence (%)', fontsize=10)
ax2.set_xticks(indices + bar_width * (len(deities) - 1) / 2)
ax2.set_xticklabels(time_periods, rotation=20)
ax2.legend(title="Deities", bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()