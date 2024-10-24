import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Navigation', 'Communication', 'Problem-solving', 'Resource Management', 'Environmental Analysis']
N = len(categories)

# Hypothetical data for each AstroBot
astrobot_a = [7, 5, 8, 6, 7]
astrobot_b = [6, 7, 7, 8, 6]
astrobot_c = [8, 6, 7, 7, 9]

# Repeat the first value at the end to close the radar chart
astrobot_a += astrobot_a[:1]
astrobot_b += astrobot_b[:1]
astrobot_c += astrobot_c[:1]

# Calculate the angles for the radar chart (one extra to close the chart)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each AstroBot's data
ax.fill(angles, astrobot_a, color='teal', alpha=0.25)
ax.fill(angles, astrobot_b, color='orange', alpha=0.25)
ax.fill(angles, astrobot_c, color='purple', alpha=0.25)

# Plot lines for each AstroBot
ax.plot(angles, astrobot_a, color='teal', linewidth=2, label='AstroBot A')
ax.plot(angles, astrobot_b, color='orange', linewidth=2, label='AstroBot B')
ax.plot(angles, astrobot_c, color='purple', linewidth=2, label='AstroBot C')

# Set category labels for each angle
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Title with line breaks for better readability
plt.title('Robotic Competence Evaluation\nin Space Missions - 2045', size=14, color='navy', y=1.1)

# Legend positioned to avoid occlusion
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Add gridlines for clarity
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust the layout to avoid overlap
plt.tight_layout()

# Display the radar chart
plt.show()