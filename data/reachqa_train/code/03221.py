import matplotlib.pyplot as plt
import numpy as np

# Define the expanded areas of impact and their intensities
sectors = ['Education', 'Entertainment', 'Finance', 'Healthcare', 'Agriculture', 'Retail', 'Logistics', 'Manufacturing']
# Intensity values derived from a mathematical function to introduce complexity
intensities = [5*np.sin(i) + 8 for i in range(len(sectors))] 

# Calculate angles for each sector
num_sectors = len(sectors)
sector_angle = (2 * np.pi) / num_sectors
angles = np.arange(0, 2 * np.pi, sector_angle)

# Repeat the first intensity and angle to complete the loop
intensities += intensities[:1]
angles = np.append(angles, angles[0])

# Colors for different sectors
colors = plt.cm.viridis(np.linspace(0, 1, num_sectors))

# Create polar plot
fig, ax = plt.subplots(figsize=(12, 9), subplot_kw=dict(polar=True))

# Draw bars with calculated angles and intensities
bars = ax.bar(angles[:-1], intensities[:-1], width=sector_angle, color=colors, alpha=0.7, edgecolor='k', linewidth=1.5)

# Add chart title
ax.set_title("AI Impact Across Sectors:\nA Complex Harmonic Analysis", fontsize=18, weight='bold', pad=30)

# Set labels on perimeter
ax.set_xticks(angles[:-1])
ax.set_xticklabels(sectors, fontsize=11, weight='bold')

# Hide radial labels and draw grid lines
ax.set_yticklabels([])
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)

# Add legend outside the plot
ax.legend(bars, sectors, loc='upper right', bbox_to_anchor=(1.3, 1.15), fontsize=9, frameon=False, title='Sectors', title_fontsize='13')

# Auto adjust layout
plt.tight_layout()

# Display the plot
plt.show()