import matplotlib.pyplot as plt
import numpy as np

# Countries and coffee consumption data
countries = ['Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 
             'Sweden', 'Switzerland', 'Belgium', 'Canada', 'Brazil']
consumption_kg = [12, 9.9, 9, 8.7, 8.4, 8.2, 7.9, 6.8, 6.5, 6.1]

# Hypothetical growth trend data (percentage changes over recent years)
growth_rate = [1.5, 1.2, 2.0, -0.5, 0.8, 1.0, 0.3, 0.5, 0.6, 1.1]

# Create a horizontal bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors for each bar
colors = plt.cm.cividis(np.linspace(0.2, 0.8, len(countries)))

# Plotting horizontal bars
bars = ax1.barh(countries, consumption_kg, color=colors, edgecolor='darkslategray')

# Titles and labels
ax1.set_title('Global Caffeine Rush:\nTop Coffee Consuming Countries in 2023', 
              fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Average Annual Coffee Consumption (kg per capita)', fontsize=12)

# Annotate each bar with the corresponding consumption value
for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width} kg',
                 xy=(width, bar.get_y() + bar.get_height() / 2),
                 xytext=(3, 0),  # Offset text position
                 textcoords='offset points',
                 ha='left', va='center', fontsize=10, color='black')

# Enhancing the layout with grid
ax1.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_axisbelow(True)

# Reverse the order to have the highest consumption on top
ax1.invert_yaxis()

# Customize tick params
ax1.tick_params(axis='y', which='major', labelsize=10)

# Create a second y-axis for growth rate overlay
ax2 = ax1.twinx()
ax2.plot(growth_rate, countries, marker='o', color='royalblue', linestyle='-',
         label='Growth Rate (%)')

# Add labels and styling for the second axis
ax2.set_ylabel('Coffee Consumption Growth Rate (%)', fontsize=12, color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue', labelsize=10)

# Add a legend to differentiate between the datasets
ax2.legend(loc='lower right', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()