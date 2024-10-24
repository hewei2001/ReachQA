import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Define the factors
labels = ['Cost of Living', 'Internet Quality', 'Community', 'Safety', 'Climate']
num_vars = len(labels)

# Calculate angles for each factor axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Data for each location
bali_scores = [8, 7, 6, 5, 8]
lisbon_scores = [6, 8, 7, 9, 5]
chiang_mai_scores = [9, 6, 8, 7, 9]

# Wrap the data to close the radar chart
bali_values = bali_scores + bali_scores[:1]
lisbon_values = lisbon_scores + lisbon_scores[:1]
chiang_mai_values = chiang_mai_scores + chiang_mai_scores[:1]
angles += angles[:1]

# Set up the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True), dpi=100)

# Use a colormap for distinct colors
colors = cm.get_cmap('tab10', 3)

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color='grey', size=12)

# Draw y-labels and adjust limits
ax.set_ylim(0, 10)
ax.yaxis.set_tick_params(labelsize=10)

# Plot each location's data with gradient fills
ax.plot(angles, bali_values, linewidth=2, linestyle='solid', label='Bali', color=colors(0))
ax.fill(angles, bali_values, colors(0), alpha=0.1)

ax.plot(angles, lisbon_values, linewidth=2, linestyle='solid', label='Lisbon', color=colors(1))
ax.fill(angles, lisbon_values, colors(1), alpha=0.1)

ax.plot(angles, chiang_mai_values, linewidth=2, linestyle='solid', label='Chiang Mai', color=colors(2))
ax.fill(angles, chiang_mai_values, colors(2), alpha=0.1)

# Add markers at data points
ax.scatter(angles[:-1], bali_scores, color=colors(0), edgecolors='k', zorder=10)
ax.scatter(angles[:-1], lisbon_scores, color=colors(1), edgecolors='k', zorder=10)
ax.scatter(angles[:-1], chiang_mai_scores, color=colors(2), edgecolors='k', zorder=10)

# Add a title with line breaks for better readability
ax.set_title('Digital Nomad Lifestyle Preferences\n(Comparison of Popular Destinations)', 
             size=16, color='navy', ha='center', va='bottom', y=1.1)

# Customize grid
ax.grid(color='grey', linestyle='--', linewidth=0.5)

# Legend outside the plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=10)

# Adjust layout to ensure everything fits
plt.tight_layout()

# Display the radar chart
plt.show()