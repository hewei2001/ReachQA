import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color='grey', size=12)

# Draw y-labels and adjust limits
ax.set_ylim(0, 10)

# Plot each location's data
ax.plot(angles, bali_values, linewidth=2, linestyle='solid', label='Bali')
ax.fill(angles, bali_values, 'b', alpha=0.1)

ax.plot(angles, lisbon_values, linewidth=2, linestyle='solid', label='Lisbon', color='r')
ax.fill(angles, lisbon_values, 'r', alpha=0.1)

ax.plot(angles, chiang_mai_values, linewidth=2, linestyle='solid', label='Chiang Mai', color='g')
ax.fill(angles, chiang_mai_values, 'g', alpha=0.1)

# Add a title
ax.set_title('Digital Nomad Lifestyle Preferences\n(Comparison of Popular Destinations)', 
             size=16, color='navy', position=(0.5, 1.2), ha='center')

# Adjust layout to ensure everything fits
plt.tight_layout()

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Display the radar chart
plt.show()