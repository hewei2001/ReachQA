import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ingredients and schools
ingredients = ["Dragon Scale", "Phoenix Feather", "Unicorn Horn", "Mermaid Tears", "Fairy Dust"]
schools = ["Hogwarts", "Beauxbatons", "Durmstrang"]

# Popularity percentages at each school (3D bar plot data)
popularity = np.array([
    [35, 20, 15, 10, 20],  # Hogwarts
    [20, 30, 25, 15, 10],  # Beauxbatons
    [10, 25, 30, 20, 15],  # Durmstrang
])

# Difficulty to acquire for each ingredient at each school (Radar chart data)
difficulty = np.array([
    [40, 50, 60, 45, 55],  # Hogwarts
    [55, 45, 50, 60, 65],  # Beauxbatons
    [50, 60, 55, 50, 45],  # Durmstrang
])

fig = plt.figure(figsize=(16, 8))

# 3D Bar Plot
ax1 = fig.add_subplot(121, projection='3d')

x, y = np.meshgrid(np.arange(len(ingredients)), np.arange(len(schools)))
x = x.flatten()
y = y.flatten()
z = np.zeros_like(x)
dx = dy = 0.6
dz = popularity.flatten()
colors = ['#FF9999', '#66B2FF', '#99FF99']

ax1.bar3d(x, y, z, dx, dy, dz, color=[colors[i % len(schools)] for i in y], alpha=0.9, edgecolor='k')
ax1.set_xlabel('Ingredients', fontsize=11, labelpad=45)
ax1.set_ylabel('Schools', fontsize=11, labelpad=15)
ax1.set_zlabel('Popularity (%)', fontsize=11, labelpad=10)
ax1.set_zlim(0, 50)
ax1.set_xticks(np.arange(len(ingredients)) + dx / 2)
ax1.set_yticks(np.arange(len(schools)) + dy / 2)
ax1.set_xticklabels(ingredients, rotation=45, ha='right', fontsize=10)
ax1.set_yticklabels(schools, fontsize=10)
ax1.set_title('Popularity of Magical Potion Ingredients\nAcross Potion-Making Schools', fontsize=14, fontweight='bold', pad=20)

# Radar Chart
ax2 = fig.add_subplot(122, polar=True)

angles = np.linspace(0, 2 * np.pi, len(ingredients), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

for i, school in enumerate(schools):
    values = difficulty[i].tolist()
    values += values[:1]
    ax2.plot(angles, values, color=colors[i], linewidth=2, label=school)
    ax2.fill(angles, values, color=colors[i], alpha=0.25)

ax2.set_yticklabels([])
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(ingredients, fontsize=10)
ax2.set_title("Difficulty to Acquire Ingredients\nby School", fontsize=14, fontweight='bold', pad=20)
ax2.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=10)

plt.tight_layout()
plt.show()