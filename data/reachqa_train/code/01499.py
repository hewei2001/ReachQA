import matplotlib.pyplot as plt
import numpy as np

# Define quarters within each year
years = np.arange(2018, 2024, 0.25)  # Quarterly data from 2018 to 2023

# Define content types with additional categories
content_types = ['Videos', 'Images', 'Blog Posts', 'Podcasts', 'Infographics', 'Webinars']

# Engagement data for each content type over the quarters (in arbitrary units)
# Non-linear growth patterns
engagement_data = np.array([
    150 + 20 * np.sin(0.5 * np.pi * years),  # Videos
    80 + 30 * np.exp(0.05 * (years-2018)),   # Images
    50 + 15 * np.log(years-2017),            # Blog Posts
    20 + 5 * (years-2018)**2,                # Podcasts
    40 + 10 * np.cos(0.2 * np.pi * years),   # Infographics
    25 + 12 * np.sqrt(years-2017)            # Webinars
])

# Define colors for each content type with varying shades
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a figure for the area chart with an additional subplot for total engagement
fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Create a stacked area chart in the first subplot
ax[0].stackplot(years, engagement_data, labels=content_types, colors=colors, alpha=0.8)
ax[0].set_title('Quarterly Social Media Engagement Growth\nby Content Type (2018-2023)', fontsize=16, fontweight='bold')
ax[0].set_ylabel('Engagement (Arbitrary Units)', fontsize=12)
ax[0].legend(loc='upper left', fontsize=10, title='Content Types')
ax[0].grid(True, linestyle='--', alpha=0.5)

# Calculate the total engagement per quarter and plot in the second subplot
total_engagement = np.sum(engagement_data, axis=0)
ax[1].plot(years, total_engagement, label='Total Engagement', color='black', linewidth=2, marker='o')
ax[1].set_title('Total Social Media Engagement (2018-2023)', fontsize=14)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Total Engagement', fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.5)
ax[1].legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()