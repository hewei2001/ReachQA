import matplotlib.pyplot as plt
import numpy as np

# Define the fashion styles and months
styles = ['Minimalist', 'Streetwear', 'Vintage', 'Bohemian', 'Athleisure', 'Gothic']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Engagement rates (manually constructed data)
engagement_rates = np.array([
    [65, 70, 68, 75, 80, 85, 90, 88, 83, 78, 72, 68],  # Minimalist
    [72, 77, 75, 82, 88, 92, 95, 93, 87, 83, 78, 74],  # Streetwear
    [60, 65, 63, 67, 70, 76, 80, 78, 74, 70, 66, 63],  # Vintage
    [58, 62, 60, 65, 68, 72, 76, 73, 70, 66, 62, 60],  # Bohemian
    [70, 75, 73, 78, 82, 87, 90, 89, 84, 79, 74, 71],  # Athleisure
    [50, 55, 53, 57, 60, 65, 68, 66, 61, 58, 54, 51]   # Gothic
])

# Plotting the heat map
plt.figure(figsize=(10, 6))
heatmap = plt.imshow(engagement_rates, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Adding a color bar
cbar = plt.colorbar(heatmap)
cbar.set_label('Engagement Level\n(Scale 1-100)', fontsize=10)

# Set title and axis labels
plt.title('Digital Fashion Trends Analysis\nEngagement Rates by Style and Month', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Fashion Style', fontsize=12)

# Set ticks and labels
plt.xticks(ticks=np.arange(len(months)), labels=months, fontsize=10, rotation=45)
plt.yticks(ticks=np.arange(len(styles)), labels=styles, fontsize=10)

# Annotating each cell with the engagement rate
for i in range(len(styles)):
    for j in range(len(months)):
        plt.text(j, i, f"{engagement_rates[i, j]}", ha='center', va='center', color='black', fontsize=8)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()