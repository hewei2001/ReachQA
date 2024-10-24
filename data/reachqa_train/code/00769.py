import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# Define the categories for the radar chart
categories = ['Creativity', 'Technical Skill', 'Originality', 'Emotion', 'Audience Engagement']
num_vars = len(categories)

# Define the data for each art style
classical_art = [8, 9, 6, 7, 8]
modern_art = [9, 8, 9, 9, 7]
digital_design = [7, 8, 8, 6, 9]
street_art = [8, 7, 9, 8, 8]
minimalism = [6, 7, 5, 6, 7]

# Aggregate data
art_styles = [classical_art, modern_art, digital_design, street_art, minimalism]
labels = ['Classical Art', 'Modern Art', 'Digital Design', 'Street Art', 'Minimalism']

# Compute the angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Setup the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw radar chart grid with custom gridlines
gridline_styles = {'linewidth': 0.8, 'linestyle': '--', 'color': 'grey', 'alpha': 0.5}
ax.yaxis.grid(True, **gridline_styles)
ax.xaxis.grid(True, linewidth=0.5, linestyle='-', color='black', alpha=0.7)

# Set radar chart limits
ax.set_ylim(0, 10)

# Data point markers and line style
markers = ['o', 's', '^', 'D', '*']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33B5', '#FF8C33']

# Draw one line per art style with different markers
for i, style_data in enumerate(art_styles):
    data = style_data + style_data[:1]  # to close the radar chart
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=labels[i], color=colors[i], marker=markers[i])
    ax.fill(angles, data, alpha=0.25, color=colors[i])

# Customize the labels for each slice of the chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13, fontweight='bold', color='navy')

# Set the yticks, not labeling them directly to keep chart clean
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([])

# Enhance the legend for clarity
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.2), fontsize=10, title='Art Styles')
legend.get_title().set_fontsize('12')

# Use a bounding box to improve aesthetics of the legend
for text in legend.get_texts():
    text.set_ha('left')

# Draw a fancy bounding box around the legend
bbox = FancyBboxPatch((1.1, 1.1), 0.35, 0.2, boxstyle="round,pad=0.2", fc="white", ec="black", lw=0.5)
ax.add_patch(bbox)

# Title of the plot with a line break for readability
plt.title('Creative Expressions:\nEvaluating Key Elements in Art and Design',
          fontsize=16, fontweight='bold', color='darkslateblue', pad=30)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()