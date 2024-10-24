import matplotlib.pyplot as plt
import numpy as np

# Define cities and waste management categories
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Mumbai']
categories = ['Recycled', 'Composted', 'Incinerated', 'Landfilled']
data = [
    [30, 20, 10, 40],  # New York
    [45, 25, 15, 15],  # London
    [50, 10, 30, 10],  # Tokyo
    [60, 25, 5, 10],   # Sydney
    [10, 5, 10, 75]    # Mumbai
]

# Transpose the data for stacking bars
data = np.array(data).T

# Define colors for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot stacked bar chart
for i, (category, color) in enumerate(zip(categories, colors)):
    bottom = np.sum(data[:i], axis=0) if i > 0 else None
    ax.bar(cities, data[i], bottom=bottom, color=color, label=category)

# Set chart title and labels
ax.set_title("Urban Waste Management: Recycling and Disposal\nStatistics Across Major Cities - 2023", 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Cities", fontsize=12, weight='bold')
ax.set_ylabel("Percentage", fontsize=12, weight='bold')

# Set y-axis limits
ax.set_ylim(0, 100)

# Add data labels
for i, (category_data, color) in enumerate(zip(data, colors)):
    bottom = np.sum(data[:i], axis=0) if i > 0 else np.zeros_like(category_data)
    for x, (height, b) in enumerate(zip(category_data, bottom)):
        ax.text(x, b + height / 2, f'{height}%', ha='center', va='center', color='white', fontweight='bold')

# Add legend
ax.legend(title="Waste Management Type", loc='upper left', bbox_to_anchor=(1, 1))

# Use tight layout to avoid label overlap
plt.tight_layout()

# Display the plot
plt.show()