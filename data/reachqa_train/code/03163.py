import matplotlib.pyplot as plt
import numpy as np

# Data: Number of visitors by genre preference each day
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4']
genres = ['Rock', 'Pop', 'Jazz', 'Electronic', 'Hip-Hop']
attendance = np.array([
    [250, 200, 100, 150, 100],  # Day 1
    [300, 250, 150, 180, 130],  # Day 2
    [350, 300, 180, 200, 160],  # Day 3
    [400, 350, 200, 220, 180]   # Day 4
])

# Calculate number of genres and define angles for each sector
num_genres = len(genres)
angles = np.linspace(0, 2 * np.pi, num_genres, endpoint=False).tolist()

# Create a color palette for days
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Set up the figure and axis for polar plot
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Plot each day's data
for i, day in enumerate(days):
    values = np.append(attendance[i], attendance[i][0])  # Closing the circle
    angle_values = np.append(angles, angles[0])
    ax.fill(angle_values, values, color=colors[i % len(colors)], alpha=0.3, label=day)
    ax.plot(angle_values, values, color=colors[i % len(colors)], linewidth=1.5)

# Customize the plot appearance
ax.set_theta_offset(np.pi / 2)  # Start from the top
ax.set_theta_direction(-1)      # Clockwise

# Set the labels for each genre
ax.set_thetagrids(np.degrees(angles), genres, fontsize=11, fontweight='bold')

# Title and legend
ax.set_title("Harmony Music Festival 2023\nGenre Preferences by Day", fontsize=14, fontweight='bold', pad=20)
plt.legend(title='Festival Days', loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Automatically adjust the layout for readability
plt.tight_layout()

# Display the plot
plt.show()