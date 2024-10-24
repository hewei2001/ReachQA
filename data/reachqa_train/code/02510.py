import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
pollution_sources = [
    'Transportation Emissions', 
    'Industrial Discharges', 
    'Residential Heating', 
    'Construction Dust', 
    'Agricultural Activities', 
    'Waste Burning', 
    'Other Sources'
]
percentages = [30, 25, 15, 10, 10, 5, 5]

# Colors for each pollution source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Explode the slices slightly to highlight them
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Set up the figure
fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121)

# 2D Pie Chart
ax1.pie(
    percentages, labels=pollution_sources, autopct='%1.1f%%', startangle=140, colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}, explode=explode
)
ax1.set_title("Air Pollution Sources in Greenfield City", fontsize=14, pad=30)

# Secondary chart: Bar chart for visualization over time (example data)
years = np.array([2018, 2019, 2020, 2021])
emission_changes = np.array([
    [20, 22, 24, 30],  # Transportation
    [23, 25, 27, 25],  # Industrial
    [13, 14, 15, 15],  # Residential
    [9, 10, 10, 10],   # Construction
    [8, 8, 9, 10],     # Agricultural
    [4, 4, 5, 5],      # Waste Burning
    [4, 4, 5, 5]       # Other
])

ax2 = fig.add_subplot(122)
bar_width = 0.1
indices = np.arange(len(years))

for i, source in enumerate(pollution_sources):
    ax2.bar(indices + i * bar_width, emission_changes[i], bar_width, label=source, color=colors[i])

ax2.set_xticks(indices + bar_width * (len(pollution_sources) / 2 - 1))
ax2.set_xticklabels(years)
ax2.set_title('Emission Changes Over Time', fontsize=14)
ax2.set_xlabel('Year')
ax2.set_ylabel('Emission Percentage (%)')
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Pollution Sources", fontsize=8)
ax2.grid(True)

# Adjust layout for better visibility and to prevent overlap
plt.tight_layout()
plt.subplots_adjust(right=0.85)

# Display the chart
plt.show()