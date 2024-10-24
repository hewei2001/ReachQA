import matplotlib.pyplot as plt
import numpy as np

# Define the cities and their corresponding Sustainability Index scores
cities = ['GreenVille', 'EcoTown', 'SustainCity', 'RenewVille', 'Futurepolis']
indices = {
    'GreenVille': [8, 7, 9, 6, 8],
    'EcoTown': [9, 8, 8, 7, 9],
    'SustainCity': [7, 9, 8, 8, 7],
    'RenewVille': [8, 6, 7, 9, 6],
    'Futurepolis': [6, 8, 9, 8, 7]
}

# Define the sustainability categories
categories = ['Air Quality', 'Transport Efficiency', 'Green Spaces', 'Waste Management', 'Energy Use']
num_vars = len(categories)

# Compute angle for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop by appending the first angle and category for closure
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = plt.cm.Paired.colors

# Plot data for each city
for i, (city, index) in enumerate(indices.items()):
    data = index + index[:1]  # Close the loop for the radar plot
    ax.plot(angles, data, color=colors[i], linewidth=2, linestyle='solid', label=city)
    ax.fill(angles, data, color=colors[i], alpha=0.25)

# Customize the radar chart
ax.set_yticklabels([])  # Remove y-tick labels to avoid clutter
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_title("Urban Sustainability Indices:\nComparing Imaginary Cities",
             fontsize=15, fontweight='bold', pad=20)

# Add a legend to the radar chart
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Automatically adjust the layout to avoid overlapping
plt.tight_layout()

# Display the radar chart
plt.show()