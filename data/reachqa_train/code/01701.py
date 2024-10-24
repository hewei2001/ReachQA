import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Energy Conservation', 'Waste Reduction', 'Water Usage Efficiency', 'Sustainable Transportation', 'Local Food Consumption']
num_vars = len(categories)

# Define the data for each household segment
urban_families = [78, 65, 70, 90, 60]
suburban_singles = [60, 80, 55, 85, 75]
rural_communities = [85, 70, 80, 65, 95]

# Extend the data to close the radar chart
urban_families += urban_families[:1]
suburban_singles += suburban_singles[:1]
rural_communities += rural_communities[:1]

# Calculate the angles for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart with polar coordinates
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define a function to plot data on the radar chart
def plot_radar(data, label, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, label=label, color=color, linewidth=2)

# Plot the data for each segment
plot_radar(urban_families, 'Urban Families', 'forestgreen')
plot_radar(suburban_singles, 'Suburban Singles', 'royalblue')
plot_radar(rural_communities, 'Rural Communities', 'darkgoldenrod')

# Customize the chart
ax.set_yticklabels([])  # Remove y-axis labels for cleaner appearance
ax.set_xticks(angles[:-1])  # Position the category labels
ax.set_xticklabels(categories, fontsize=9)  # Set category labels

# Title and legend setup
plt.title('EcoSmart Living: Household Sustainability Practices\nin 2023', fontsize=15, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Improve layout to ensure everything fits nicely
plt.tight_layout()

# Display the radar chart
plt.show()