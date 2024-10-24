import matplotlib.pyplot as plt
import numpy as np

# Define categories and data
categories = ['Cost', 'Speed', 'Convenience', 'Env. Impact', 'Safety']
modes = ['Buses', 'Trains', 'Bicycles', 'Cars', 'Walking']

# Data for each transportation mode
data = {
    'Buses': [8, 6, 7, 5, 7],
    'Trains': [7, 9, 8, 8, 8],
    'Bicycles': [9, 5, 6, 9, 6],
    'Cars': [5, 8, 9, 4, 6],
    'Walking': [10, 3, 5, 10, 7]
}

# Number of variables
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Make the plot circular by repeating the first category
angles += angles[:1]

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each mode's data
colors = ['b', 'r', 'g', 'm', 'c']
for i, (mode, values) in enumerate(data.items()):
    # Repeat the first value to close the radar chart
    values += values[:1]
    ax.fill(angles, values, color=colors[i], alpha=0.25)
    ax.plot(angles, values, color=colors[i], linewidth=2, label=mode)

# Set labels for each angle
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Set title and legend
plt.title('Performance of Urban Transportation Systems\nin Metroville', size=14, color='navy', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Transportation Modes")

# Remove radial labels
ax.set_yticklabels([])

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()