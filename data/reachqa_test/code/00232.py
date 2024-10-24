import matplotlib.pyplot as plt
import numpy as np

# Define the superhero attributes
attributes = ['Strength', 'Agility', 'Intelligence', 'Stamina', 'Speed', 'Durability']
num_attributes = len(attributes)

# Superhero data
hero_alpha = [9, 5, 6, 8, 7, 9]
hero_beta = [6, 9, 7, 7, 9, 6]
hero_gamma = [7, 8, 10, 8, 6, 7]

# Prepare data
heroes_data = [hero_alpha, hero_beta, hero_gamma]
hero_names = ['Hero Alpha', 'Hero Beta', 'Hero Gamma']

# Calculate angles for each attribute
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Set up the radar chart framework
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f8f8f8')  # Light background color for enhanced contrast

# Draw the radar chart for each superhero
colors = ['#FF5733', '#33FF57', '#3357FF']
marker_styles = ['o', 's', 'D']  # Different markers for each hero

for i, hero_data in enumerate(heroes_data):
    data = hero_data + hero_data[:1]
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=hero_names[i], color=colors[i], marker=marker_styles[i])
    ax.fill(angles, data, color=colors[i], alpha=0.25)

# Add gridlines and custom radial labels
ax.set_yticklabels([])  # Remove y-tick labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=12, fontweight='bold')

# Add gridlines and scale labels
ax.yaxis.grid(True, linestyle='dashed', color='#CCCCCC')
ax.set_rscale('linear')
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=10)

# Title and legend
plt.title('Superhero Abilities Comparison\nRadar Chart', fontsize=18, fontweight='bold', color='#333333', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Heroes', title_fontsize='13', frameon=True)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()