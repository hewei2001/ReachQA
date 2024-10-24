import matplotlib.pyplot as plt
import numpy as np

# Define the labels and data for renewable energy sources
labels = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']
contributions = np.array([28, 35, 25, 7, 5])

# Define colors for each sector
colors = ['#FFD700', '#1E90FF', '#00FA9A', '#A52A2A', '#FF8C00']

# Create the pie chart with 'explode' effect for better visual distinction
explode = (0.1, 0.1, 0, 0, 0)  # Explode the first two sectors (Solar and Wind)

plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    contributions, labels=labels, autopct='%1.1f%%', startangle=140, 
    colors=colors, explode=explode, shadow=True, textprops=dict(color="w"))

# Customize the text properties
plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=12, weight="bold")

# Set the title with multiple lines for readability
plt.title('Distribution of Renewable Energy Sources\nin Global Power Generation - 2023', 
          fontsize=16, fontweight='bold', pad=20)

# Equal aspect ratio ensures the pie chart is circular
plt.axis('equal')

# Add a legend to explain the sectors outside the pie
plt.legend(wedges, labels, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()