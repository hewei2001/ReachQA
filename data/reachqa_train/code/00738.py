import numpy as np
import matplotlib.pyplot as plt

# Define categories and months
categories = ['Wildflowers', 'Shrubs', 'Trees', 'Perennials', 'Annuals']
months = np.arange(1, 13)

# Artificial data representing the number of plant varieties blooming each month
wildflowers = [5, 8, 10, 12, 15, 18, 20, 18, 15, 10, 8, 5]
shrubs = [3, 4, 6, 8, 10, 12, 12, 10, 8, 6, 4, 3]
trees = [2, 3, 5, 6, 8, 9, 7, 6, 5, 3, 2, 2]
perennials = [4, 5, 7, 9, 11, 13, 14, 13, 11, 8, 5, 4]
annuals = [1, 2, 3, 5, 8, 12, 15, 14, 11, 7, 3, 1]

# Stack the data for plotting
data = np.array([wildflowers, shrubs, trees, perennials, annuals])

# Set colors for each category
colors = ['#FF8C00', '#556B2F', '#8B4513', '#4682B4', '#C71585']

# Calculate angles for each month
angles = np.linspace(0, 2 * np.pi, len(months), endpoint=False).tolist()

# Add the first month at the end to close the plot
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each category on the rose chart
for i, category in enumerate(categories):
    ax.fill(angles, data[i], color=colors[i], alpha=0.25, label=category)
    ax.plot(angles, data[i], color=colors[i], linewidth=2)

# Add labels for each month
ax.set_xticks(angles[:-1])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Set the title and customize the chart
ax.set_title('Pollinator Planting Guide:\nSeasonal Bloom Contribution', va='bottom', fontsize=14, fontweight='bold')
ax.set_yticklabels([])
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Plant Categories", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()