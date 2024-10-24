import matplotlib.pyplot as plt
import numpy as np

# Delivery time data in hours for each city
delivery_times = {
    'New York': [1, 2, 2.5, 3, 4, 4.5, 5, 6, 6.5, 7, 8],
    'Los Angeles': [1.5, 2, 3, 3.5, 4, 4.5, 5.5, 6, 7, 8.5],
    'Chicago': [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8],
    'Houston': [2, 2.5, 3, 3.5, 4, 5, 5.5, 6, 6.5, 7, 9],
    'Miami': [1, 1.5, 2, 2.5, 3.5, 4, 5, 5.5, 6, 7, 8]
}

# Prepare data for the boxplot
data_to_plot = [delivery_times[city] for city in delivery_times]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))
box = ax.boxplot(data_to_plot, vert=False, patch_artist=True, 
                 labels=delivery_times.keys(), notch=True, whis=1.5)

# Customize colors for each box
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Titles and labels
ax.set_title('E-commerce Delivery Time Distribution Across Major US Cities', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Delivery Time (Hours)', fontsize=12)
ax.set_ylabel('Cities', fontsize=12)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Set y-tick positions manually for better visibility and spacing
ax.set_yticks(np.arange(1, len(delivery_times) + 1))
ax.set_yticklabels(delivery_times.keys())

# Use a tight layout to ensure nothing overlaps
plt.tight_layout()

# Display the plot
plt.show()