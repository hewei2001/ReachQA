import matplotlib.pyplot as plt
import numpy as np

# Data for the ring chart
materials = ['Steel', 'Concrete', 'Glass', 'Wood', 'Composites']
usage_percentage = [30, 25, 20, 15, 10]

# Colors for each segment
colors = ['#FFD700', '#C0C0C0', '#1E90FF', '#8B4513', '#FF6347']

# Plot the ring chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Create wedges for the pie chart, which will appear as a ring chart
wedges, texts, autotexts = ax.pie(
    usage_percentage, labels=materials, startangle=90,
    colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'),
    autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", weight='bold')
)

# Adding a central circle to convert the pie chart to a ring (donut) chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Title of the chart
plt.title('Materials Usage in Modern Architecture', fontsize=16, pad=20)

# Customize autotexts
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Legend with title outside the plot
plt.legend(wedges, materials, title="Materials", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatic layout adjustment
plt.tight_layout()

# Show the chart
plt.show()