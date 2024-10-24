import matplotlib.pyplot as plt
import numpy as np

# Define additional attributes for more complexity
attributes = ['Bravery', 'Strength', 'Wisdom', 'Dexterity', 'Honor', 
              'Leadership', 'Charisma', 'Strategy', 'Endurance', 'Resilience']
n_attributes = len(attributes)

# Data for each knight with explicit values for clarity
lancelot = [9, 10, 7, 8, 9, 9, 8, 7, 8, 7]
gawain = [8, 7, 9, 7, 10, 7, 8, 9, 8, 9]
percival = [10, 8, 8, 9, 7, 8, 9, 8, 7, 10]
galahad = [7, 9, 8, 6, 9, 10, 10, 9, 7, 8]
bors = [6, 8, 9, 7, 8, 8, 7, 9, 10, 9]

# Append the first value to close the radar chart
for knight in [lancelot, gawain, percival, galahad, bors]:
    knight += knight[:1]

# Calculate angles for each attribute
angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the figure and axis for the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], attributes, fontsize=10, fontweight='bold', color='navy')

# Plot each knight's attribute data
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
knight_names = ['Sir Lancelot', 'Sir Gawain', 'Sir Percival', 'Sir Galahad', 'Sir Bors']
knight_data = [lancelot, gawain, percival, galahad, bors]

for idx, knight in enumerate(knight_data):
    ax.plot(angles, knight, color=colors[idx], linewidth=2, linestyle='solid', label=knight_names[idx])
    ax.fill(angles, knight, color=colors[idx], alpha=0.15)

# Enhance chart aesthetics
ax.set_yticklabels([])
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend with a title, ensuring it doesn't obscure the plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), title='Legendary Knights', fontsize=9)

# Set the title of the chart with a line break
plt.title('Attributes of Legendary Knights\nin the Realm of Astoria', size=16, fontweight='bold', pad=30, color='darkslategray')

# Automatically adjust the layout to prevent overlapping text
plt.tight_layout()

# Display the radar chart
plt.show()