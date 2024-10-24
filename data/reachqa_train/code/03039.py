import matplotlib.pyplot as plt
import numpy as np

# Categories of internet usage
activities = ['Social Media', 'E-commerce', 'Streaming', 'Online Education', 'Gaming', 'Other']

# Proportional usage data (in percentage)
usage_percentages = [30, 25, 20, 10, 10, 5]

# Colors for each category
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251']

# Explode the 'Social Media' slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Plot the ring chart
wedges, texts, autotexts = ax.pie(usage_percentages, explode=explode, labels=activities, autopct='%1.1f%%',
                                  pctdistance=0.85, colors=colors, startangle=140, 
                                  wedgeprops=dict(width=0.3, edgecolor='w'))

# Customize text properties
plt.setp(autotexts, size=10, weight="bold", color="black")

# Add a circle at the center to create a donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title and styling
ax.set_title("Global Internet Usage Breakdown:\nA Digital Era Overview", fontsize=14, weight='bold')
ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout for no overlap
plt.tight_layout()

# Display the chart
plt.show()