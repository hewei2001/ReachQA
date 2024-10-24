import matplotlib.pyplot as plt
import numpy as np

# Define data for different activities: hours spent by Enchanters daily
spell_crafting_hours = np.array([2, 3, 3.5, 4, 5, 4.5, 3.7, 3.2, 4.1, 3.8, 4.2, 3.9, 5.1, 3.6, 4.4])
potion_brewing_hours = np.array([1, 1.5, 2, 2.5, 3, 2.7, 2.1, 1.9, 2.6, 2.3, 2.8, 2.0, 3.1, 1.8, 2.4])
dragon_taming_hours = np.array([0.5, 1, 0.7, 0.8, 1.5, 1.2, 1.3, 1.1, 0.9, 1.4, 1.6, 1.7, 1.0, 1.2, 1.3])
elden_tree_meditation_hours = np.array([3, 2.8, 3.5, 4, 5.2, 4.6, 4.3, 4.9, 4.1, 5, 4.7, 4.2, 5.1, 3.9, 4.5])
rune_deciphering_hours = np.array([1.2, 2.3, 1.8, 2.4, 3.3, 2.5, 3.1, 3.0, 2.8, 2.9, 3.2, 2.2, 3.0, 2.7, 2.6])

# Compile data into a list
data = [
    spell_crafting_hours, 
    potion_brewing_hours, 
    dragon_taming_hours, 
    elden_tree_meditation_hours,
    rune_deciphering_hours
]

# Labels for each activity
labels = [
    'Spell Crafting', 
    'Potion Brewing', 
    'Dragon Taming', 
    'Elden Tree Meditation',
    'Rune Deciphering'
]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a box plot with notches and color fill
bp = ax.boxplot(data, patch_artist=True, labels=labels, notch=True)

# Customize boxplot colors
colors = ['#8c564b', '#2ca02c', '#d62728', '#1f77b4', '#9467bd']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)  # Add transparency

# Style whiskers, caps, medians
plt.setp(bp['whiskers'], color='grey', linestyle='--')
plt.setp(bp['caps'], color='grey', linewidth=1.5)
plt.setp(bp['medians'], color='gold', linewidth=2)

# Title and labels
ax.set_title(
    "Time Usage in Enchanted Realms:\nA Comprehensive Analysis of Enchanters' Daily Activities",
    fontsize=14, fontweight='bold', pad=20
)
ax.set_ylabel("Hours Spent", fontsize=12)
ax.set_xlabel("Activities", fontsize=12)

# Add a horizontal grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add annotations for median values
medians = [np.median(activity) for activity in data]
for i, median in enumerate(medians, start=1):
    ax.annotate(f'{median:.1f}', xy=(i, median), xytext=(0, -15),
                textcoords='offset points', ha='center', fontsize=10, color='black')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()