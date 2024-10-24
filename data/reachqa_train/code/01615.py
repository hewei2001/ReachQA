import matplotlib.pyplot as plt
import numpy as np

# Define data
regions = ['North America', 'Europe', 'Asia']
coffee_types = ['Espresso', 'Cappuccino', 'Latte']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Monthly consumption data for each coffee type in each region
consumption_data = {
    'North America': {
        'Espresso': [40, 45, 50, 60, 70, 75, 80, 70, 60, 55, 45, 40],
        'Cappuccino': [20, 22, 25, 30, 35, 40, 45, 50, 45, 40, 30, 20],
        'Latte': [60, 65, 70, 75, 80, 85, 90, 85, 80, 75, 65, 60]
    },
    'Europe': {
        'Espresso': [70, 75, 80, 85, 90, 95, 100, 95, 90, 85, 75, 70],
        'Cappuccino': [50, 55, 60, 65, 70, 75, 80, 75, 70, 65, 55, 50],
        'Latte': [40, 45, 50, 55, 60, 65, 70, 65, 60, 55, 45, 40]
    },
    'Asia': {
        'Espresso': [30, 35, 40, 50, 60, 65, 70, 60, 50, 45, 35, 30],
        'Cappuccino': [10, 12, 15, 18, 22, 25, 30, 28, 25, 20, 15, 10],
        'Latte': [50, 55, 60, 65, 70, 75, 80, 75, 70, 65, 55, 50]
    }
}

# Function to plot a rose chart for a given region
def plot_rose_chart(region_data, ax, title):
    num_months = len(months)
    angles = np.linspace(0, 2 * np.pi, num_months, endpoint=False).tolist()
    
    for coffee_type, values in region_data.items():
        values += values[:1]  # Repeat the first value to close the circle
        angles_complete = angles + angles[:1]
        ax.fill(angles_complete, values, alpha=0.25, label=coffee_type)
    
    ax.set_xticks(angles)
    ax.set_xticklabels(months)
    ax.set_yticks([])
    ax.set_title(title, fontsize=12)

# Initialize the plot
fig, axs = plt.subplots(1, 3, subplot_kw=dict(projection='polar'), figsize=(15, 6))

# Plot each region's data
for i, region in enumerate(regions):
    plot_rose_chart(consumption_data[region], axs[i], f'{region} Coffee Consumption')

# Add a legend outside of the plots
axs[2].legend(loc='upper left', bbox_to_anchor=(1.1, 1.0), title="Coffee Types")

# Overall title and layout adjustments
fig.suptitle('Global Coffee Consumption Patterns\nAverage Monthly Cups by Coffee Type and Region', fontsize=16, fontweight='bold', y=1.1)
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Show the plot
plt.show()