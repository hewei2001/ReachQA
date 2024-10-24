import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2024)

# Simulated research funding data for each discipline (in million USD)
# Modifying some values for better visualization and trends
life_sciences = np.array([220, 230, 240, 250, 260, 270, 280, 290, 310, 330, 350])
physical_sciences = np.array([160, 155, 165, 170, 175, 180, 185, 190, 195, 200, 205])
computer_science = np.array([45, 50, 65, 80, 95, 110, 130, 150, 170, 190, 210])
engineering = np.array([190, 195, 200, 205, 210, 220, 225, 230, 240, 245, 250])
environmental_science = np.array([15, 20, 25, 30, 40, 55, 70, 85, 105, 130, 160])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the funding data
ax.stackplot(years, life_sciences, physical_sciences, computer_science, engineering, environmental_science,
             labels=['Life Sciences', 'Physical Sciences', 'Computer Science', 'Engineering', 'Environmental Science'],
             colors=['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3'], alpha=0.8)

# Title and labels
ax.set_title("Decadal Trends in Research Funding Allocation\nAcross Scientific Disciplines", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Funding (in million USD)", fontsize=14)

# Customize grid style
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Set ticks for both axes
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 1101, 100))

# Rotate the x-tick labels for better readability
ax.set_xticklabels(years, rotation=45, ha='right')

# Adding a legend and positioning it outside the plot area
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1, 1), title="Disciplines")

# Adjust layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()