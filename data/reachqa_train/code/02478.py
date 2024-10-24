import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2012, 2023)

# Renewable energy adoption data (% of total energy use)
new_york_renewables = np.array([10, 12, 15, 18, 23, 28, 35, 42, 50, 58, 65])
tokyo_renewables = np.array([8, 10, 14, 19, 25, 32, 40, 48, 56, 60, 68])
berlin_renewables = np.array([12, 14, 18, 24, 30, 37, 45, 55, 60, 65, 70])

# Calculate annual growth rates
ny_growth = np.diff(new_york_renewables) / new_york_renewables[:-1] * 100
tk_growth = np.diff(tokyo_renewables) / tokyo_renewables[:-1] * 100
bl_growth = np.diff(berlin_renewables) / berlin_renewables[:-1] * 100

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot line charts for each city (original plot)
ax1.plot(years, new_york_renewables, marker='o', label='New York', linestyle='-', linewidth=2, color='#1f77b4')
ax1.plot(years, tokyo_renewables, marker='s', label='Tokyo', linestyle='-', linewidth=2, color='#ff7f0e')
ax1.plot(years, berlin_renewables, marker='^', label='Berlin', linestyle='-', linewidth=2, color='#2ca02c')

# Annotate significant milestones
annotations = [
    {'year': 2016, 'ny_value': 23, 'tk_value': 25, 'bl_value': 30, 'note': 'Paris Agreement'},
    {'year': 2020, 'ny_value': 58, 'tk_value': 60, 'bl_value': 65, 'note': 'Local Initiatives Boost'}
]

for ann in annotations:
    ax1.annotate(ann['note'], xy=(ann['year'], ann['ny_value']), xytext=(-90, 30),
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#1f77b4'),
                 fontsize=10, color='#1f77b4', fontweight='bold')
    ax1.annotate(ann['note'], xy=(ann['year'], ann['tk_value']), xytext=(-90, -40),
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#ff7f0e'),
                 fontsize=10, color='#ff7f0e', fontweight='bold')
    ax1.annotate(ann['note'], xy=(ann['year'], ann['bl_value']), xytext=(50, 40),
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#2ca02c'),
                 fontsize=10, color='#2ca02c', fontweight='bold')

ax1.set_title('The Rise of Renewable Energy Adoption in Urban Areas\n(2012-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Renewable Energy Adoption (%)', fontsize=14)
ax1.set_xticks(years)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=12)

# Plot bar charts for annual growth rates (new subplot)
bar_width = 0.25
ax2.bar(years[:-1] - bar_width, ny_growth, width=bar_width, label='New York Growth', color='#1f77b4', align='center')
ax2.bar(years[:-1], tk_growth, width=bar_width, label='Tokyo Growth', color='#ff7f0e', align='center')
ax2.bar(years[:-1] + bar_width, bl_growth, width=bar_width, label='Berlin Growth', color='#2ca02c', align='center')

ax2.set_title('Annual Growth Rates of Renewable Energy Adoption', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Growth Rate (%)', fontsize=14)
ax2.set_xticks(years[:-1])
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()