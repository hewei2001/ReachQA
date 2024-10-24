import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Define the countries and their annual coffee consumption per person (in kg)
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Denmark', 
             'Switzerland', 'Germany', 'Brazil', 'USA', 'Italy']
consumption = np.array([12.0, 10.5, 9.8, 9.0, 8.5, 7.9, 6.5, 5.0, 4.5, 4.0])

# Generate colors for the bars using a colormap
color_map = plt.get_cmap("YlGnBu")
colors = color_map(np.linspace(0.3, 0.9, len(countries)))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the horizontal bar chart
bars = ax.barh(countries, consumption, color=colors, height=0.6, edgecolor='darkblue')

# Add text annotations for each bar
for bar, value in zip(bars, consumption):
    ax.text(value + 0.1, bar.get_y() + bar.get_height() / 2, f'{value:.1f} kg', 
            va='center', fontsize=9, color='darkblue')

# Title and axis labels
ax.set_title('Global Coffee Culture:\nAnnual Consumption Per Capita by Country', 
             fontsize=18, color='darkgreen', weight='bold', pad=20)
ax.set_xlabel('Consumption (kg per person)', fontsize=12, color='darkolivegreen')
ax.set_ylabel('Countries', fontsize=12, color='darkolivegreen')

# Customizing the axis and grid
ax.set_xlim(0, max(consumption) + 2)
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.4)
ax.set_axisbelow(True)  # Ensure grid lines are behind bars

# Format the y-ticks
ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries, fontsize=11, color='darkgreen')

# Adjust layout to fit everything neatly
plt.tight_layout()

# Show the plot
plt.show()