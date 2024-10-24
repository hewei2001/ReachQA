import matplotlib.pyplot as plt
import numpy as np

# Data representing the percentage contribution of each energy source
energy_sources = ['Solar Energy', 'Wind Power', 'Geothermal', 'Hydroelectric', 'Nuclear']
percentages = [35, 25, 15, 20, 5]  # Predefined percentages

# Colors for each energy source
colors = ['#FFD700', '#87CEEB', '#DAA520', '#4682B4', '#C0C0C0']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the bars
bars = ax.barh(energy_sources, percentages, color=colors)

# Adding data labels on the bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}%', 
            ha='center', va='center', fontsize=11, fontweight='bold', color='black')

# Customizing the plot
ax.set_title('Energy Source Distribution\nin Electra City - 2075', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Percentage Contribution', fontsize=12)
ax.set_xlim(0, 50)  # Setting x-limit to accommodate data labels and improve visual balance

# Hide y-axis grid lines and add x-axis grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()