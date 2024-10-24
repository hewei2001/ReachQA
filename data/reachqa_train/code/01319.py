import matplotlib.pyplot as plt
import numpy as np

# Define the years for which data is available
years = np.arange(2010, 2021)

# Define the streaming platforms
platforms = ["Streaming A", "Streaming B", "Streaming C", "Streaming D", "Other Platforms"]

# Hours of content streamed globally (in billion hours) for each platform
streamed_hours = np.array([
    [10, 15, 20, 25, 32, 40, 55, 68, 75, 80, 82],  # Streaming A
    [5, 10, 15, 20, 28, 35, 45, 50, 55, 60, 65],   # Streaming B
    [2, 5, 9, 14, 20, 28, 38, 45, 50, 55, 60],     # Streaming C
    [1, 2, 5, 10, 15, 20, 28, 30, 32, 34, 36],     # Streaming D
    [5, 6, 8, 11, 15, 20, 25, 30, 32, 35, 37]      # Other Platforms
])

# Setup figure and axes for the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define color palette for the areas
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plotting the stacked area chart
ax.stackplot(years, streamed_hours, labels=platforms, colors=colors, alpha=0.85)

# Adding title and labels
ax.set_title('The Rise of Streaming:\nEvolution of Digital Streaming Platforms from 2010 to 2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Hours Streamed (in billion hours)', fontsize=12)

# Adding legend
ax.legend(loc='upper left', fontsize=10, title='Streaming Platforms', bbox_to_anchor=(1, 1))

# Adding a grid to enhance readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Set x-ticks for each year
ax.set_xticks(years)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45)

# Ensure no overlap of elements
plt.tight_layout()

# Display the plot
plt.show()