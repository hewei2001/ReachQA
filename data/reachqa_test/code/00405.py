import matplotlib.pyplot as plt
import numpy as np

# Cargo capacities (in millions of tons per year) for different transportation modes
# Data fabricated for demonstration purposes
maritime_shipping = [8000, 9200, 10500, 12000, 13000]
air_freight = [50, 60, 70, 75, 80]
rail_transport = [3000, 3300, 3500, 3700, 4000]
road_transport = [1500, 1600, 1700, 1800, 1900]

# Define the years for which data is available
years = [2000, 2005, 2010, 2015, 2020]

# Combine data for all transportation modes
transport_data = [maritime_shipping, air_freight, rail_transport, road_transport]

# Transportation modes
modes = ['Maritime Shipping', 'Air Freight', 'Rail Transport', 'Road Transport']

# Prepare data for plotting
bar_width = 0.18
index = np.arange(len(years))

# Calculate the offset for grouped bars
offset = bar_width * (len(modes) / 2)

fig, ax = plt.subplots(figsize=(12, 8))

# Set the colors for each mode for distinct appearance
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

# Plot grouped bar charts for each transportation mode with colors
for i, (mode, color) in enumerate(zip(modes, colors)):
    # Calculate the position for each bar group
    pos = [x + bar_width * i - offset for x in index]
    # Plot the grouped bar chart
    bars = ax.bar(pos, transport_data[i], bar_width, label=mode, color=color, edgecolor='black')

    # Annotate the bars with the cargo capacity value
    for bar, val in zip(bars, transport_data[i]):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, '{}'.format(val),
                ha='center', va='bottom', rotation=45, fontsize=8, color='black')

# Set the labels and titles
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Cargo Capacity (in millions of tons per year)', fontsize=12, fontweight='bold')
ax.set_title('Evolution of Cargo Capacity\nAcross Major Transportation Modes\n(2000-2020)', fontsize=14, fontweight='bold')

# Set the x-axis to only show labels where we have data
ax.set_xticks(index)
ax.set_xticklabels(years)
ax.tick_params(axis='both', which='major', labelsize=10)

# Set grid lines for y-axis, only on major ticks
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.5)

# Set background color to light gray for better visual separation
ax.set_facecolor('#f0f0f0')

# Place legend inside the chart with a transparent background
ax.legend(framealpha=0.5, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adjust layout for a cleaner appearance
plt.tight_layout()

# Display the plot
plt.show()