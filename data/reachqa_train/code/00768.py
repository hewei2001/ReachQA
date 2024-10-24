import matplotlib.pyplot as plt
import numpy as np

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

# Repeat the first value to close the radar chart
angles += angles[:1]

# Setup the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw one line per art style
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33B5', '#FF8C33']
for i, style_data in enumerate(art_styles):
    data = style_data + style_data[:1]  # to close the radar chart
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=labels[i], color=colors[i])
    ax.fill(angles, data, alpha=0.25, color=colors[i])

# Customize the labels for each slice of the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Add a legend with a slight offset to avoid crowding
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Art Styles')

# Title of the plot with a line break for readability
plt.title('Creative Expressions:\nEvaluating Key Elements in Art and Design', fontsize=15, fontweight='bold', pad=20)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()