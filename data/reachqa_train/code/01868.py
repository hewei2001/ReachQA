import matplotlib.pyplot as plt
import numpy as np

# Define the attributes for Quidditch team performance
attributes = ['Speed', 'Strategy', 'Teamwork', 'Spirit', 'Accuracy', 'Defense']
n_attributes = len(attributes)

# Data for each Quidditch team
gryffindor = [9, 8, 7, 10, 9, 6]
slytherin = [8, 9, 8, 7, 10, 7]
ravenclaw = [7, 9, 9, 6, 8, 9]
hufflepuff = [8, 7, 8, 8, 7, 9]

# Append the first value to close the radar chart
for team in [gryffindor, slytherin, ravenclaw, hufflepuff]:
    team += team[:1]

# Calculate angles for each attribute
angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

# Set up the figure and axis for the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Plot background with subtle gradient
ax.set_facecolor('whitesmoke')
ax.spines['polar'].set_visible(False)

# Add labels
plt.xticks(angles[:-1], attributes, fontsize=11, fontweight='bold', color='midnightblue')

# Define markers and colors
colors = ['#ff6f61', '#6a5acd', '#20b2aa', '#ffd700']
markers = ['o', 's', 'D', 'x']
team_names = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
team_data = [gryffindor, slytherin, ravenclaw, hufflepuff]

# Plot each team's attribute data
for idx, team in enumerate(team_data):
    ax.plot(angles, team, color=colors[idx], linewidth=2, linestyle='solid', label=team_names[idx], marker=markers[idx], markersize=6)
    ax.fill(angles, team, color=colors[idx], alpha=0.1)

# Customization of grid and lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_yticks([])

# Add a legend with a title
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Teams', fontsize=9)

# Add a title
plt.title('Performance Attributes of Teams\nin the Fantasy Quidditch League', 
          size=15, fontweight='bold', pad=30, color='darkred')

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()