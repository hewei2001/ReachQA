import matplotlib.pyplot as plt
import numpy as np

# Define the decades from the 1980s to the 2020s
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Streaming data for each genre in millions
classical = np.array([15, 20, 22, 24, 28])
jazz = np.array([25, 30, 28, 22, 18])
rock = np.array([30, 40, 35, 30, 25])
hip_hop = np.array([5, 10, 25, 40, 50])
electronic = np.array([2, 5, 15, 30, 45])

# Create a stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, classical, jazz, rock, hip_hop, electronic,
             labels=['Classical', 'Jazz', 'Rock', 'Hip-Hop', 'Electronic'],
             colors=['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99'],
             alpha=0.8)

# Set plot title and labels
ax.set_title('Evolution of Music Streaming Preferences\nfrom the 1980s to the 2020s', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Streams (Millions)', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', title='Music Genres')

# Format the x-axis to display decades nicely
ax.set_xticks(decades)
ax.set_xticklabels([f"{decade}s" for decade in decades], fontsize=10)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()