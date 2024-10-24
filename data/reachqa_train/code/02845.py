import matplotlib.pyplot as plt
import numpy as np

# List of fruits
fruits = ["Apple", "Banana", "Orange", "Strawberry", "Mango"]

# Popularity data in percentages for each fruit across different regions
popularity = [
    [32, 15, 20, 18, 15],  # North America
    [25, 30, 15, 20, 10],  # Europe
    [18, 22, 35, 10, 25],  # Asia
    [20, 18, 15, 35, 12],  # South America
    [15, 25, 20, 15, 25]   # Africa
]

# Average popularity across all regions
average_popularity = np.mean(popularity, axis=0)
std_dev = np.std(popularity, axis=0)  # Simulated standard deviation for error bars

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15
x = np.arange(len(fruits))
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#D9D9D9']
region_labels = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# List to store bar containers
bar_containers = []

# Plot bars for each region with error bars
for i, (region_popularity, color, label) in enumerate(zip(popularity, colors, region_labels)):
    bars = ax.bar(x + i * bar_width, region_popularity, color=color, width=bar_width, edgecolor='black',
                  label=label, yerr=std_dev if i == 0 else None)  # Show error bars for one region
    bar_containers.append(bars)  # Append bar container to the list
    for bar, percentage in zip(bars, region_popularity):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                f'{percentage}%', ha='center', va='bottom', fontsize=9)

# Plot average popularity as a line
ax.plot(x + 2 * bar_width, average_popularity, marker='o', linestyle='-', color='purple', linewidth=2,
        label='Average Popularity')

# Add hatch patterns to bars for visual distinction
hatch_patterns = ['/', '\\', '|', '-', '+']
for i, bars in enumerate(bar_containers):  # Apply hatch patterns to each bar container
    for bar in bars:
        bar.set_hatch(hatch_patterns[i % len(hatch_patterns)])

# Set title and labels
ax.set_title('Fruits of the World:\nPopularity Survey 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Fruits', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(fruits)
ax.legend(title='Region', loc='upper left', fontsize=10)

# Grid and layout adjustments
ax.grid(True, linestyle='--', alpha=0.7, axis='y')
plt.tight_layout()

# Display the plot
plt.show()