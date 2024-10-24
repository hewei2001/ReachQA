import matplotlib.pyplot as plt
import numpy as np

# Data for the chart: hours spent on various activities during a weekend
activities = ['Watching Movies', 'Playing Sports', 'Socializing', 'Relaxing', 'Household Chores']
hours_spent = [8, 5, 6, 7, 4]  # Ensure the data totals to 30 hours, a typical weekend

# Colors for the different sections of the pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    hours_spent,
    labels=activities,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),  # Slightly explode each section for emphasis
    shadow=True  # Add a shadow for 3D effect
)

# Add a circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, color='black', fc='white', linewidth=1.25)
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')

# Customize the autotext for better visibility
plt.setp(autotexts, size=10, weight="bold", color="black")

# Title with a backstory, split into two lines for readability
ax.set_title('Weekend Leisure Time Distribution:\nBalancing Sports & Entertainment', fontsize=14, fontweight='bold', pad=20)

# Add legend and position it for clarity
ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(0.85, 0, 0.5, 1))

# Adjust layout to ensure the plot is centered and nothing is clipped
plt.tight_layout()

# Show the plot
plt.show()