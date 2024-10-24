import matplotlib.pyplot as plt
import numpy as np

# Data for mythical creature sightings
creatures = ['Dragon', 'Unicorn', 'Phoenix', 'Mermaid', 'Griffin', 'Centaur']
sightings = [150, 120, 80, 100, 60, 90]
characteristics = [
    "Fiery and Majestic", 
    "Graceful and Magical", 
    "Rebirth from Ashes", 
    "Mysterious and Alluring", 
    "Guardian of Treasures", 
    "Dual Natured and Wise"
]

# Additional data for average magical power levels
magical_power = [95, 85, 88, 70, 60, 75]  # Hypothetical values
power_descriptions = [
    "Extraordinarily Powerful", 
    "Eminently Graceful", 
    "Immortally Reborn", 
    "Underwater Enchantment", 
    "Treasure Guardian", 
    "Strategically Wise"
]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart for sightings
bar_positions = np.arange(len(creatures))
colors = ['#FF6347', '#FFD700', '#FF4500', '#1E90FF', '#8A2BE2', '#7FFF00']
bars1 = ax1.bar(bar_positions, sightings, color=colors, width=0.6)
ax1.set_title('Enchanted Encounters:\nMythical Creature Sightings', fontsize=16, weight='bold')
ax1.set_xlabel('Mythical Creatures', fontsize=12)
ax1.set_ylabel('Number of Sightings', fontsize=12)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(creatures, rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for bar, characteristic in zip(bars1, characteristics):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 2, characteristic, ha='center', va='bottom', fontsize=10, style='italic')

# Radar chart for magical power
def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)
    if frame == 'circle':
        def draw_polygon(ax):
            ax.set_xticks(theta)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
    draw_polygon = draw_polygon
    return theta, draw_polygon

theta, _ = radar_factory(len(creatures))
ax2.set_title("Magical Power Level Comparison", fontsize=16, weight='bold')
ax2 = plt.subplot(122, polar=True)
ax2.set_ylim(0, 100)
ax2.fill(theta, magical_power, color='cyan', alpha=0.25)
ax2.plot(theta, magical_power, color='blue', marker='o')

ax2.set_xticks(theta)
ax2.set_xticklabels(creatures)
ax2.set_yticks([20, 40, 60, 80, 100])
ax2.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8)

# Auto-adjust layout
plt.tight_layout()

# Display the plots
plt.show()