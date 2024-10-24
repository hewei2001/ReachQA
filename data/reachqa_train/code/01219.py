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

# Start from an initial base value
base_value = 50  # Hypothetical starting usage percentage

# Initialize lists to hold net changes
net_changes = [base_value]

# Compute cumulative net changes for each year
for year in range(len(years) - 1):
    yearly_change = sum(change_list[year] for change_list in changes.values())
    cumulative_change = net_changes[-1] + yearly_change
    net_changes.append(cumulative_change)

# Calculate final net change for labeling
final_value = net_changes[-1]

# Plotting the Waterfall Chart
fig, ax = plt.subplots(figsize=(14, 8))

# Create bar plots
colors = ['green' if net_changes[i] - net_changes[i-1] > 0 else 'red' for i in range(1, len(net_changes))]
for i in range(1, len(net_changes)):
    ax.bar(i, net_changes[i] - net_changes[i-1], bottom=net_changes[i-1], color=colors[i-1], edgecolor='k')

# Connectors between bars
for i in range(1, len(net_changes)):
    ax.plot([i-1, i], [net_changes[i-1], net_changes[i-1]], 'k--', lw=0.5)

# Set titles and labels
ax.set_xticks(range(1, len(years)))  # Correct number of ticks
ax.set_xticklabels([f'{years[i]}-{years[i+1]}' for i in range(len(years) - 1)], rotation=45, ha='right', fontsize=10)
ax.set_title('Transportation Evolution in Neotron\nA Decade of Transition (2020-2030)', fontsize=14, fontweight='bold')
ax.set_ylabel('Change in Transport Mode Usage (%)', fontsize=12)

# Adding value labels above bars
for i in range(1, len(net_changes)):
    ax.text(i, net_changes[i], f'{net_changes[i]:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Indicate starting point
ax.text(0, base_value, f'Start: {base_value}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='blue')

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()