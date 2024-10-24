import matplotlib.pyplot as plt
import numpy as np

# Define decades from 1900 to 1999
decades = np.arange(1900, 2000, 10)

# Define theme data for each decade
romance = np.array([30, 25, 20, 15, 10, 12, 18, 20, 22, 25])
war = np.array([5, 8, 15, 25, 30, 35, 25, 15, 10, 5])
identity = np.array([10, 12, 15, 18, 22, 25, 30, 35, 40, 42])
sci_fi = np.array([1, 2, 4, 8, 10, 12, 15, 18, 22, 25])

# Stack the data for plotting
theme_data = np.vstack([romance, war, identity, sci_fi])

# Create the figure and the axis
plt.figure(figsize=(12, 7))

# Set colors for each literary theme
colors = ['#FFB6C1', '#FFD700', '#87CEEB', '#8A2BE2']

# Create the stacked area plot
plt.stackplot(decades, theme_data, labels=['Romance', 'War', 'Identity', 'Science Fiction'], colors=colors, alpha=0.8)

# Add title and labels
plt.title('Evolving Themes in Literature:\nA Century of Change (1900-1999)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Prominence in Literature (%)', fontsize=12)

# Adjust x-axis labels to prevent overlap
plt.xticks(decades, rotation=45)

# Adding legend outside the main plot area
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()