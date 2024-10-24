import matplotlib.pyplot as plt
import numpy as np

# Flower types
flower_types = ['Clover', 'Lavender', 'Wildflower', 'Sunflower', 
                'Bluebell', 'Dandelion', 'Buckwheat', 'Heather']

# Honey production (arbitrary units)
honey_production = np.array([150, 200, 180, 220, 160, 210, 190, 170])

# Convert flower types to angles in radians for the rose chart
num_categories = len(flower_types)
sector_angle = (2 * np.pi) / num_categories
theta = np.linspace(0.0, 2 * np.pi, num_categories, endpoint=False)

# Repeat the first value at the end to close the rose chart
radii = np.append(honey_production, honey_production[0])
theta = np.append(theta, theta[0])

# Plot the rose chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
bars = ax.bar(theta[:-1], radii[:-1], width=sector_angle, color=plt.cm.viridis(radii[:-1] / max(radii)), alpha=0.7, edgecolor='black')

# Add labels to each bar
for bar, angle, flower, production in zip(bars, theta[:-1], flower_types, radii[:-1]):
    rotation = np.rad2deg(angle) + 90  # Rotate label to be readable
    alignment = "left" if np.pi / 2 < angle < 3 * np.pi / 2 else "right"
    ax.text(angle, bar.get_height() + 10, f"{flower}\n{int(production)} units",
            ha=alignment, rotation=rotation, rotation_mode='anchor', fontsize=10, color='gray')

# Customize the rose chart
ax.set_title("Honey Production by Flower Type\nin the Enchanted World of Melis Terra", 
             fontsize=16, fontweight='bold', va='bottom')
ax.set_yticklabels([])
ax.set_xticks(theta)
ax.set_xticklabels([])  # Hide angle labels
ax.spines['polar'].set_visible(False)

# Add a legend outside the chart
ax.legend(bars, flower_types, loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()