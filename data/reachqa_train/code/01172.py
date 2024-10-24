import matplotlib.pyplot as plt
import numpy as np

# Years for data
years = np.arange(2010, 2020)

# Coffee consumption data (average cups per week)
young_adults = [15, 16, 18, 20, 23, 24, 25, 26, 28, 30]
middle_aged_adults = [20, 22, 23, 25, 26, 27, 29, 30, 32, 33]
seniors = [10, 11, 12, 13, 14, 14, 15, 16, 17, 18]

# Annotations for significant points
annotations = {
    2013: ('Rising Trend', young_adults[3], "More students embracing coffee"),
    2016: ('Stabilization', middle_aged_adults[6], "Market saturation observed"),
    2019: ('Growth Peak', young_adults[9], "Coffee culture flourishes")
}

# Plotting the Line Chart with Annotations
plt.figure(figsize=(14, 8))

# Plotting each age group's data
plt.plot(years, young_adults, '-o', label='Young Adults (18-35)', color='teal', markersize=6, linewidth=2)
plt.plot(years, middle_aged_adults, '-s', label='Middle-aged Adults (36-55)', color='orange', markersize=6, linewidth=2)
plt.plot(years, seniors, '-^', label='Seniors (56+)', color='purple', markersize=6, linewidth=2)

# Annotate significant points
for year, (text, y_position, note) in annotations.items():
    plt.annotate(f'{text}\n{note}', 
                 xy=(year, y_position), 
                 xytext=(year, y_position + 5),
                 arrowprops=dict(arrowstyle='->', color='black'),
                 fontsize=10, 
                 ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Add title and labels
plt.title("Sips of Time: Coffee Consumption Trends\nAcross Generations (2010-2019)", fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Cups per Week", fontsize=12)

# Adding legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Set x-ticks to match years and ensure clean x-axis
plt.xticks(years)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()