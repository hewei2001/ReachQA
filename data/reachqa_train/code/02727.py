import matplotlib.pyplot as plt
import numpy as np

# Extending graduation rate data (%) for more departments over a 10-year span
years = np.arange(2010, 2020)
data_dict = {
    'Comp Sci': [85, 88, 90, 87, 89, 92, 91, 93, 90, 94],
    'Arts & Hum': [70, 75, 72, 74, 73, 76, 78, 77, 80, 79],
    'Business': [82, 80, 85, 83, 81, 84, 86, 88, 87, 89],
    'Biology': [78, 76, 80, 79, 77, 81, 82, 85, 83, 86],
    'Mech Eng': [88, 85, 87, 86, 89, 90, 92, 91, 94, 95],
    'Electrical Eng': [80, 82, 84, 83, 81, 85, 87, 88, 86, 89],
    'Mathematics': [75, 77, 79, 78, 76, 80, 82, 81, 84, 86],
    'Physics': [74, 72, 75, 77, 76, 78, 80, 79, 81, 83]
}

# Collecting data into a list for vertical box plot
data = [rates for rates in data_dict.values()]

# Set up the main figure and grid
fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Main Box Plot
ax = axs[0]
bp = ax.boxplot(data, patch_artist=True, vert=True, widths=0.6, notch=True)

# Define unique colors for each box
colors = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightcoral', 'lightcyan', 'lightgrey', 'lightgoldenrodyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add grid and customize axis
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.set_xticklabels(data_dict.keys(), fontsize=10, rotation=30, ha='right')
ax.set_ylabel('Graduation Rate (%)', fontsize=12)
ax.set_title('Variability in Graduation Rates Across University Departments\n(2010-2019)',
             fontsize=14, fontweight='bold', pad=15)

# Highlighting medians with annotations
for i, median in enumerate(bp['medians']):
    x_median = median.get_xdata()[1]
    y_median = median.get_ydata()[1]
    ax.annotate(f'{y_median:.0f}%', xy=(x_median, y_median), xytext=(0, 5), 
                textcoords='offset points', color='blue', fontsize=10, ha='center')

# Add subplot for average trends
ax2 = axs[1]
for department, rates in data_dict.items():
    ax2.plot(years, rates, marker='o', label=department)

# Customize plot elements for clarity
ax2.set_ylabel('Graduation Rate (%)', fontsize=12)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_title('Trend Analysis of Graduation Rates\nOver Time by Department',
              fontsize=14, fontweight='bold', pad=15)
ax2.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=9)
ax2.grid(True, linestyle='--', color='grey', alpha=0.5)

# Tight layout to avoid overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the chart
plt.show()