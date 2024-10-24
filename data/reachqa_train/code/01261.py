import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
import matplotlib.cm as cm

# Data for the chart: hours spent on various activities during a weekend
activities = ['Watching Movies', 'Playing Sports', 'Socializing', 'Relaxing', 'Household Chores']
hours_spent = [8, 5, 6, 7, 4]  # Total 30 hours

# Create a color map with a gradient effect
colors = cm.PuBuGn(np.linspace(0.5, 1.0, len(activities)))

# Create the pie chart with enhanced visualization
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    hours_spent,
    labels=activities,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2, antialiased=True),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Add a circular center to transform into a donut chart and provide space for an additional label
centre_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', linewidth=1.25, edgecolor='black')
fig.gca().add_artist(centre_circle)
plt.text(0, 0, 'Total\n30 Hours', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Set an equal aspect ratio
ax.axis('equal')

# Customize the autotexts for better visibility
plt.setp(autotexts, size=10, weight="bold", color="black")

# Enhanced title with a backstory
ax.set_title('Weekend Leisure Time Distribution:\nAchieving Balance Across Activities', fontsize=14, fontweight='bold', pad=20)

# Legend with dynamic positioning
ax.legend(wedges, activities, title="Activities", loc="upper right", bbox_to_anchor=(1.3, 1), frameon=False)

# Adjust layout to ensure the plot is centered and nothing is clipped
plt.tight_layout()

# Show the plot
plt.show()