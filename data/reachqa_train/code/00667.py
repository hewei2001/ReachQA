import matplotlib.pyplot as plt
import numpy as np

# Color preference ratings (1 to 10 scale) for different cultures
asian_preferences = [7, 8, 6, 9, 5, 7, 6, 8, 7, 9]
african_preferences = [8, 9, 7, 8, 9, 8, 7, 9, 8, 9]
european_preferences = [5, 6, 5, 7, 6, 5, 6, 7, 6, 8]
american_preferences = [6, 7, 7, 8, 6, 6, 8, 7, 8, 7]
oceanian_preferences = [7, 6, 8, 8, 6, 7, 6, 9, 8, 8]

# Aggregating data
data = [
    asian_preferences,
    african_preferences,
    european_preferences,
    american_preferences,
    oceanian_preferences
]

# Labels for the cultures
cultures = ["Asian", "African", "European", "American", "Oceanian"]

# Creating the horizontal box chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting boxplot
boxplots = ax.boxplot(data, vert=False, patch_artist=True,
                      boxprops=dict(facecolor='lightblue', color='darkblue'),
                      whiskerprops=dict(color='darkblue'),
                      capprops=dict(color='darkblue'),
                      medianprops=dict(color='red', linewidth=2),
                      flierprops=dict(marker='o', color='red', alpha=0.5))

# Customizing colors for each box
colors = ['lightcoral', 'lightgreen', 'lightskyblue', 'gold', 'lightpink']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Adding cultural labels
ax.set_yticklabels(cultures)

# Titles and labels
ax.set_title('Harmony in Colors: The Diversity of Artistic Preferences\nAcross Cultures', fontsize=16, pad=20)
ax.set_xlabel('Preference Rating (1-10)', fontsize=12)
ax.set_ylabel('Cultures', fontsize=12)

# Customizing grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend manually
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=culture) for color, culture in zip(colors, cultures)]
ax.legend(handles=legend_elements, title='Cultures', loc='upper right', fontsize=9)

# Automatically adjust the subplot params to give specified padding
plt.tight_layout()

# Display the plot
plt.show()