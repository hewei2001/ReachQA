import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Factors for evaluation
factors = ['Visibility', 'Biodiversity', 'Water Temperature', 'Safety', 'Accessibility']

# Diving destination evaluations
destination_data = {
    'Great Barrier Reef': [9, 10, 7, 8, 7],
    'Red Sea': [8, 9, 8, 9, 8],
    'Galapagos Islands': [7, 10, 6, 9, 6],
    'Maldives': [9, 8, 9, 7, 8],
    'Belize Barrier Reef': [8, 9, 8, 7, 7]
}

# Number of variables and angles for the radar chart
num_vars = len(factors)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.title('Aquatic Adventures:\nScuba Diving Destinations\nKey Factor Comparison', size=14, weight='bold', pad=20)

# Function to plot each destination
def create_radar_chart(destination_name, color):
    values = destination_data[destination_name]
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid', label=destination_name)
    ax.fill(angles, values, color=color, alpha=0.25)

# Color palette for different destinations
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each destination
for destination, color in zip(destination_data.keys(), colors):
    create_radar_chart(destination, color)

# Add factor labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(factors, color='black', size=11)

# Add legend and adjust layout
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15), fontsize='small', ncol=1)
plt.tight_layout()

# Display the radar chart
plt.show()