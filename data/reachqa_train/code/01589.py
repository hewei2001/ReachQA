import matplotlib.pyplot as plt
import numpy as np

# Define the attributes and their values for each mythical creature
attributes = ['Strength', 'Agility', 'Intelligence', 'Magic', 'Charm', 'Defense']
n_attributes = len(attributes)

# Create data for each mythical creature
creatures = {
    'Dragon': [9, 6, 7, 8, 5, 9],
    'Unicorn': [4, 8, 9, 10, 10, 6],
    'Phoenix': [6, 9, 8, 9, 7, 5],
    'Siren': [5, 7, 8, 7, 10, 4]
}

# Calculate average scores across creatures for each attribute
average_scores = np.mean(list(creatures.values()), axis=0)

# Function to create a radar chart
def create_radar_chart(ax, data, attributes, title, color):
    angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
    data = data + data[:1]  # Complete the loop
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, fontsize=10)
    ax.set_title(title, size=15, color=color, pad=20)

# Create subplot layout: 1 row, 2 columns
fig, axes = plt.subplots(1, 2, figsize=(14, 6), subplot_kw=dict(polar=True))

# Plot radar charts for each mythical creature
creature_colors = {'Dragon': 'red', 'Unicorn': 'purple', 'Phoenix': 'orange', 'Siren': 'blue'}

for ax, (creature, values) in zip(axes, creatures.items()):
    create_radar_chart(ax, values, attributes, f'{creature} Abilities', creature_colors[creature])

# Creating an additional bar chart subplot for average scores
fig, ax2 = plt.subplots(figsize=(10, 6))
avg_bar_colors = ['#FF9999','#66B3FF','#99FF99','#FFCC99','#C2C2F0','#FFB3E6']
ax2.bar(attributes, average_scores, color=avg_bar_colors)

# Add labels, title, and grid for the bar chart
ax2.set_title('Average Abilities of Mythical Creatures\n(Comparative Analysis)', fontsize=14, pad=20)
ax2.set_xlabel('Attributes', fontsize=12)
ax2.set_ylabel('Average Score', fontsize=12)
ax2.grid(color='grey', linestyle='--', linewidth=0.5)
ax2.set_ylim(0, 11)

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plots
plt.show()