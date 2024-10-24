import matplotlib.pyplot as plt
import numpy as np

# Data: Observation hours of key planets by astronomy clubs
observation_hours = {
    'Mercury': [12, 15, 10, 9, 11],
    'Venus': [25, 28, 30, 35, 27],
    'Mars': [40, 42, 38, 45, 43],
    'Jupiter': [55, 53, 58, 60, 56],
    'Saturn': [30, 32, 31, 29, 33],
}

# Prepare data for boxplot
data = [observation_hours[planet] for planet in observation_hours.keys()]

# Calculate means for overlay line plot
means = [np.mean(observation_hours[planet]) for planet in observation_hours.keys()]

# Create horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the boxplot
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customizing color scheme for boxes
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Overlay line plot for means
ax.plot(means, range(1, len(means) + 1), marker='o', linestyle='--', color='#ff7f00', label='Mean Observation Hours')

# Setting labels and title
ax.set_yticklabels(observation_hours.keys(), fontsize=12)
ax.set_xlabel('Observation Hours', fontsize=12)
ax.set_title('Observational Trends in Planetary Studies\nUsing Telescopes: 2023 Analysis', fontsize=14, fontweight='bold')

# Adding a grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Customize legend
plt.legend(loc="upper right", fontsize=10, title_fontsize='13')

# Annotate mean points
for i, mean in enumerate(means):
    ax.annotate(f'{mean:.1f}', (mean, i + 1), textcoords="offset points", xytext=(-15, 5), ha='center', fontsize=10, color='#ff7f00')

# Adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()