import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

# Define the categories and performance data for each company
categories = ['Energy Efficiency', 'Waste Management', 'Water Conservation', 
              'Social Responsibility', 'Sustainable Sourcing']
# Wrap category labels to avoid overlap
categories = [ '\n'.join(wrap(label, 20)) for label in categories ]

# Data for each company
ecoTech_data = [8, 6, 7, 9, 7]
greenWave_data = [7, 8, 6, 6, 9]
sustainIt_data = [6, 5, 8, 8, 6]

# Close the radar chart by appending the first element to the end of each list
ecoTech_data += ecoTech_data[:1]
greenWave_data += greenWave_data[:1]
sustainIt_data += sustainIt_data[:1]

# Calculate angle of each axis
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Set up the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Plot each company's data
ax.plot(angles, ecoTech_data, color='#1f77b4', linewidth=2, linestyle='solid', label='EcoTech', marker='o')
ax.fill(angles, ecoTech_data, color='#1f77b4', alpha=0.3)

ax.plot(angles, greenWave_data, color='#2ca02c', linewidth=2, linestyle='dashdot', label='GreenWave', marker='s')
ax.fill(angles, greenWave_data, color='#2ca02c', alpha=0.3)

ax.plot(angles, sustainIt_data, color='#ff7f0e', linewidth=2, linestyle='dotted', label='SustainIt', marker='^')
ax.fill(angles, sustainIt_data, color='#ff7f0e', alpha=0.3)

# Customize grid
ax.yaxis.grid(True, color='gray', linestyle='dashed')
ax.xaxis.grid(True, color='gray', linestyle='dotted')

# Add labels to each axis
ax.set_yticklabels(range(0, 11), fontsize=10, color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, wrap=True)

# Add a title and a legend
plt.title('Comparison of Sustainability Practices\nAcross Three Companies', fontsize=16, pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Use tight layout to adjust
plt.tight_layout()

# Display the chart
plt.show()