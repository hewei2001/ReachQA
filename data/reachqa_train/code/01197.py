import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define organizations
organizations = ['NASA', 'ESA', 'SpaceX']

# Define efficiency metrics
metrics = ['Mission Success Rate', 'Cost Efficiency', 'Tech Innovation', 'Scientific Output', 'Public Engagement']

# Efficiency data for each organization
data = [
    [90, 75, 85, 90, 70],  # NASA
    [85, 80, 80, 85, 65],  # ESA
    [95, 85, 90, 88, 80]   # SpaceX
]

# Convert data into a format suitable for plotting
data = np.array(data)

# Number of metrics
num_vars = len(metrics)

# Compute the angle for each metric
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for plotting

# Set up the radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each organization's data
for i, organization_data in enumerate(data):
    values = organization_data.tolist()
    values += values[:1]  # Complete the loop for plotting
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=organizations[i])
    ax.fill(angles, values, alpha=0.25)

# Add labels for each metric
plt.xticks(angles[:-1], metrics, color='grey', size=10)

# Set y-labels
ax.set_rlabel_position(30)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)

# Add a title
plt.title('Exploration Efficiency in Space Missions\nA Comparative Radar Analysis', size=14, color='navy', pad=20)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()