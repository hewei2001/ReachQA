import matplotlib.pyplot as plt
import numpy as np

# Define regions and energy sources
regions = ['Northlandia', 'Southovia', 'Eastalis', 'Westoros']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']

# Percentage data for each energy source in each region
data = {
    'Northlandia': [30, 25, 15, 20, 10],
    'Southovia': [20, 35, 30, 10, 5],
    'Eastalis': [25, 20, 40, 10, 5],
    'Westoros': [15, 30, 25, 25, 5]
}

# Prepare data arrays for plotting
data_values = np.array([data[region] for region in regions])

# Colors for energy sources
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FFD700']

# Aggregate data for the pie chart
total_per_source = np.sum(data_values, axis=0)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Stacked Bar Chart
bar_positions = np.arange(len(regions))
bottom_values = np.zeros(len(regions))
for i in range(len(energy_sources)):
    axs[0].bar(bar_positions, data_values[:, i], bottom=bottom_values, label=energy_sources[i], color=colors[i])
    bottom_values += data_values[:, i]

# Add percentage labels inside bars
for j, region in enumerate(regions):
    cumulative = 0
    for i, source in enumerate(energy_sources):
        cumulative += data[region][i]
        axs[0].text(j, cumulative - data[region][i] / 2, f"{data[region][i]}%", ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Set labels and title for the bar chart
axs[0].set_title('Distribution of Renewable Energy Consumption\nby Source in Global Regions (2023)', fontsize=14, pad=15)
axs[0].set_xticks(bar_positions)
axs[0].set_xticklabels(regions, rotation=0)
axs[0].set_xlabel('Regions', fontsize=12)
axs[0].set_ylabel('Percentage of Total Renewable Energy', fontsize=12)
axs[0].set_ylim(0, 100)
axs[0].legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1.02, 1))
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Pie Chart for the aggregated data
axs[1].pie(total_per_source, labels=energy_sources, autopct='%1.1f%%', startangle=140, colors=colors)
axs[1].set_title('Overall Contribution of Each Energy Source\nAcross All Regions', fontsize=14, pad=15)

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Show plot
plt.show()