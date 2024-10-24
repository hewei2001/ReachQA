import matplotlib.pyplot as plt
import numpy as np

# Define years and content types
years = np.array([2018, 2019, 2020, 2021, 2022, 2023])
content_types = ['Videos', 'Images', 'Blog Posts', 'Podcasts']

# Engagement data for each content type over the years (in arbitrary units)
engagement_data = np.array([
    [150, 180, 240, 300, 360, 420],  # Videos
    [100, 130, 170, 210, 250, 290],  # Images
    [80, 90, 100, 110, 120, 130],    # Blog Posts
    [40, 60, 90, 130, 170, 210],     # Podcasts
])

# Define colors for each content type with transparency
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a figure for the area chart
plt.figure(figsize=(12, 8))

# Create a stacked area chart
plt.stackplot(years, engagement_data, labels=content_types, colors=colors, alpha=0.8)

# Set the title and labels
plt.title('Annual Social Media Engagement Growth\nby Content Type (2018-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Engagement (Arbitrary Units)', fontsize=12)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Customize x-ticks and rotate if necessary
plt.xticks(years, rotation=0, fontsize=10)

# Place a legend outside the plot to avoid clutter
plt.legend(loc='upper left', fontsize=10, title='Content Types')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()