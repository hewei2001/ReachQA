import matplotlib.pyplot as plt
import numpy as np

# Define the categories and their innovation scores
categories = ['AI', 'Space\nExploration', 'Biotech', 'Sustainable\nEnergy', 
              'Quantum\nComputing', 'Cybersecurity']
scores_primary = [9.5, 8.7, 7.8, 9.2, 8.0, 8.3]
scores_secondary = [8.8, 8.2, 8.5, 9.0, 7.5, 8.6]  # Additional data for circular bars

# Radar chart requires the dataset to be circular, so append the first score to the end
scores_primary += scores_primary[:1]
scores_secondary += scores_secondary[:1]

# Calculate the angle for each category on the radar chart
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one sector per variable and add labels
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories, fontsize=11, ha='center')

# Draw y-labels and set their scale
ax.yaxis.set_tick_params(labelsize=9)
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], fontsize=10)
ax.yaxis.grid(True, color='gray', linestyle='--', alpha=0.7)

# Plot the primary radar chart
ax.plot(angles, scores_primary, color='navy', linewidth=2, linestyle='solid', label='Innovation Scores')
ax.fill(angles, scores_primary, color='skyblue', alpha=0.3)

# Overlay a circular bar plot
# Calculate bar widths (distance between angles)
bar_width = (2 * np.pi) / num_vars * 0.3
bars = ax.bar(angles[:-1], scores_secondary[:-1], width=bar_width, color='lightcoral', alpha=0.6, edgecolor='red', linewidth=1.2, label='Projected Growth')

# Add a title
plt.title("Technological Innovations and Growth Projections in 2075", fontsize=14, weight='bold', pad=40)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()