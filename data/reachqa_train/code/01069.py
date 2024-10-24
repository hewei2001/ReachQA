import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define programming languages
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Go']
N = len(languages)

# Proficiency levels for the development team
proficiency_levels = [9, 8, 7, 5, 6, 4]
proficiency_levels += proficiency_levels[:1]  # Loop closure

# Calculate angles for each language
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Customize the grid and labels
ax.yaxis.grid(True, color='lightblue', linestyle='dotted')
ax.xaxis.grid(True, color='blue', linestyle='solid', linewidth=0.7)
ax.spines['polar'].set_visible(False)  # Remove the outermost frame

# Draw one axe per variable with labels
plt.xticks(angles[:-1], languages, color='blue', size=10, fontweight='bold')

# Define y-axis ticks with enhanced labels
ax.set_rscale('linear')
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
plt.ylim(0, 10)

# Plot the data with enhanced styling
ax.plot(angles, proficiency_levels, linewidth=2.5, linestyle='-', color='dodgerblue', marker='o', markersize=8, label="Team Proficiency")
ax.fill(angles, proficiency_levels, 'skyblue', alpha=0.25)

# Title and Legend with improved formatting
plt.title('Proficiency Levels in\nModern Programming Languages', size=16, color='darkblue', loc='center', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize='medium', title="Team", title_fontsize='medium')

# Adjust layout for readability
plt.tight_layout()

# Display the radar chart
plt.show()