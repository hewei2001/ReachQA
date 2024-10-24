import matplotlib.pyplot as plt
import numpy as np

# Define years for which changes are tracked
years = np.arange(2020, 2031)

# Define the change in percentage points for each transportation mode
changes = {
    "Traditional Cars": [-5, -7, -4, -6, -3, -4, -5, -6, -7, -5, -6],
    "Public Transport": [2, 1, 3, 4, 3, 2, 3, 4, 3, 2, 3],
    "Electric Vehicles": [3, 5, 7, 5, 6, 7, 5, 6, 7, 6, 8],
    "Hyperloop": [0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8],
    "Drones": [0, 0, 0, 1, 1, 2, 3, 4, 5, 6, 7],
    "Bicycles & Walking": [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
}

# Additional data for overlay plot (e.g., CO2 emission reductions over the years)
emissions_reduction = [5, 4.8, 4.6, 4.5, 4.3, 4.0, 3.8, 3.5, 3.3, 3.0, 2.8]

# Base usage percentage
base_value = 50

# Initialize lists to hold net changes and colors
net_changes = [base_value]
colors = []

# Compute cumulative net changes for each year and determine bar colors
for year in range(len(years) - 1):
    cumulative_change = base_value
    for mode, change_list in changes.items():
        cumulative_change += change_list[year]
    net_changes.append(cumulative_change)
    colors.append('green' if cumulative_change > net_changes[-2] else 'red')

# Calculate final net change for labeling
final_value = net_changes[-1]

# Create the main plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Waterfall Chart: Create bar plots
for i in range(1, len(net_changes)):
    ax1.bar(i, net_changes[i] - net_changes[i-1], bottom=net_changes[i-1], color=colors[i-1], edgecolor='k')

# Connectors between bars
for i in range(1, len(net_changes)):
    ax1.plot([i-1, i], [net_changes[i-1], net_changes[i-1]], 'k--', lw=0.5)

# Set titles and labels
ax1.set_xticks(range(1, len(net_changes)))
ax1.set_xticklabels([f'{years[i]}-{years[i+1]}' for i in range(len(years) - 1)], rotation=45, ha='right', fontsize=10)
ax1.set_title('Transportation Evolution in Neotron\nA Decade of Transition (2020-2030)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Change in Transport Mode Usage (%)', fontsize=12)

# Adding value labels above bars
for i in range(1, len(net_changes)):
    ax1.text(i, net_changes[i], f'{net_changes[i]:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Indicate starting point
ax1.text(0, base_value, f'Start: {base_value}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='blue')

# Overlay Plot: CO2 Emissions Reduction
ax2 = ax1.twinx()  # Create a second y-axis
ax2.plot(range(1, len(emissions_reduction) + 1), emissions_reduction, color='blue', marker='o', linestyle='-', label='CO2 Emission Reduction')
ax2.set_ylabel('CO2 Emission Reduction (%)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Add a legend for the line plot
ax2.legend(loc='upper right')

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()