import matplotlib.pyplot as plt
import numpy as np

# Define centuries and writing materials
centuries = ['1000 BCE', '500 BCE', '0 CE', '500 CE', '1000 CE', '1500 CE', '1800 CE', '1900 CE', '21st Century']
materials = ['Clay Tablets', 'Papyrus', 'Parchment', 'Paper', 'Digital']

# Estimated usage data (%)
usage = np.array([
    [80, 20, 0, 0, 0],    # 1000 BCE
    [60, 40, 0, 0, 0],    # 500 BCE
    [20, 60, 20, 0, 0],   # 0 CE
    [0, 50, 50, 0, 0],    # 500 CE
    [0, 10, 70, 20, 0],   # 1000 CE
    [0, 0, 20, 80, 0],    # 1500 CE
    [0, 0, 10, 90, 0],    # 1800 CE
    [0, 0, 5, 85, 10],    # 1900 CE
    [0, 0, 0, 30, 70],    # 21st Century
])

# Estimated literacy rates (%)
literacy_rates = [1, 2, 3, 5, 8, 15, 40, 70, 95]

# Set up the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Colors for each material
colors = ['#8B4513', '#FFD700', '#FF4500', '#1E90FF', '#32CD32']

# Plot the data as stacked bars
bottoms = np.zeros(len(centuries))
for i, (material, color) in enumerate(zip(materials, colors)):
    ax1.bar(centuries, usage[:, i], label=material, color=color, bottom=bottoms, edgecolor='white')
    bottoms += usage[:, i]

# Customize the plot
ax1.set_xlabel('Centuries', fontsize=12)
ax1.set_ylabel('Estimated Usage (%)', fontsize=12)
ax1.set_title('The Evolution of Writing Materials\nand Literacy Rates Over Centuries', fontsize=16, weight='bold', pad=20)
ax1.set_ylim(0, 100)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Rotate x-tick labels for better readability
plt.xticks(rotation=45)

# Add data labels to the bars
for idx, (century, bottom) in enumerate(zip(centuries, bottoms)):
    for j, usage_value in enumerate(usage[idx]):
        if usage_value > 0:
            ax1.text(
                x=century, y=bottom - usage_value/2, s=f'{usage_value}%', ha='center', va='center', fontsize=9, color='white'
            )

# Add a secondary y-axis for literacy rates
ax2 = ax1.twinx()
ax2.plot(centuries, literacy_rates, color='purple', marker='o', linestyle='-', linewidth=2, label='Estimated Literacy Rate')
ax2.set_ylabel('Literacy Rate (%)', fontsize=12)
ax2.set_ylim(0, 100)

# Add a legend for the line plot
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()