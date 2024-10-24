import matplotlib.pyplot as plt
import numpy as np

# Coffee consumption data (kg/person annually) for selected countries over several years
coffee_consumption = {
    'Finland': [12.0, 12.1, 11.9, 12.2, 12.3, 12.1, 12.4, 12.2, 11.8, 12.0],
    'Norway': [9.8, 9.9, 9.5, 9.6, 10.0, 9.7, 9.9, 10.1, 9.8, 9.9],
    'Iceland': [9.0, 8.8, 9.2, 9.1, 8.9, 9.0, 9.3, 9.1, 8.8, 9.2],
    'Denmark': [8.7, 8.6, 8.8, 8.9, 8.7, 8.8, 8.9, 8.6, 8.7, 8.8],
    'Netherlands': [8.2, 8.1, 8.3, 8.2, 8.4, 8.2, 8.3, 8.1, 8.2, 8.3]
}

# Prepare data for box plot
data = [coffee_consumption[country] for country in coffee_consumption]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal box plot
bplot = ax.boxplot(data, vert=False, patch_artist=True, notch=True, labels=coffee_consumption.keys(), whis=[5, 95])

# Customize the appearance of the boxes
colors = ['#FFDDC1', '#FFC8A2', '#FFB694', '#FFA78B', '#FF927B']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Set title and axis labels
ax.set_title('Coffee Consumption per Person: Top Nations\nMeasured in Kilograms Annually', fontsize=14, fontweight='bold')
ax.set_xlabel('Average Annual Coffee Consumption (kg)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)

# Enable grid for the x-axis
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate median values
for i, country in enumerate(coffee_consumption):
    median_value = np.median(coffee_consumption[country])
    ax.text(median_value + 0.1, i + 1, f'{median_value:.1f} kg', va='center', ha='left', fontsize=10, color='darkblue')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()