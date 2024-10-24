import numpy as np
import matplotlib.pyplot as plt

# Define the categories and their respective scores
categories = ['Renewable Energy', 'Waste Management', 'Biodiversity',
              'Water Conservation', 'Air Quality', 'Green Transportation']
values = np.array([85, 78, 65, 90, 70, 60])

# Close the loop by appending the first value at the end
values = np.concatenate((values, [values[0]]))

# Calculate the angles for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot the data
ax.fill(angles, values, color='skyblue', alpha=0.4)
ax.plot(angles, values, color='blue', linewidth=2)

# Add category labels around the chart
ax.set_yticklabels([])  # Remove radial labels for simplicity
ax.set_xticks(angles)
ax.set_xticklabels(categories + [categories[0]], fontsize=10, fontweight='bold', color='darkgreen')

# Set title
plt.title("EcoVision: Sustainability Index 2040\nPerformance of EcoNation",
          size=16, color='darkblue', weight='bold', pad=20)

# Set radial limits
ax.set_ylim(0, 100)

# Add a legend
ax.legend(['Performance Score'], loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize='medium', frameon=True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()