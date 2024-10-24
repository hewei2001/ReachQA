import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Strength', 'Agility', 'Intelligence', 'Durability', 'Energy Manipulation']
n_categories = len(categories)

# Define the data for each superhero
hero1 = [9, 7, 6, 8, 9]  # Superhero A
hero2 = [7, 9, 8, 7, 5]  # Superhero B
hero3 = [6, 5, 9, 6, 7]  # Superhero C
hero4 = [8, 6, 7, 9, 6]  # Superhero D
hero5 = [5, 8, 6, 7, 9]  # Superhero E

# Combine the data and append the first value at the end to close the loop
heroes_data = np.array([hero1, hero2, hero3, hero4, hero5])
heroes_data = np.concatenate((heroes_data, heroes_data[:, [0]]), axis=1)

# Append the first category to close the circle in the radar chart
categories = categories + [categories[0]]

# Calculate the angles for each category
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]

# Calculate the average score for each superhero
average_scores = heroes_data.mean(axis=1)

# Initialize the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), subplot_kw={'polar': [True, False]})

# Radar chart for superhero abilities
names = ['Superhero A', 'Superhero B', 'Superhero C', 'Superhero D', 'Superhero E']
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#EE82EE']

for idx, hero in enumerate(heroes_data):
    ax1.fill(angles, hero, color=colors[idx], alpha=0.25, label=names[idx])
    ax1.plot(angles, hero, color=colors[idx], linewidth=2)

ax1.set_yticklabels([])
ax1.set_xticks(angles)  # Use all angles including the repeated one
ax1.set_xticklabels(categories, fontsize=10)
ax1.set_title("Superheroes' Abilities Overview", size=14, weight='bold', pad=20)

# Bar chart for average ability scores
x_pos = np.arange(len(names))
ax2.bar(x_pos, average_scores, color=colors, alpha=0.7)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(names, fontsize=10, rotation=30, ha='right')
ax2.set_ylabel('Average Ability Score', fontsize=12)
ax2.set_title('Average Ability Score per Superhero', size=14, weight='bold', pad=20)

# Add a legend with a bounding box to avoid overlap
ax1.legend(loc='upper right', bbox_to_anchor=(1.1, 1.2))

# Adjust layout
plt.tight_layout()

# Display the charts
plt.show()