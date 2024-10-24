import matplotlib.pyplot as plt
import numpy as np

# Define sectors and AI technologies
sectors = ['Healthcare', 'Finance', 'Manufacturing', 'Retail', 'Education']
technologies = ['Machine Learning', 'Computer Vision', 'NLP', 'Robotics', 'Predictive\nAnalytics']

# Adoption data (manually curated)
adoption_data = np.array([
    [6, 7, 5, 4, 8],  # Healthcare
    [8, 5, 7, 3, 9],  # Finance
    [5, 4, 6, 8, 7],  # Manufacturing
    [7, 6, 5, 3, 7],  # Retail
    [4, 3, 5, 2, 6]   # Education
])

# Create the heatmap
fig, ax = plt.subplots(figsize=(10, 7))
cax = ax.imshow(adoption_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')

# Add color bar with label
color_bar = plt.colorbar(cax)
color_bar.set_label('Adoption Level', rotation=270, labelpad=20)

# Set axis ticks and labels
ax.set_xticks(np.arange(len(technologies)))
ax.set_yticks(np.arange(len(sectors)))
ax.set_xticklabels(technologies, fontsize=10, ha='right', rotation=25)
ax.set_yticklabels(sectors, fontsize=10)

# Set axis labels and title
ax.set_xlabel('AI Technologies', fontsize=12, labelpad=10)
ax.set_ylabel('Sectors', fontsize=12, labelpad=10)
ax.set_title('AI Technology Adoption Across Sectors (2018-2023)', fontsize=14, fontweight='bold', pad=20)

# Annotate each cell with the adoption level value
for (i, j), val in np.ndenumerate(adoption_data):
    ax.text(j, i, f'{val}', ha='center', va='center', color='black', fontsize=9, fontweight='bold')

# Ensure the layout is tight to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()