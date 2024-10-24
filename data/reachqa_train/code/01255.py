import matplotlib.pyplot as plt
import numpy as np

# Data for discovery methods
methods = ['Transit Method', 'Radial Velocity', 'Direct Imaging', 'Gravitational Microlensing', 'Astrometry']
proportions = [45, 30, 10, 10, 5]

# Colors for each segment
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect='equal'))

# Draw the ring chart
wedges, texts = ax.pie(proportions, colors=colors, startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'))

# Customize the wedge labels with percentages
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2.0 + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(angle)
    ax.annotate(f'{methods[i]}: {proportions[i]}%', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=11,
                arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle, color='gray'))

# Adding a center circle to label or decorate
center_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(center_circle)

# Title and center text
plt.title('Celestial Exploration:\nPlanetary Discovery Methods (2023)', fontsize=16, weight='bold', pad=20)
ax.text(0, 0, 'Planetary Discoveries', horizontalalignment='center', verticalalignment='center', fontsize=12, color='gray')

# Legend for methods
ax.legend(wedges, methods, title="Discovery Methods", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()