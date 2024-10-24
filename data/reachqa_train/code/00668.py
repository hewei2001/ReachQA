import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Preference data for cultures (on a scale from 1 to 10)
asian_preferences = [7, 8, 6, 9, 5, 7, 6, 8, 7, 9]
african_preferences = [8, 9, 7, 8, 9, 8, 7, 9, 8, 9]
european_preferences = [5, 6, 5, 7, 6, 5, 6, 7, 6, 8]
american_preferences = [6, 7, 7, 8, 6, 6, 8, 7, 8, 7]
oceanian_preferences = [7, 6, 8, 8, 6, 7, 6, 9, 8, 8]

# Aggregating data for boxplot
data = [
    asian_preferences,
    african_preferences,
    european_preferences,
    american_preferences,
    oceanian_preferences
]

# Labels for the cultures
cultures = ["Asian", "African", "European", "American", "Oceanian"]

# Creating subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 8))

# Plotting the boxplot
boxplots = axs[0].boxplot(data, vert=False, patch_artist=True,
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
axs[0].set_yticklabels(cultures)

# Titles and labels
axs[0].set_title('Harmony in Colors:\nDiversity of Artistic Preferences Across Cultures', fontsize=14, pad=20)
axs[0].set_xlabel('Preference Rating (1-10)', fontsize=12)
axs[0].set_ylabel('Cultures', fontsize=12)

# Customizing grid
axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend manually
legend_elements = [Patch(facecolor=color, label=culture) for color, culture in zip(colors, cultures)]
axs[0].legend(handles=legend_elements, title='Cultures', loc='upper right', fontsize=9)

# Creating a bar plot for average preference
average_preferences = [np.mean(pref) for pref in data]
axs[1].barh(cultures, average_preferences, color=colors)

# Titles and labels for bar chart
axs[1].set_title('Average Color Preferences by Culture', fontsize=14, pad=20)
axs[1].set_xlabel('Average Preference Rating', fontsize=12)
axs[1].set_ylabel('')

# Customizing bar chart grid
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()