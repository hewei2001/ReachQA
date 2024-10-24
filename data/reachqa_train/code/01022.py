import matplotlib.pyplot as plt
import numpy as np

# Define the attributes and the legendary knights
attributes = ['Bravery', 'Strength', 'Wisdom', 'Dexterity', 'Honor']
n_attributes = len(attributes)

# Data for each knight
lancelot = [9, 10, 7, 8, 9]
gawain = [8, 7, 9, 7, 10]
percival = [10, 8, 8, 9, 7]

# Append the first value to close the radar chart
lancelot += lancelot[:1]
gawain += gawain[:1]
percival += percival[:1]

# Calculate angles for each attribute
angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the figure and axis for the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold')

# Plot each knight's attribute data
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Distinct colors for each knight
knight_names = ['Sir Lancelot', 'Sir Gawain', 'Sir Percival']
knight_data = [lancelot, gawain, percival]

for idx, knight in enumerate(knight_data):
    ax.plot(angles, knight, color=colors[idx], linewidth=2, linestyle='solid', label=knight_names[idx])
    ax.fill(angles, knight, color=colors[idx], alpha=0.25)

# Remove y-tick labels for cleaner look
ax.set_yticklabels([])

# Add a legend with a title
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1), title='Legendary Knights')

# Set the title of the chart
plt.title('Attributes of Legendary Knights in Astoria', size=16, fontweight='bold', pad=20)

# Automatically adjust the layout to prevent overlapping text
plt.tight_layout()

# Display the radar chart
plt.show()