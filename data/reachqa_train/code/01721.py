import matplotlib.pyplot as plt
import numpy as np

# Define player names and performance metrics
players = ['Thunderfoot', 'Speedy', 'Wall', 'Sniper', 'Maestro']
skills = ['Dribbling', 'Shooting', 'Passing', 'Stamina', 'Defense']

# Performance data for each player (values between 1 and 10)
performance_data = [
    [6, 9, 7, 6, 5],  # Thunderfoot
    [9, 5, 6, 8, 5],  # Speedy
    [5, 6, 7, 7, 9],  # Wall
    [7, 10, 5, 5, 6], # Sniper
    [8, 7, 9, 6, 6]   # Maestro
]

# Close the data loops for radar chart
performance_data = [np.array(player + [player[0]]) for player in performance_data]

# Number of variables
num_vars = len(skills)

# Calculate angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # close the radar chart loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one line per player
for idx, (player_data, player) in enumerate(zip(performance_data, players)):
    ax.plot(angles, player_data, linewidth=2, label=player, linestyle='-', marker='o')
    ax.fill(angles, player_data, alpha=0.25)

# Set the angle for each axis and add labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='navy')

# Add a title and a legend
plt.title("Performance Metrics of Star Players\nin Fantasy Football", size=15, color='darkred', y=1.08)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10)

# Add grid for clarity
ax.grid(color='grey', linestyle='--', linewidth=0.5)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()