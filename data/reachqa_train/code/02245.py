import matplotlib.pyplot as plt
import numpy as np

# Define the labels for each skill
skills = ['Navigation', 'Climbing', 'Survival Tactics', 'Foraging', 'Combat']

# Skill levels for the adventurer
skill_levels = [7, 5, 9, 6, 8]
skill_levels += skill_levels[:1]

# Average skill levels (overlay line plot)
average_skill_levels = [6, 7, 7.5, 5, 6.5]
average_skill_levels += average_skill_levels[:1]

# Calculate the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot the adventurer's skill levels
ax.plot(angles, skill_levels, color='steelblue', linewidth=2, label='Adventurer')
ax.fill(angles, skill_levels, color='skyblue', alpha=0.4)

# Overlay: plot the average skill levels
ax.plot(angles, average_skill_levels, color='darkorange', linewidth=2, linestyle='dashed', label='Average')
ax.fill(angles, average_skill_levels, color='orange', alpha=0.1)

# Add labels for each skill on the chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, color='navy', fontsize=10)

# Remove radial labels
ax.set_yticklabels([])

# Customize the grid lines
ax.grid(color='gray', linestyle='dotted')

# Set radial limits
ax.set_ylim(0, 10)

# Annotate the chart with skill level
ax.text(0, 10, 'Skill Level (0-10)', ha='center', va='center', fontsize=10, color='darkred')

# Add a legend with distinctive styling
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title='Skill Level Comparison', title_fontsize='12')

# Set title with line breaks for clarity
plt.title('Adventure Traveler Skills Assessment\nand Average Skill Levels Comparison', 
          size=14, color='darkblue', weight='bold', pad=30)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the radar chart
plt.show()