import matplotlib.pyplot as plt
import numpy as np

# Define years and seasons
years = np.arange(2020, 2024)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Create visitor data (in thousands)
visitors_spring = np.array([30, 34, 36, 38])
visitors_summer = np.array([50, 55, 60, 62])
visitors_autumn = np.array([25, 27, 28, 30])
visitors_winter = np.array([15, 18, 16, 14])

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Create the area chart using stackplot
ax.stackplot(years, visitors_spring, visitors_summer, visitors_autumn, visitors_winter,
             labels=seasons, colors=['#98FB98', '#FFD700', '#FF6347', '#4682B4'], alpha=0.8)

# Title and labels with appropriate font size and line breaks
ax.set_title('Seasonal Visitor Trends\nEvergreen National Park (2020-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Visitors (Thousands)', fontsize=12)

# Set x-axis tick labels and avoid overlapping
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add grid to enhance readability
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(loc='upper left', title='Seasons', fontsize=10)

# Annotations for data insight
ax.annotate('Summer Peak', xy=(2023, 62), xytext=(2022.5, 70),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
            fontsize=10, color='darkblue')

# Tight layout adjustment
plt.tight_layout()

# Display the plot
plt.show()