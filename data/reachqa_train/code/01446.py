import matplotlib.pyplot as plt
import numpy as np

# Define categories for coffee evaluation
categories = ['Aroma', 'Acidity', 'Body', 'Sweetness', 'Bitterness', 'Aftertaste']

# Data for coffee blends (ratings on a scale from 1 to 10)
coffee_data = {
    'Colombian Supremo': [8, 7, 6, 7, 5, 6],
    'Ethiopian Yirgacheffe': [9, 8, 5, 6, 4, 8],
    'Brazilian Santos': [6, 5, 7, 8, 5, 7]
}

# Hypothetical average satisfaction scores for reference
average_satisfaction = [7.5, 6.5, 6, 6.5, 5, 7]

# Convert data to numpy array and complete the circle
labels = np.array(categories)
data_entries = {name: np.array(values + [values[0]]) for name, values in coffee_data.items()}
avg_satisfaction_entry = np.array(average_satisfaction + [average_satisfaction[0]])

# Compute angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Define colors for each coffee blend
colors = ['#8B4513', '#D2691E', '#A0522D']

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each coffee blend's sensory profile
for (name, data), color in zip(data_entries.items(), colors):
    ax.fill(angles, data, color=color, alpha=0.3, label=name)
    ax.plot(angles, data, color=color, linewidth=2)

# Overlay plot for average satisfaction scores
ax.plot(angles, avg_satisfaction_entry, color='black', linewidth=2, linestyle='--', label='Avg Satisfaction')
ax.fill(angles, avg_satisfaction_entry, color='grey', alpha=0.1)

# Customize the radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.set_yticklabels([])  # Hide radial labels
ax.set_ylim(0, 10)

# Add multi-line title and legend
ax.set_title('Global Gourmet Coffee Flavor Profiles\nand Average Consumer Satisfaction', size=14, weight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Profiles", frameon=False)

# Automatically adjust layout
plt.tight_layout()

# Display radar chart
plt.show()