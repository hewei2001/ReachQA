import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define superhero categories
categories = ['Combat Skills', 'Intelligence', 'Speed', 'Power', 'Endurance']

# Number of variables
num_vars = len(categories)

# Define abilities of each superhero (normalized scale of 1-10)
captain_valor = [9, 7, 6, 8, 9]
shadow_knight = [8, 9, 7, 6, 8]
electro_girl = [6, 8, 9, 7, 6]
terra_quake = [7, 6, 8, 9, 7]

# List of superheroes' abilities
superheroes = [captain_valor, shadow_knight, electro_girl, terra_quake]
superhero_names = ['Captain Valor', 'Shadow Knight', 'Electro Girl', 'Terra Quake']

# Calculate angles for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the circle

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each superhero's data
for i, hero in enumerate(superheroes):
    data = hero + hero[:1]  # Complete the loop
    ax.plot(angles, data, label=superhero_names[i], linewidth=2)
    ax.fill(angles, data, alpha=0.25)

# Configure chart aesthetics
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='navy')
ax.set_title("Superhero Attribute Comparison\nin the Heroic Chronicles Universe", fontsize=16, fontweight='bold', pad=30)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Superheroes")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()