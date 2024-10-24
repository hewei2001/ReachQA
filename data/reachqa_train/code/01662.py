import matplotlib.pyplot as plt
import numpy as np

# Define the expanded data for the galactic citizenship distribution
citizenship_labels = [
    'Full Citizens', 
    'Temporary Residents', 
    'Probationary Citizens', 
    'Non-Aligned Beings', 
    'Galactic Nomads', 
    'Exiled or Outlawed',
    'Under Review', 
    'New Settlers'
]
citizenship_sizes = [30, 18, 12, 8, 6, 6, 10, 10]

# Ensure that the sum of percentages is 100
assert sum(citizenship_sizes) == 100, "The citizenship sizes must sum up to 100."

# Define a more nuanced color palette
colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703', '#fb8500', '#d62828', '#2a9d8f', '#e9c46a']

# Explode certain slices to emphasize them
explode = (0.1, 0, 0, 0.1, 0, 0, 0, 0.1) 

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 9))
fig.suptitle('Galactic Federation Citizenship Analysis\nYear 3085', fontsize=20, weight='bold')

# Pie chart
ax[0].pie(
    citizenship_sizes, explode=explode, labels=citizenship_labels, colors=colors,
    autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='w', linewidth=1.5), shadow=True
)
ax[0].set_title('Citizenship Distribution', fontsize=16, pad=20)

# Bar chart to show hypothetical changes in each group's size over past decades
years = np.arange(3080, 3086)
bar_labels = citizenship_labels[:5]
# Hypothetical data showing population trends over time
population_trends = {
    'Full Citizens': [32, 31, 30, 31, 30, 30],
    'Temporary Residents': [20, 19, 18, 18, 18, 18],
    'Probationary Citizens': [15, 14, 13, 13, 12, 12],
    'Non-Aligned Beings': [8, 8, 9, 8, 8, 8],
    'Galactic Nomads': [5, 5, 6, 6, 6, 6]
}

for index, (key, values) in enumerate(population_trends.items()):
    ax[1].plot(years, values, label=key, marker='o', linewidth=2, color=colors[index])

ax[1].set_title('Historical Citizenship Trends (3080-3085)', fontsize=16, pad=20)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Population Percentage', fontsize=12)
ax[1].set_ylim(0, 35)  # Set y-limits to give some space to the line plot
ax[1].legend(title="Citizenship Status", loc='upper left', fontsize=10)

# Automatically adjust the layout to fit elements within the figure
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for the main title
plt.show()