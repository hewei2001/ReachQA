import matplotlib.pyplot as plt
import numpy as np

# Data
materials = ['Copper', 'Silver', 'Gold', 'Titanium', 'Aluminum', 'Copper-Zinc Alloy']
efficiencies = [0.08, 0.12, 0.15, 0.10, 0.06, 0.11]
costs = [100, 150, 200, 120, 80, 130]
specific_weights = [8.96, 10.49, 19.3, 4.54, 2.7, 8.4]

# Color scheme
colors = ['#0047AB', '#00698F', '#0085CA', '#0099D6', '#00B2FF', '#0047AB']

# Create figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot horizontal bars on ax1
ax1.barh(materials, efficiencies, height=0.5, color=colors)

# Add value labels on the end of each bar on ax1
for i, efficiency in enumerate(efficiencies):
    ax1.text(efficiency + 0.005, i, f'{efficiency:.2f}', ha='left', va='center')

# Set title and labels on ax1
ax1.set_title('Efficiency of Different Materials in Thermoelectric Conversion\n'
              'Measured in terms of energy conversion rate')
ax1.set_xlabel('Efficiency')
ax1.set_ylabel('Materials')
ax1.tick_params(axis='y', labelsize=8)
plt.sca(ax1)
plt.yticks(range(len(materials)), materials, ha='center')

# Add grid lines on ax1
ax1.grid(axis='x', linestyle='--', alpha=0.5)

# Plot scatter plot on ax2
ax2.scatter(costs, specific_weights, c=colors)
ax2.set_xlabel('Cost ($)')
ax2.set_ylabel('Specific Weight (g/cm³)')
ax2.set_title('Relationship between Cost and Specific Weight of Materials')

# Add annotation on ax2
for i, material in enumerate(materials):
    ax2.annotate(material, (costs[i], specific_weights[i]))

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()