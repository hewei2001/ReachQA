import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2020)

# Coffee consumption data (average cups per week)
young_adults = [15, 16, 18, 20, 23, 24, 25, 26, 28, 30]
middle_aged_adults = [20, 22, 23, 25, 26, 27, 29, 30, 32, 33]
seniors = [10, 11, 12, 13, 14, 14, 15, 16, 17, 18]

# Calculating average annual growth rate for each group
young_adults_growth = [(young_adults[i] - young_adults[i-1]) for i in range(1, len(young_adults))]
middle_aged_growth = [(middle_aged_adults[i] - middle_aged_adults[i-1]) for i in range(1, len(middle_aged_adults))]
seniors_growth = [(seniors[i] - seniors[i-1]) for i in range(1, len(seniors))]

# Annotations for significant points in the original line chart
annotations = {
    2013: ('Rising Trend', young_adults[3], "More students embracing coffee"),
    2016: ('Stabilization', middle_aged_adults[6], "Market saturation observed"),
    2019: ('Growth Peak', young_adults[9], "Coffee culture flourishes")
}

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Plotting the Line Chart
axs[0].plot(years, young_adults, '-o', label='Young Adults (18-35)', color='teal', markersize=6, linewidth=2)
axs[0].plot(years, middle_aged_adults, '-s', label='Middle-aged Adults (36-55)', color='orange', markersize=6, linewidth=2)
axs[0].plot(years, seniors, '-^', label='Seniors (56+)', color='purple', markersize=6, linewidth=2)

# Annotate significant points
for year, (text, y_position, note) in annotations.items():
    axs[0].annotate(f'{text}\n{note}', 
                    xy=(year, y_position), 
                    xytext=(year, y_position + 5),
                    arrowprops=dict(arrowstyle='->', color='black'),
                    fontsize=10, 
                    ha='center',
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Configure the first subplot
axs[0].set_title("Sips of Time: Coffee Consumption Trends\nAcross Generations (2010-2019)", fontsize=14, weight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Average Cups per Week", fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].set_xticks(years)

# Plotting the Bar Chart of Growth Rates
x_labels = years[1:]  # Exclude the first year because growth rate is calculated from 2011 onwards
bar_width = 0.25

axs[1].bar(x_labels - bar_width, young_adults_growth, width=bar_width, color='teal', label='Young Adults')
axs[1].bar(x_labels, middle_aged_growth, width=bar_width, color='orange', label='Middle-aged Adults')
axs[1].bar(x_labels + bar_width, seniors_growth, width=bar_width, color='purple', label='Seniors')

# Configure the second subplot
axs[1].set_title("Growth Rates: Coffee Consumption Increase\nPer Age Group (Annual)", fontsize=14, weight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Annual Growth (Cups/Week)", fontsize=12)
axs[1].set_xticks(years[1:])
axs[1].legend(loc='upper left', fontsize=10, frameon=False)
axs[1].grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()