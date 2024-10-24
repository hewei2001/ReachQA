import matplotlib.pyplot as plt
import numpy as np

# Define the expanded regions and spice types
regions = ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Oceania', 'Middle East', 'Antarctica']
spice_types = ['Cumin', 'Cinnamon', 'Paprika', 'Turmeric', 'Pepper', 'Nutmeg']

# Artificial data representing the average annual spice consumption in kilograms
data = {
    'Cumin': [0.8, 1.5, 1.0, 1.2, 5.0, 0.9, 3.4, 0.0],
    'Cinnamon': [0.6, 1.0, 2.5, 1.8, 1.2, 0.7, 2.8, 0.0],
    'Paprika': [1.0, 1.8, 2.0, 1.5, 0.8, 1.0, 0.9, 0.0],
    'Turmeric': [0.5, 0.7, 0.6, 0.9, 3.5, 0.8, 1.5, 0.0],
    'Pepper': [1.5, 1.9, 2.7, 1.6, 2.5, 1.2, 0.7, 0.0],
    'Nutmeg': [0.3, 0.4, 0.5, 0.6, 0.2, 0.5, 0.4, 0.0]
}

# Calculate cumulative consumption for the line plot
cumulative_consumption = np.array([sum([data[spice][i] for spice in spice_types]) for i in range(len(regions))])

# Bar width
bar_width = 0.13

# Create figure and axes for the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Position of each group of bars on the x-axis
x_indexes = np.arange(len(regions))

# Colors for the spices
colors = ['darkorange', 'saddlebrown', 'firebrick', 'goldenrod', 'black', 'darkgreen']

# Plot bars for each spice
for i, (spice, consumption) in enumerate(data.items()):
    ax.bar(x_indexes - bar_width*(len(spice_types)/2) + i*bar_width, consumption, width=bar_width, label=spice, color=colors[i], alpha=0.8)

# Plot cumulative consumption as a line plot
ax.plot(x_indexes, cumulative_consumption, color='blue', marker='o', label='Cumulative Consumption', linewidth=2)

# Add titles and labels
ax.set_title('Culinary Traditions Around the World:\nDetailed Spice Consumption by Region', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Average Annual Consumption (kg)', fontsize=12)
ax.set_xticks(x_indexes)
ax.set_xticklabels(regions, rotation=30, ha='right')

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=10, title='Spice Types')

# Customize gridlines
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Display data values on each bar
for i, region in enumerate(regions):
    y_offset = 0.15
    for j, spice in enumerate(spice_types):
        ax.text(x_indexes[i] - bar_width*(len(spice_types)/2) + j*bar_width, data[spice][i] + y_offset, f'{data[spice][i]:.1f}', 
                ha='center', va='bottom', fontsize=8)

# Annotate cumulative consumption
for i, value in enumerate(cumulative_consumption):
    ax.annotate(f'{value:.1f}', xy=(x_indexes[i], value), xytext=(5, 5), textcoords='offset points', fontsize=9, color='blue')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()