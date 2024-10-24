import matplotlib.pyplot as plt
import numpy as np

# Define the labels and data for renewable energy sources
labels = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']
contributions = np.array([28, 35, 25, 7, 5])

# Define colors and edge colors for each sector
colors = ['#FFD700', '#1E90FF', '#00FA9A', '#A52A2A', '#FF8C00']
edge_colors = ['#B8860B', '#104E8B', '#006400', '#8B4513', '#CD3700']

# Create the pie chart with explode effect and additional enhancements
explode = (0.1, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    contributions, labels=labels, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='black'))

# Customize the text properties and annotations
plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=12, weight="bold")

# Annotate with arrows for clearer labeling
for i, wedge in enumerate(wedges):
    plt.annotate(f'{labels[i]}', xy=(wedge.theta2 / 2, 1.2), 
                 xytext=(wedge.theta2 / 2, 1.5), 
                 textcoords='polar',
                 arrowprops=dict(facecolor=edge_colors[i], arrowstyle='->'),
                 horizontalalignment='center', fontsize=11)

# Set the title with multiple lines for readability
plt.title('Distribution of Renewable Energy Sources\nin Global Power Generation - 2023', 
          fontsize=16, fontweight='bold', pad=20)

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')

# Add a legend to explain the sectors outside the pie
ax.legend(wedges, labels, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()