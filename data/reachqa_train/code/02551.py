import numpy as np
import matplotlib.pyplot as plt

# Define the years
years = np.arange(2010, 2021)

# Coffee consumption data (average cups per day)
teenagers_consumption = np.array([0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3])
adults_consumption = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5])
seniors_consumption = np.array([1.0, 1.0, 1.1, 1.1, 1.2, 1.3, 1.2, 1.1, 1.1, 1.1, 1.2])

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plotting the data
plt.plot(years, teenagers_consumption, color='blue', marker='o', linestyle='-', linewidth=2, label='Teenagers (13-19)')
plt.plot(years, adults_consumption, color='green', marker='s', linestyle='-', linewidth=2, label='Adults (20-39)')
plt.plot(years, seniors_consumption, color='red', marker='^', linestyle='-', linewidth=2, label='Seniors (40+)')

# Adding title and labels
plt.title('Trends in Coffee Consumption Across\nDifferent Age Groups (2010-2020)', fontsize=16, fontweight='bold', color='brown')
plt.xlabel('Year', fontsize=12, color='darkblue')
plt.ylabel('Average Cups of Coffee per Day', fontsize=12, color='darkblue')

# Configure x-ticks
plt.xticks(years, rotation=45)

# Adding a grid for better readability
plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight a specific year (e.g., 2015) and add text annotation
plt.axvline(x=2015, linestyle='--', color='purple', linewidth=1.5)
plt.text(2015.5, 3.2, 'Significant\nYear', verticalalignment='center', horizontalalignment='left', color='purple', fontsize=10)

# Annotations for specific years on the teenager's line
for year, cups in zip(years, teenagers_consumption):
    if year in [2010, 2015, 2020]:
        plt.annotate(f'{cups} cups', xy=(year, cups), textcoords='offset points', xytext=(-30, 10), ha='center', fontsize=9, color='blue')

# Set axis limits for better visualization
plt.xlim(2010, 2020)
plt.ylim(0, 4)

# Add a legend and position it appropriately
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()