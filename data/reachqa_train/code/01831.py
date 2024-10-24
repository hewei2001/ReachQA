import matplotlib.pyplot as plt
import numpy as np

# Countries and coffee consumption data
countries = ['Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 
             'Sweden', 'Switzerland', 'Belgium', 'Canada', 'Brazil']
consumption_kg = [12, 9.9, 9, 8.7, 8.4, 8.2, 7.9, 6.8, 6.5, 6.1]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each bar
colors = plt.cm.cividis(np.linspace(0.2, 0.8, len(countries)))

# Plotting horizontal bars
bars = ax.barh(countries, consumption_kg, color=colors, edgecolor='darkslategray')

# Titles and labels
ax.set_title('Global Caffeine Rush:\nTop Coffee Consuming Countries in 2023', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Average Annual Coffee Consumption (kg per capita)', fontsize=12)

# Annotate each bar with the corresponding consumption value
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width} kg',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # Offset text position
                textcoords='offset points',
                ha='left', va='center', fontsize=10, color='black')

# Enhancing the layout with grid and style
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)

# Reverse the order to have the highest consumption on top
ax.invert_yaxis()

# Customize tick params for better label alignment
ax.tick_params(axis='y', which='major', labelsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()