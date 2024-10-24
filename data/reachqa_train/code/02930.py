import matplotlib.pyplot as plt
import numpy as np

# Data for the transport modes and their adoption rates (in thousands)
transport_modes = ['Hyperloop', 'Flying Cars', 'MagLev Trains', 'Teleports', 'Autonomous Buses']
adoption_rates = np.array([80, 120, 150, 60, 90])

# Colors corresponding to each transport mode
colors = ['#6a5acd', '#ff69b4', '#ff8c00', '#32cd32', '#4682b4']

# Positions of the bars on the x-axis
x_positions = np.arange(len(transport_modes))

# Plot the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(x_positions, adoption_rates, color=colors, edgecolor='black', width=0.6)

# Adding titles and labels
ax.set_title('Futuristic City Transport Adoption Rates\nin the Year 2050', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Transport Modes', fontsize=14)
ax.set_ylabel('Adoption Rate (in thousands)', fontsize=14)

# Assign the x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(transport_modes, fontsize=12, rotation=30, ha='right')

# Annotating the bars with their respective values
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}k', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Adding gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Adding a legend to describe the data more effectively
legend_labels = ['Rapid & Efficient', 'High-tech & Luxurious', 'Fast & Capacity', 'Instantaneous Travel', 'Eco-Friendly']
ax.legend(bars, legend_labels, title='Description', title_fontsize='12', loc='upper right', fontsize=10, frameon=False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()