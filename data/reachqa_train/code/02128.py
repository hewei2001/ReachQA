import matplotlib.pyplot as plt
import numpy as np

# Communication methods and their time distribution
communication_methods = ['Emails', 'Meetings', 'Instant Messaging', 'Phone Calls', 'Video Conferences']
time_spent_percentages = [35, 25, 20, 10, 10]

# Colors for each segment of the chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Generate the pie chart with the 'wedgeprops' parameter for the donut shape
wedges, texts, autotexts = ax.pie(time_spent_percentages, labels=communication_methods, colors=colors, 
                                  autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
                                  wedgeprops=dict(width=0.3), explode=(0.05, 0.05, 0.05, 0.05, 0.05),
                                  shadow=True)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Title of the chart
plt.title('GlobaTalk: Distribution of Communication Methods\nAmong Employees in the 21st Century', 
          fontsize=16, fontweight='bold', pad=20)

# Customize autotexts within wedges
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a legend with title
ax.legend(wedges, communication_methods, title="Communication Methods", loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()