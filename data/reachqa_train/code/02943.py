import matplotlib.pyplot as plt
import numpy as np

# Countries and food categories
countries = ['USA', 'India', 'Brazil', 'China']
categories = ['Grains', 'Fruits', 'Vegetables']

# Data: Production in million metric tons
production_data = {
    'Grains': [420, 320, 210, 480],
    'Fruits': [110, 130, 170, 150],
    'Vegetables': [140, 190, 150, 210]
}

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Colors for each category
colors = ['#FFCC00', '#FF6600', '#00CC66']

# Initialize bottom for stacking
bottom = np.zeros(len(countries))

# Plot each category stacked on top of the previous one
for idx, category in enumerate(categories):
    values = production_data[category]
    ax.bar(countries, values, bottom=bottom, color=colors[idx], edgecolor='black', label=category)
    # Update the bottom for the next stack
    bottom += values

# Title and labels
ax.set_title("Global Food Production Composition:\nGrains, Fruits, and Vegetables", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Countries", fontsize=12)
ax.set_ylabel("Production Volume (Million Metric Tons)", fontsize=12)

# Add legend and grid
ax.legend(title='Food Categories', loc='upper left', fontsize=10)
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

# Annotate each bar segment for clarity
for i, country in enumerate(countries):
    for j, category in enumerate(categories):
        value = production_data[category][i]
        ax.text(i, bottom[i] - value/2, f'{value}', ha='center', va='center', color='white', fontsize=10)

# Avoid overlapping of x-tick labels
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()