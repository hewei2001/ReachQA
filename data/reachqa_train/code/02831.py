import matplotlib.pyplot as plt
import numpy as np

# Define the countries and renewable energy sectors
countries = ['USA', 'China', 'Germany', 'India', 'Brazil']
sectors = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

# R&D Expenditure Data (in million USD)
expenditure_data = np.array([
    [1200, 1100, 500, 300],  # USA
    [1400, 900, 600, 400],   # China
    [900, 700, 200, 100],    # Germany
    [800, 600, 300, 150],    # India
    [500, 400, 300, 200]     # Brazil
])

# Create the heatmap
plt.figure(figsize=(10, 6))
cmap = plt.cm.viridis  # Color map choice
heatmap = plt.imshow(expenditure_data, cmap=cmap, aspect='auto', interpolation='nearest')

# Add color bar
cbar = plt.colorbar(heatmap)
cbar.set_label('R&D Expenditure (Million USD)', rotation=270, labelpad=15)

# Set the ticks and labels
plt.xticks(ticks=np.arange(len(sectors)), labels=sectors, fontsize=10)
plt.yticks(ticks=np.arange(len(countries)), labels=countries, fontsize=10)

# Add title and labels
plt.title('Tech Innovation Impact:\nGlobal R&D Expenditure in Renewable Energy by Country (2023)', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Renewable Energy Sector', fontsize=12)
plt.ylabel('Country', fontsize=12)

# Add text annotations inside the heat map
for i in range(len(countries)):
    for j in range(len(sectors)):
        plt.text(j, i, f'{expenditure_data[i, j]}', ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()