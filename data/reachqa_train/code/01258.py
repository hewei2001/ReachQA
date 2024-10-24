import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.array([2000, 2005, 2010, 2015, 2020])

# Data for the engagement percentages
education = np.array([10, 20, 30, 40, 55])
corporate = np.array([5, 10, 20, 35, 50])
government = np.array([15, 25, 35, 50, 65])
non_profit = np.array([10, 20, 30, 50, 60])

# Stack the data for the area chart
engagement_data = np.vstack([education, corporate, government, non_profit])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for each sector
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c']
labels = ['Education', 'Corporate', 'Government', 'Non-Profit']

# Create an area chart using stackplot
ax.stackplot(years, engagement_data, labels=labels, colors=colors, alpha=0.8)

# Set title and labels
ax.set_title('Growth in Environmental Awareness Initiatives\nAcross Various Sectors (2000-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Engagement (%)', fontsize=14)

# Customizing the ticks and grid for better readability
ax.set_xticks(years)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add a legend
ax.legend(loc='upper left', fontsize=12, title='Sectors')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()