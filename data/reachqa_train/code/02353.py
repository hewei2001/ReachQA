import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2012, 2023)

# Data for the number of bikers (in thousands)
bikers = [10, 12, 15, 18, 22, 28, 35, 40, 45, 50, 60]

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the line for bikers
ax.plot(years, bikers, marker='o', color='seagreen', linestyle='-', linewidth=2.5, markersize=8, label='Bikers')

# Annotate significant points
for i, value in enumerate(bikers):
    ax.text(years[i], value + 2, f"{value}k", ha='center', fontsize=9, color='darkgreen')

# Title and labels with a focus on climate change awareness
ax.set_title('Rise in Biking Trends in UrbanVille (2012-2022)\nImpact of Climate Change Awareness', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Bikers (Thousands)', fontsize=14)

# Add a legend
ax.legend(title='Transport Mode', fontsize=12, loc='upper left', frameon=False)

# Customize grid and layout for better readability
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years)
plt.yticks(np.arange(0, 70, 10))

# Ensure no text overlaps by adjusting layout
plt.tight_layout()

# Display the chart
plt.show()