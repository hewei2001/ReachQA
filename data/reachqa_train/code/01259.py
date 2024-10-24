import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.array([2000, 2005, 2010, 2015, 2020])

# Data for the engagement percentages for each sector
education = np.array([10, 20, 30, 40, 55])
corporate = np.array([5, 10, 20, 35, 50])
government = np.array([15, 25, 35, 50, 65])
non_profit = np.array([10, 20, 30, 50, 60])

# Stack the data for the area chart
engagement_data = np.vstack([education, corporate, government, non_profit])

# Data for the overall engagement trend (total initiatives)
overall_engagement = education + corporate + government + non_profit

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for each sector and the line plot
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c']
line_color = '#ff7f00'  # Orange color for the overlay line plot

# Labels for the sectors
labels = ['Education', 'Corporate', 'Government', 'Non-Profit']

# Create an area chart using stackplot
ax.stackplot(years, engagement_data, labels=labels, colors=colors, alpha=0.8)

# Overlay a line plot for overall engagement
ax.plot(years, overall_engagement, label='Overall Engagement', color=line_color, linewidth=2.5, marker='o', markersize=8)

# Set title and labels
ax.set_title('Growth in Environmental Awareness Initiatives\nAcross Various Sectors (2000-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Engagement (%)', fontsize=14)

# Customizing the ticks and grid for better readability
ax.set_xticks(years)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Adding annotations at each point of the overall engagement line
for i, txt in enumerate(overall_engagement):
    ax.annotate(f'{txt}%', (years[i], overall_engagement[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Add a legend
ax.legend(loc='upper left', fontsize=12, title='Sectors & Overall Engagement')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()