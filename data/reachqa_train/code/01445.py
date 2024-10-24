import matplotlib.pyplot as plt
import numpy as np

# Define categories to evaluate coffee blends
categories = ['Aroma', 'Acidity', 'Body', 'Sweetness', 'Bitterness', 'Aftertaste']

# Data for each coffee blend (ratings on a scale from 1 to 10)
coffee_data = {
    'Colombian Supremo': [8, 7, 6, 7, 5, 6],
    'Ethiopian Yirgacheffe': [9, 8, 5, 6, 4, 8],
    'Brazilian Santos': [6, 5, 7, 8, 5, 7]
}

# Convert categories to a numpy array and complete the circle by appending the first category
labels = np.array(categories)
data_entries = {name: np.array(values + [values[0]]) for name, values in coffee_data.items()}

# Compute angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Define colors for each coffee blend
colors = ['#8B4513', '#D2691E', '#A0522D']

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each coffee blend's sensory profile
for (name, data), color in zip(data_entries.items(), colors):
    ax.fill(angles, data, color=color, alpha=0.3, label=name)
    ax.plot(angles, data, color=color, linewidth=2)

# Customize the radar chart
ax.set_xticks(angles[:-1])  # Set x-ticks to exclude closing angle
ax.set_xticklabels(labels, fontsize=10)
ax.set_yticklabels([])  # No radial labels
ax.set_ylim(0, 10)  # Set the same scale for all dimensions
ax.set_title('Global Gourmet Coffee Flavor Profiles:\nA Sensory Journey', size=15, weight='bold', pad=20)

# Add legend to the chart
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Coffee Blends", frameon=False)

# Automatically adjust layout
plt.tight_layout()

# Display radar chart
plt.show()