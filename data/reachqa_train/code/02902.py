import matplotlib.pyplot as plt
import numpy as np

# Countries in Candyland
countries = ['Sweetopia', 'Chocoria', 'Cocotown', 'Nougatville', 'Truffleheim']
# Annual chocolate consumption per person in kilograms
consumption = [35, 40, 22, 30, 45]

# Set positions and width for the bars
x_pos = np.arange(len(countries))
width = 0.6

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(x_pos, consumption, width, color=['#D2691E', '#8B4513', '#A0522D', '#CD853F', '#F4A460'],
              edgecolor='black', linewidth=1.2)

# Title and labels with adjustments
ax.set_title('Annual Chocolate Consumption\nper Country in Candyland', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Countries', fontsize=12)
ax.set_ylabel('Chocolate Consumption (kg/person)', fontsize=12)
ax.set_xticks(x_pos)
ax.set_xticklabels(countries, fontsize=11, rotation=15, ha='right')

# Adding data labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval} kg', ha='center', va='bottom', fontsize=10)

# Customize and enhance visual clarity
ax.set_ylim(0, 50)
ax.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for better visual reference

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()