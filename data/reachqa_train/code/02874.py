import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
countries = ['Germany', 'China', 'United States', 'India', 'Brazil', 'United Kingdom', 'Australia', 'France', 'Canada', 'Japan']
installed_capacity = [150, 1200, 1000, 800, 600, 300, 200, 250, 400, 500]  # in Gigawatts

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create a color gradient from light to dark green
bar_colors = plt.cm.Greens(np.linspace(0.4, 0.8, len(countries)))
bars = ax.barh(countries, installed_capacity, color=bar_colors, edgecolor='black')

# Add labels and title
ax.set_xlabel('Installed Capacity (Gigawatts)', fontsize=12)
ax.set_title('Global Leadership in Renewable Energy:\nInstalled Capacity by Country (2023)', fontsize=16, fontweight='bold')
ax.set_xlim(0, max(installed_capacity) + 100)

# Add grid lines to improve readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Annotate each bar with the data value for better clarity
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Offset text slightly to the right
                textcoords='offset points',
                ha='left', va='center', fontsize=10, fontweight='bold', color='black')

# Adjust layout for aesthetics and visibility
plt.tight_layout()

# Display the plot
plt.show()