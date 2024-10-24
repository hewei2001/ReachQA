import matplotlib.pyplot as plt
import numpy as np

# Define the resource categories
resource_categories = [
    'Agriculture & Livestock',
    'Magical R&D',
    'Infrastructure & Trade',
    'Defense & Security',
    'Healthcare',
    'Education',
    'Arts & Culture',
    'Environment & Forestry'
]

# Allocate hypothetical percentages to each category
resource_allocation = [20, 15, 15, 12, 10, 10, 10, 8]

# Ensure the sum of allocation percentages is 100
assert sum(resource_allocation) == 100, "The resource allocations must sum up to 100."

# Define a whimsical color palette
colors = ['#8a9a5b', '#b9936c', '#6c5b7b', '#d16ba5', '#9f9f9f', '#ffab84', '#c9cba3', '#6c91bf']

# Choose to explode the slices for emphasis on Magical Research and Education
explode = (0, 0.1, 0, 0, 0, 0.1, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    resource_allocation, explode=explode, labels=resource_categories, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85, shadow=True, wedgeprops=dict(edgecolor='k')
)

# Customize text properties
for text in texts:
    text.set_fontsize(9)
    text.set_color('darkblue')

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('darkred')

# Draw a circle at the center to transform the pie into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title and additional styling
ax.set_title("Resource Distribution in the Kingdom of Eldoria", fontsize=14, fontweight='bold', pad=20)

# Position the legend to avoid overlap with the pie chart
ax.legend(wedges, resource_categories, title="Resource Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Ensure the plot is well adjusted
plt.tight_layout()

# Display the plot
plt.show()