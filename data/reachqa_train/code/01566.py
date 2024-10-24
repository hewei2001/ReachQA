import matplotlib.pyplot as plt
import numpy as np

# Data setup
countries = ['USA', 'China', 'Germany', 'India', 'Norway', 'Brazil']
adoption_rates = [55, 70, 65, 45, 85, 50]  # Percentage of vehicles that are electric
colors = ['#4a7c59', '#f4a261', '#2a9d8f', '#e76f51', '#f4a261', '#264653']

# Set positions and width for the bars
x_pos = np.arange(len(countries))
bar_width = 0.6

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(x_pos, adoption_rates, color=colors, edgecolor='white', linewidth=0.8, width=bar_width)

# Title and labels
ax.set_title('The Dawn of Renewable Transport:\nElectric Vehicle Adoption in 2035', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Adoption Rate (%)', fontsize=13)
ax.set_xlabel('Countries', fontsize=13)
ax.set_xticks(x_pos)
ax.set_xticklabels(countries, fontsize=11)

# Annotate bars with values
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval - 5, f'{yval}%', ha='center', va='bottom', color='white', fontsize=10, fontweight='bold')

# Adding grid lines to the y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()