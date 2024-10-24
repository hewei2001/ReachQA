import matplotlib.pyplot as plt
import numpy as np

# Define the regions for the x-axis
regions = ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Oceania']

# Artificial data representing the average annual spice consumption in kilograms
cumin_consumption = [0.8, 1.5, 1.0, 1.2, 5.0, 0.9]
cinnamon_consumption = [0.6, 1.0, 2.5, 1.8, 1.2, 0.7]
paprika_consumption = [1.0, 1.8, 2.0, 1.5, 0.8, 1.0]
turmeric_consumption = [0.5, 0.7, 0.6, 0.9, 3.5, 0.8]

# Bar width
bar_width = 0.2

# Create figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Position of each group of bars on the x-axis
x_indexes = np.arange(len(regions))

# Plot bars for each spice
ax.bar(x_indexes - bar_width*1.5, cumin_consumption, width=bar_width, label='Cumin', color='darkorange', alpha=0.8)
ax.bar(x_indexes - bar_width*0.5, cinnamon_consumption, width=bar_width, label='Cinnamon', color='saddlebrown', alpha=0.8)
ax.bar(x_indexes + bar_width*0.5, paprika_consumption, width=bar_width, label='Paprika', color='firebrick', alpha=0.8)
ax.bar(x_indexes + bar_width*1.5, turmeric_consumption, width=bar_width, label='Turmeric', color='goldenrod', alpha=0.8)

# Add titles and labels
ax.set_title('Culinary Traditions Around the World:\nAnnual Spice Consumption by Region', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Average Annual Consumption (kg)', fontsize=12)
ax.set_xticks(x_indexes)
ax.set_xticklabels(regions, rotation=30, ha='right')

# Add a legend to the plot
ax.legend(loc='upper right', fontsize=10, title='Spice Types')

# Customize gridlines
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate with the most consumed spice in each region
annotations = [
    'Most Cumin', 'Most Cinnamon', 'Most Cinnamon', 
    'Most Cinnamon', 'Most Turmeric', 'Most Paprika'
]
for i, txt in enumerate(annotations):
    ax.annotate(txt, xy=(x_indexes[i], max(cumin_consumption[i], cinnamon_consumption[i], paprika_consumption[i], turmeric_consumption[i]) + 0.2), 
                fontsize=9, ha='center', color='blue')

# Display data values on each bar
for i in range(len(regions)):
    ax.text(x_indexes[i] - bar_width*1.5, cumin_consumption[i] + 0.1, f'{cumin_consumption[i]:.1f}', ha='center', va='bottom', fontsize=9)
    ax.text(x_indexes[i] - bar_width*0.5, cinnamon_consumption[i] + 0.1, f'{cinnamon_consumption[i]:.1f}', ha='center', va='bottom', fontsize=9)
    ax.text(x_indexes[i] + bar_width*0.5, paprika_consumption[i] + 0.1, f'{paprika_consumption[i]:.1f}', ha='center', va='bottom', fontsize=9)
    ax.text(x_indexes[i] + bar_width*1.5, turmeric_consumption[i] + 0.1, f'{turmeric_consumption[i]:.1f}', ha='center', va='bottom', fontsize=9)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()