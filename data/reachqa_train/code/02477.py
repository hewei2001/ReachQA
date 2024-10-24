import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2012, 2023)

# Renewable energy adoption data (% of total energy use)
new_york_renewables = [10, 12, 15, 18, 23, 28, 35, 42, 50, 58, 65]
tokyo_renewables = [8, 10, 14, 19, 25, 32, 40, 48, 56, 60, 68]
berlin_renewables = [12, 14, 18, 24, 30, 37, 45, 55, 60, 65, 70]

# Plotting
plt.figure(figsize=(14, 8))

# Plot line charts for each city
plt.plot(years, new_york_renewables, marker='o', label='New York', linestyle='-', linewidth=2, color='#1f77b4')
plt.plot(years, tokyo_renewables, marker='s', label='Tokyo', linestyle='-', linewidth=2, color='#ff7f0e')
plt.plot(years, berlin_renewables, marker='^', label='Berlin', linestyle='-', linewidth=2, color='#2ca02c')

# Annotate significant milestones
annotations = [
    {'year': 2016, 'ny_value': 23, 'tk_value': 25, 'bl_value': 30, 'note': 'Paris Agreement'},
    {'year': 2020, 'ny_value': 58, 'tk_value': 60, 'bl_value': 65, 'note': 'Local Initiatives Boost'}
]

for ann in annotations:
    plt.annotate(ann['note'],
                 xy=(ann['year'], ann['ny_value']), xycoords='data',
                 xytext=(-90, 30), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#1f77b4'),
                 fontsize=10, color='#1f77b4', fontweight='bold')

    plt.annotate(ann['note'],
                 xy=(ann['year'], ann['tk_value']), xycoords='data',
                 xytext=(-90, -40), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#ff7f0e'),
                 fontsize=10, color='#ff7f0e', fontweight='bold')

    plt.annotate(ann['note'],
                 xy=(ann['year'], ann['bl_value']), xycoords='data',
                 xytext=(50, 40), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#2ca02c'),
                 fontsize=10, color='#2ca02c', fontweight='bold')

# Title and labels
plt.title('The Rise of Renewable Energy Adoption in Urban Areas\n(2012-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Renewable Energy Adoption (%)', fontsize=14)

# Customize x-ticks for clarity
plt.xticks(years)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()