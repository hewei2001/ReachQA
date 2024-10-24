import matplotlib.pyplot as plt
import numpy as np

# Define the e-commerce platforms and service aspects
platforms = ['Amazon', 'eBay', 'Alibaba', 'Walmart', 'Etsy']
service_aspects = ['Delivery', 'Quality', 'Support', 'Experience', 'Value']

# Ratings data
ratings_data = np.array([
    [4.5, 4.2, 4.0, 4.8, 4.3],  # Amazon
    [4.0, 4.1, 3.5, 4.2, 4.0],  # eBay
    [4.3, 4.5, 3.9, 4.5, 4.4],  # Alibaba
    [4.1, 4.0, 3.8, 4.4, 4.1],  # Walmart
    [4.2, 4.6, 4.3, 4.7, 4.5]   # Etsy
])

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 7))

# Define bar width and positions
bar_width = 0.15
positions = np.arange(len(platforms))

# Colors for each service aspect
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each aspect as a series of bars
for idx, (aspect, color) in enumerate(zip(service_aspects, colors)):
    ax.bar(positions + idx * bar_width, ratings_data[:, idx], bar_width,
           label=aspect, color=color, edgecolor='black')

# Add labels and title
ax.set_xlabel('E-commerce Platforms', fontsize=12)
ax.set_ylabel('Satisfaction Rating (1 to 5)', fontsize=12)
ax.set_title('Customer Satisfaction Ratings Across E-commerce Platforms\nFirst Quarter 2023', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(positions + 2 * bar_width)
ax.set_xticklabels(platforms, fontsize=11)

# Add legend
ax.legend(title='Service Aspects', loc='upper right', fontsize=10)

# Annotate each bar with the rating value
for i in range(len(platforms)):
    for j in range(len(service_aspects)):
        ax.text(i + j * bar_width, ratings_data[i, j] + 0.05, f'{ratings_data[i, j]:.1f}', 
                ha='center', va='bottom', fontsize=9)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent text and labels from being cut off
plt.tight_layout()

# Show the plot
plt.show()