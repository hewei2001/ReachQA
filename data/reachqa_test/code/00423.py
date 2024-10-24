import numpy as np
import matplotlib.pyplot as plt

# City names
cities = ['New York', 'Paris', 'Tokyo', 'London', 'Sydney']

# Data for coffee consumption (cups per day) in each city
coffee_data = [
    [1.5, 1.2, 1.7, 1.8, 1.6, 2.2, 2.4, 2.1, 1.9, 1.3],  # New York
    [1.0, 0.8, 1.2, 1.3, 1.4, 1.5, 1.6, 1.1, 0.9, 1.0],  # Paris
    [2.2, 2.4, 2.5, 2.6, 2.1, 1.8, 1.9, 2.3, 2.4, 2.7],  # Tokyo
    [1.4, 1.6, 1.2, 1.3, 1.5, 1.7, 1.1, 1.0, 1.7, 1.8],  # London
    [1.6, 1.8, 1.5, 1.7, 2.0, 2.2, 2.1, 1.9, 1.5, 1.4]   # Sydney
]

# Set the figure size
plt.figure(figsize=(10, 8), facecolor='aliceblue')  # Add a subtle background color

# Custom color palette and additional font settings
colors = ['skyblue', 'springgreen', 'lightcoral', 'slategray', 'gold']
plt.rcParams['font.family'] = 'Arial'  # Change font style for better aesthetics
plt.rcParams['font.size'] = 12

# Create horizontal box plots for each city
boxplot = plt.boxplot(coffee_data, positions=np.arange(1, len(cities) + 1), vert=False, 
                      patch_artist=True, widths=0.7)

# Customize the appearance of the boxes, whiskers, outliers, and medians
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(2)

for whisker in boxplot['whiskers']:
    whisker.set(color='black', linewidth=1)

for cap in boxplot['caps']:
    cap.set(color='black', linewidth=1)

for median in boxplot['medians']:
    median.set(color='red', linewidth=2)

for flier in boxplot['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)  # Change outlier color to red for emphasis

# Customize grid lines to be less prominent
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

# Set the y-axis to represent the city names and adjust label rotation for better visibility
plt.yticks(np.arange(1, len(cities) + 1), cities)

# Adjust x-axis and y-axis limits for better visualization
plt.xlim(0.5, 3.0)
plt.ylim(0.5, 5.5)

# Add a title with subtitles, and adjust labels
plt.title('Comparative Analysis\nof Coffee Consumption\nAcross Major Cities', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Cups of Coffee Consumed Daily', fontsize=16)
plt.ylabel('Cities', fontsize=16)

# Add boxplot annotations for median values
medians = [np.median(data) for data in coffee_data]
for median, pos in zip(medians, np.arange(1, len(cities) + 1)):
    plt.text(median, pos, f'Median = {median:.2f}\n', ha='center', va='center', color='red', fontsize=14)

# Add a legend for the different elements in the boxplot
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=f'{city}', markersize=10) for color, city in zip(colors, cities)]
legend_elements += [plt.Line2D([0], [0], color='red', lw=3, label='Median')]
plt.legend(handles=legend_elements, bbox_to_anchor=(1, 1))

# Automatically adjust the image layout before plt.show() via tight_layout()
plt.tight_layout()

# Show the plot
plt.show()