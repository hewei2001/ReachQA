import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Define years
years = np.arange(2013, 2023)

# Define adoption data for each technology
ai_adoption = np.array([5, 10, 20, 30, 40, 50, 55, 60, 70, 75])
blockchain_adoption = np.array([2, 8, 15, 22, 30, 28, 26, 24, 22, 20])
iot_adoption = np.array([10, 15, 25, 35, 45, 55, 53, 51, 50, 48])
ar_adoption = np.array([3, 7, 10, 15, 18, 20, 22, 20, 18, 17])

# Sum up all tech adoptions per year
total_adoption = ai_adoption + blockchain_adoption + iot_adoption + ar_adoption

# Normalize to percentage of total adoption each year
ai_adoption_percentage = (ai_adoption / total_adoption) * 100
blockchain_adoption_percentage = (blockchain_adoption / total_adoption) * 100
iot_adoption_percentage = (iot_adoption / total_adoption) * 100
ar_adoption_percentage = (ar_adoption / total_adoption) * 100

# Stack the data for plotting
adoption_data = np.vstack([ai_adoption_percentage, blockchain_adoption_percentage, iot_adoption_percentage, ar_adoption_percentage])

# Creating a grid for better layout
fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

# Set a modern color map
colors = cm.viridis(np.linspace(0, 1, 4))

# Create a stacked area plot with gradient-style effect
ax.stackplot(years, adoption_data, labels=['AI', 'Blockchain', 'IoT', 'AR'], colors=colors, alpha=0.85)

# Add data markers for each year
for i, percentage in enumerate(adoption_data):
    ax.plot(years, np.cumsum(adoption_data, axis=0)[i], marker='o', markersize=5, linestyle='None', label='_nolegend_', color=colors[i])

# Adding title and labels
ax.set_title('Decade of Tech Evolution: Trends and Adoption\n(2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('User Adoption (%)', fontsize=12)

# Adjust x-axis labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adding annotations for key events
ax.annotate('AI Surpasses Others', xy=(2017, 50), xytext=(2015, 70),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='navy')

# Adding legend with a transparent background
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), frameon=False)

# Stylized gridlines
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()