import matplotlib.pyplot as plt
import numpy as np

# Define the performance metrics categories
categories = ['Speed', 'Durability', 'Cargo Capacity', 'Fuel Efficiency', 'Stealth Capability']

# Data for each spaceship
spaceship_data = {
    'Galactic Explorer': [8, 6, 7, 5, 8],
    'Star Voyager': [7, 7, 6, 8, 5],
    'Nebula Runner': [6, 8, 9, 7, 7]
}

# Convert categories to a numpy array and close the circle by appending the first category
labels = np.array(categories)

# Prepare data for plotting, closing the circle for each spaceship
data_entries = {name: np.array(values + [values[0]]) for name, values in spaceship_data.items()}

# Compute angles for each axis
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Define colors for each spaceship
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each spaceship's performance
for (name, data), color in zip(data_entries.items(), colors):
    ax.fill(angles, data, color=color, alpha=0.25, label=name)
    ax.plot(angles, data, color=color, linewidth=2, label=f'{name} Performance')

# Customize the radar chart
ax.set_xticks(angles[:-1])  # Adjust the xticks to exclude the closing angle
ax.set_xticklabels(labels, fontsize=10)
ax.set_yticklabels([])
ax.set_title('Intergalactic Spaceship\nPerformance Radar', size=15, weight='bold', pad=20)

# Add a legend outside the plot
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.05), title="Spaceships", frameon=False)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the radar chart
plt.show()